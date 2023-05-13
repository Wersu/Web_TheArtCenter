$(document).ready(function() {
	$(".hideText").hide();
	$(".hidebox .paintText").css("background-color", "#aa86f4");
    $(".hidebox .artistText").css("background-color", "#72dab9");
    $(".hidebox .ganre").css("background-color", "#f5ea54");
});

$(".hidebox h3").click(function () {
    var container = $(this).next("div");

    container.prop('isShowed',!container.prop('isShowed'));

var nextContainer = container.next(".hidetext");
while(nextContainer.lenght>0)
{
    nextContainer.prop('isShowed',false);

    proceedContainer(nextContainer);

    nextContainer = nextContainer.next(".hidetext");
}

    proceedContainer(container);
});

function proceedContainer(container)
{
    if(container.prop('isShowed'))
        {
            container.show("fast");
            container.prev("h3").css("background-color", "#90ccfd");
        }
        else
        {
            container.hide("fast");
            container.prev(".paintText").css("background-color", "#aa86f4");
            container.prev(".artistText").css("background-color", "#72dab9");
            container.prev(".ganre").css("background-color", "#f5ea54");
        }
}


 $(".art").click(function() {
    var img = $(this).find("img"); // use a variable to store your image element in case you have to change the container class
    var img_type = img.attr("src"); // not necessary to store it, could be use as it in the if statement
    var img_id = img.attr("imgId");

    document.getElementById("big-pic").innerHTML =
    (`
    <div class="art-preview">
    <img onClick='close_pic()' class='big-opened-pic' src='${img_type}'>
    <a href="editpictures?id=${img_id}">Редактировать</a>
    </div>
    <div onClick='close_pic()' class='full-tint'>
    </div> 
    `)
});


function close_pic() {
  document.getElementById("big-pic").innerHTML = ""
}