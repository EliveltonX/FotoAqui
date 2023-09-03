message = document.getElementById('message_bar');

setTimeout(hideMessages,5000);

function hideMessages() {
    //Em caso de n haver menssagens!
    if (message == null) {
        return
    }
    message.style.display = 'none';
}