//encontrar os buttons de like
//encontrar os button de dislike



function LikeImg(_btn,_img) {

    url = 'like_Img/';

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getToken('csrftoken'),
        },
        body:JSON.stringify({'img_id':_img})
    })

    .then(response => response.json())
    .then(data => console.log(data))
    .then(data => update_CartBar());
}

function DislikeImg(_btn,_img) {

    url = 'dislike_Img/';

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getToken('csrftoken'),
        },
        body:JSON.stringify({'img_id':_img})
    })

    .then(response => response.json())
    .then(data => console.log(data))
    .then(data => update_CartBar());
}

function display_disliked() {

        var txt = 'Ativar ou desativar esta opção faz com que você veja ou nao as fotos com dislike, você deseja confirmar?';
        if (confirm(txt)) {
            location.reload();
            
        } else {
            location.reload();
        }
}
