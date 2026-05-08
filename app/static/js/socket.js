const socket = io();

socket.on('task_update', function(data) {

    showToast(data.message);

    setTimeout(() => {

        location.reload();

    }, 1200);
});


function showToast(message) {

    const toast = document.createElement('div');

    toast.className =
        'toast-notification';

    toast.innerText = message;

    document.body.appendChild(toast);

    setTimeout(() => {

        toast.classList.add('show');

    }, 100);

    setTimeout(() => {

        toast.classList.remove('show');

        setTimeout(() => {

            toast.remove();

        }, 500);

    }, 2500);
}