var message = document.getElementById("message");
var buttonClose = document.getElementById("btn-close");

buttonClose.onclick = function(){
    //hide the box
    message.className = 'close';
};
