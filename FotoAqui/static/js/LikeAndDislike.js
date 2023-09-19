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

    var txt = 'Você deseja remover esta Foto? Ela nao poderá ser recuperada e não aparecera na sua lista de imagens!';
    url = 'dislike_Img/';

    if (confirm(txt)) {
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
        .then(data => update_CartBar())
        .then(data => location.reload());      
    } else {
        //location.reload();
    }
}

function eliminar_fotos_Dislike() {
    mybool = document.querySelector('#display_disliked').checked;
    console.log('eliminar fotos com dislike: '+mybool);
}