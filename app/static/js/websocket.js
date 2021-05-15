var socket = io.connect(location.origin);

var input = document.querySelector('.input-message');
var button = document.querySelector('.send-message');
var element = document.querySelector('.box');


socket.on('message client', (data) => {
    addNewMessage(data.msg, data.id);
    element.scrollIntoView();
});

function sendMessageToServe() {
    const message = input.value;

    if (message) {
        socket.emit('message server', message);
        input.value = "";
    }
}

button.addEventListener('click', (event) => {
    sendMessageToServe();
});

input.addEventListener('keyup', (event) => {
    if (event.keyCode == '13' && event.ctrlKey) {
        sendMessageToServe();
    }
});



function addNewMessage(msg, id) {
    const element = document.querySelector('.items');
    let newElement = document.createElement('p');

    if (socket.id === id) {
        newElement.classList.add('msg-right');
    } else {
        newElement.classList.add('msg-left');
    }
    newElement.innerHTML = msg;
    element.appendChild(newElement);
}