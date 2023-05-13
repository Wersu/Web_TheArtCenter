# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from www import app, db, login_manager
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json
from werkzeug.security import generate_password_hash,  check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user

"""

    Модуль регистрации маршрутов для запросов к серверу, т.е.
    здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения

"""

# Структура основного навигационнго меню веб-приложения,
# оформленное в виде массива dict-объектов
navmenu = [
    {
        'name': 'Главная',
        'addr': '/'
    },
    {
        'name': 'Картины',
        'addr': '/pictures'
    },
    {
        'name': 'Художники',
        'addr': '/artist'
    },
]

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

# Обработка запроса к индексной странице
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='the Art Center', navmenu=navmenu)

# Обработка запроса к странице pictures.html
@app.route('/pictures')
def pictures():
    pictures = ImageInfo.query.all()

    lenFirst = 0

    for x in range(0, len(pictures)):
        if x%2!=0:
            lenFirst+=1
            
    picturesFirst = pictures[:lenFirst]
    picturesSecond = pictures[lenFirst:]

    return render_template('pictures.html', title='the Art Center', navmenu=navmenu, l1=picturesFirst,l2=picturesSecond)

# Обработка запроса к странице artist.html
@app.route('/artist')
def artist():
    return render_template('artist.html', title='the Art Center', navmenu=navmenu)

@app.route("/addpictures")
@login_required
def add_pictures():
    return render_template('addPictures.html', title='the Art Center', navmenu=navmenu,logs = current_user.get_logs())

@app.route("/editpictures")
@login_required
def edit_pictures(): 
    modelId = request.args.get('id', default = 1, type = int)

    model = ImageInfo.query.filter_by(id=modelId).first()

    return render_template('editPictures.html', title='the Art Center', navmenu=navmenu, imageModel = model,logs = current_user.get_logs())


# Обработка POST-запроса для демонстрации AJAX
@app.route('/api/addpictures', methods=['POST'])
@login_required
def post_add_picture():
    jsonData = json.loads(request.form['json'])

    if not jsonData:
        return json_response({ 'message': "no json" })

    fileData = jsonData['file']

    if not fileData:
        return json_response({ 'message': "no file" })

    out_file = open("www/static/images/pictures/" + jsonData['filename'], 'wb')
    out_file.write(bytearray(fileData))
    out_file.close()

    db.session.add(ImageInfo(
        artName=jsonData['picture'],
        artistName=jsonData['artist'],
        fileName=jsonData['filename'],
        year=jsonData['year'],
        ))
    
    db.session.add(UserAction(
        userID = current_user.id,
        action = f"Добавление картины {jsonData['picture']}"
    ))
    
    db.session.commit()

    return json_response({ 'message': "Картина добавлена" })

@app.route('/api/editpicture', methods=['PUT'])
@login_required
def put_edit_picture():
    modelId = request.form['id']

    model = ImageInfo.query.filter_by(id=modelId).first()

    if not model:
        return json_response({ 'message': "Картина не найдена" })

    jsonData = json.loads(request.form['json'])

    if not jsonData:
        return json_response({ 'message': "no json" })

    fileData = jsonData['file']

    if fileData:
        out_file = open("www/static/images/pictures/" + jsonData['filename'], "wb")
        out_file.write(bytearray(fileData))
        out_file.close()

    model.artName=jsonData['picture']
    model.artistName=jsonData['artist']
    model.year=jsonData['year']
    model.fileName=jsonData['filename']
    
    db.session.add(UserAction(
        userID = current_user.id,
        action = f"Изменение картины {jsonData['picture']}"
    ))
    db.session.add(model)
    db.session.commit()

    return json_response({ 'message': "Картина обновлена" })


@app.route('/api/deletepicture', methods=['DELETE'])
@login_required
def delete_picture():

    modelId = request.form['id']

    model = ImageInfo.query.filter_by(id=modelId).first()

    if not model:
        return json_response({ 'message': "Картина не найдена" })

    db.session.add(UserAction(
        userID = current_user.id,
        action = f"Удаление картины {model.artName}"
    ))
    db.session.delete(model) 
    db.session.commit()

    return json_response({ 'message': "Картина удалена" })

@app.route('/login')
def login():
    return render_template('login.html', title='the Art Center', navmenu=navmenu)

@app.route('/api/login', methods=['POST'])
def login_post():
    loginVal = request.form['login']
    password = request.form['password']

    targetUser = User.query.filter_by(login=loginVal).first()

    if not targetUser:
        return json_response({ 'message': "Пользователь не найден" },400)
    
    if not User.check_password(targetUser,password):
        return json_response({ 'message': "Неправильный пароль" },400)
    
    login_user(targetUser)

    return render_template('index.html', title='the Art Center', navmenu=navmenu)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html', title='the Art Center', navmenu=navmenu)

@app.route('/reg')
def reg():
    return render_template('registration.html', title='the Art Center', navmenu=navmenu)

@app.route('/api/reg', methods=['POST'])
def post_reg():
    loginVal = request.form.get('login')
    password = request.form.get('password')

    targetUser = User.query.filter_by(login=loginVal).first()

    if targetUser:
        return json_response({ 'message': "Уже зарегестрирован" },400)
    
    targetUser = User()

    targetUser.login = loginVal
    targetUser.set_password(password)

    db.session.add(targetUser)
    db.session.commit()

    login_user(targetUser)

    return render_template('index.html', title='the Art Center', navmenu=navmenu)

"""

    Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP

"""


# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

class ImageInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artName = db.Column(db.String(100), nullable=False)
    artistName = db.Column(db.String(100), nullable=False)
    fileName = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def check_password(self,  password):
        return check_password_hash(self.password, password)

    def get_logs(self):
        return UserAction.query.filter_by(userID=self.id)

    def load_user(user_id):
        return db.session.query(User).get(user_id)

    def set_password(self, password):
	    self.password = generate_password_hash(password)
            
class UserAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    action = db.Column(db.String(100), nullable=False)
        