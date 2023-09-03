var imgs_modal = document.getElementById('imgs_modal');
var bigImage = document.getElementById('big_img');

hideModal();
var imgID_on_ModalView=0;


function hideModal() {
    imgs_modal.style.display = 'none';
    imgID_on_ModalView = 0;
}

function showModal(img,img_id) {
    imgs_modal.style.display = 'flex';
    bigImage.src = img.src;
    imgID_on_ModalView = img_id;
}