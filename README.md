# TheArtCenter
TheArtCenter - сайт, посвященный искусству. Здесь можно ознакомиться с самыми известными художниками и их работами. Веб приложение реализовано с использованием HTML, CSS, JavaScript: jQuery, Python.
## Скриншоты HTML-страницы с обозначением разметки базовых тегов
1.	Главная страница
![mainImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/main.png)
2.	Страница с картинами
![paint1Img](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/paint1.jpg)
![paint2Img](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/paint2.png)
4.	Страница с художниками
![artist1Img](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/artist1.jpg)
![artist2Img](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/artist2.png)
## Создание интерактивных элементов пользовательского интерфейса с помощью DOM, JavaScript и jQuery
JavaScript — это язык программирования, который в первую очередь применяют в вебе. С его помощью сайты делают интерактивными: добавляют всплывающие окна, анимацию, кнопки лайков и формы для отправки информации. Его ещё называют главным языком фронтенда — «лицевой» стороны сайта, с которой взаимодействуют пользователи.

jQuery  — набор функций JavaScript, фокусирующийся на взаимодействии JavaScript и HTML. Библиотека jQuery помогает легко получать доступ к любому элементу DOM, обращаться к атрибутам и содержимому элементов DOM, манипулировать ими.

В jQuery для отслеживания действий мыши наиболее часто используют следующие события:

*	mousedown
*	mouseup
*	click
*	mousemove
*	wheel
*	hover
*	mouseenter
*	mouseover
*	mouseleave
*	mouseout

Событие click является сложным событием, оно возникает после генерирования событий mousedown и mouseup. Событие mousedown возникает, когда указатель находится над элементом и кнопка мыши нажата. Событие mouseup происходит, когда указатель находится над элементом и кнопка мыши отпущена. Событие click генерируется, когда курсор находится над элементом, и клавиша мыши нажата и отпущена. Эти события могут получать любые HTML элементы.
### Анимация главного навигационного меню
Реализована анимация главного навигационного меню при наведении, при переходе на соответствующую ему страницу, при этом наименование раздела меняется в заголовке страницы.
![anim_nav_menu_Img](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/anim_nav_menu.jpg)
![anim_nav_menu_Img](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/anim_nav_menu2.png)
### Интерактивная форма
Создана форма из 3 полей и сделано так, чтобы при нажатии на кнопку ввода появлялось модальное окно с подтверждением введенных данных.
![input_dataImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/input_data.png)
![modal_windowImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/modal_window.png)
### Анимация текстовых блоков
*	Реализована анимация таком образом, чтобы при загрузке страницы были видны только заголовки, а при клике мышкой на заголовок соответствующий ему нижестоящий блок текста появлялся.
![main_textImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/main_text.png)
*	При повторном клике на этот же заголовок текст должен скрываться, а фон заголовка меняться.
![main_text_open_artistImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/main_text_open_artist.png)
![main_text_open_paintsImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/main_text_open_paints.png)
### Анимация изображений
При клике стиль изображения меняется и увеличивается.
![click_paintImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/click_paint.png)
При наведении на изображение картины появляется ее название.
![name_paintImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/name_paint.png)
## Создание веб-приложения. Применение подхода AJAX для обмена данными с сервером
Колбэк-функция - это функция, переданная в другую функцию в качестве аргумента, которая затем вызывается по завершению какого-либо действия.

AJAX - подход к построению интерактивных пользовательских интерфейсов веб-приложений, заключающийся в «фоновом» обмене данными браузера с веб-сервером. В результате при обновлении данных веб-страница не перезагружается полностью, и веб-приложения становятся быстрее и удобнее.

При использовании AJAX:
1.	Пользователь заходит на веб-страницу и нажимает на какой-нибудь её элемент;
2.	Скрипт (на языке JavaScript) определяет, какая информация необходима для обновления страницы;
3.	Браузер отправляет соответствующий запрос на сервер;
4.	Сервер возвращает только ту часть документа, на которую пришёл запрос;
5.	Скрипт вносит изменения с учётом полученной информации (без полной перезагрузки страницы).

Шаблонизатор - это программное обеспечение, позволяющее использовать html-шаблоны для генерации конечных html-страниц. Основная цель использования шаблонизаторов — это отделение представления данных от исполняемого кода. Часто это необходимо для обеспечения возможности параллельной работы программиста и дизайнера-верстальщика. Такой подход значительно ускоряет время разработки и прототипирования приложения, дизайнеру не нужно вникать в программирование, а программисту беспокоиться об интерфейсе.

Маршрутизация - процесс, который отвечает за определение обработчика для конкретной запрашиваемой страницы
Виды HTTP-запросов:
*	GET-	Позволяет запросить некоторый конкретный ресурс. Дополнительные данные могут быть переданы через строку запроса (Query String) в составе URL.О составляющих URL мы поговорим чуть позже. 
*	POST - Позволяет отправить данные на сервер. Поддерживает отправку различных типов файлов, среди которых текст, PDF-документы и другие типы данных в двоичном виде. Обычно метод POST используется при отправке информации (например, заполненной формы логина) и загрузке данных на веб-сайт, таких как изображения и документы.
*	HEAD - Здесь придется забежать немного вперед и сказать, что обычно сервер в ответ на запрос возвращает заголовок и тело, в котором содержится запрашиваемый ресурс. Данный метод при использовании его в запросе позволит получить только заголовки, которые сервер бы вернул при получении GET запроса к тому же ресурсу. Запрос с использованием данного метода обычно производится для того, чтобы узнать размер запрашиваемого ресурса перед его загрузкой.
*	PUT - Используется для создания (размещения) новых ресурсов на сервере. Если на сервере данный метод разрешен без надлежащего контроля, то это может привести к серьезным проблемам безопасности.
*	DELETE - Позволяет удалить существующие ресурсы на сервере. Если использование данного метода настроено некорректно, то это может привести к атаке типа «Отказ в обслуживании» (Denial of Service, DoS) из-за удаления критически важных файлов сервера.
*	OPTIONS - Позволяет запросить информацию о сервере, в том числе информацию о допускаемых к использованию на сервере HTTP-методов.
*	PATCH - Позволяет внести частичные изменения в указанный ресурс по указанному расположению.
### Интерактивная форма с регистрацией
![reg_formImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/reg_form.png)
### Форма добавления новой картины
![form_add_picImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/form_add_pic.png)
![form_add_pic_reqImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/form_add_pic_req.png)
## Создание и подключение базы данных к веб-приложению. Разработка REST-методов взаимодействия с базой данных веб-приложения
HTTP — это протокол, позволяющий получать различные ресурсы, например HTML-документы. Протокол HTTP лежит в основе обмена данными в Интернете. HTTP является протоколом клиент-серверного взаимодействия, что означает инициирование запросов к серверу самим получателем, обычно веб-браузером (web-browser). 

Клиенты и серверы взаимодействуют, обмениваясь одиночными сообщениями (а не потоком данных). Сообщения, отправленные клиентом, обычно веб-браузером, называются запросами, а сообщения, отправленные сервером, называются ответами.

Каждый запрос (англ. request) отправляется серверу, который обрабатывает его и возвращает ответ (англ. response). Между этими запросами и ответами как правило существуют многочисленные посредники, называемые прокси, которые выполняют различные операции и работают как шлюзы или кэш, например.

Основные HTTP-методы. 
* GET – метод запрашивает представление ресурса. Запросы с использованием этого метода могут только извлекать данные.
* POST – используется для отправки сущностей к определённому ресурсу. Часто вызывает изменение состояния или какие-то побочные эффекты.
* PUT – заменяет представление ресурса данными запроса.
* DELETE – удаляет указанный ресурс.
* HTTP-коды.

Код ответа (состояния) HTTP показывает, был ли успешно выполнен определённый HTTP запрос. Коды сгруппированы в 5 классов:
* Информационные 100 - 199
* Успешные 200 - 299
* Перенаправления 300 - 399
* Клиентские ошибки 400 - 499
* Серверные ошибки 500 – 599
### Создание базы данных (БД) 
Создание базы данных SQLite с таблицей, которая будет хранить данные, отправляемые с веб-формы приложения. 
![DB_beforeImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/DB_before.png)
![DB_afterImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/DB_after.png)
### Подключение БД 
Подключение БД к приложению и реализовать CRUD-методы для работы с таблицей, т.е. методы должны использовать следующие типы SQL-запросов: SELECT (с фильтром и без), INSERT, UPDATE, DELETE. 

При нажатии на картину она увеличивается и появляется кнопка редактирования
![edit_picImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/edit_pic.png)
![form_editImg](https://github.com/Wersu/Web_TheArtCenter/blob/main/img_readme/form_edit.png)
