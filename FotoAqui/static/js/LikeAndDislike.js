//encontrar os buttons de like
//encontrar os button de dislike


function LikeImg(_btn,_img) {

    url = 'like_Img/';

    _btn.style.display = 'none';
    document.getElementById('btn-removeLike_'+_img).style.display = 'block';

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

function RemoveLikeImg(_btn,_img) {

    url = 'remove_like_Img/';

    _btn.style.display = 'none';
    document.getElementById('btn-likeThisImg_'+_img).style.display = 'block';

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

Liked_Disliked();
function Liked_Disliked() {
    like_btn = document.getElementsByClassName('btn-likeThisImg');
    dislike_btn = document.getElementsByClassName('btn-removeLike');

    for (let i = 0; i < like_btn.length; i++) {

       if (like_btn[i].getAttribute('like') == 'True') {
            like_btn[i].style.display= 'none';
            dislike_btn[i].style.display = 'block';
       }else{
            like_btn[i].style.display= 'block';
            dislike_btn[i].style.display = 'none';
       }
        
    }

}