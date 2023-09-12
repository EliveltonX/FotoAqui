var cart_bar = document.getElementById('cart_bar');
var in_cart_list;


update_CartBar();


function show_cart_bar() 
{

    cart_bar.style.display = 'block';

}

function hide_cart_bar() {
    cart_bar.style.display = 'none'
}


function displayIfNotEmpty() {

    if (in_cart_list<=0) {
        hide_cart_bar();
    }else{
        show_cart_bar();
    }
}


function update_CartBar() {
    
    url = "/update_cart_bar/";
    
    fetch(url,{
        method:'GET',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getToken('csrftoken'),
        },
    })
    
    .then(response => response.json())
    .then(data => update(data));

    function update(data) {
        console.log(data);
        qtd = data.qtd;
        vl_total = data.vl * qtd;
        //console.log(data[message]);
        in_cart_list = qtd
        _qtd = document.getElementById('cart_bar_qtd').innerHTML = 'Imagens Selecionadas: ' + qtd;
        _vl = document.getElementById('cart_bar_value').innerHTML = 'Valor Total: ' + vl_total.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
        displayIfNotEmpty();
    }

    /*
    vl = qtd*price;
    in_cart_list = qtd
    _qtd = document.getElementById('cart_bar_qtd').innerHTML = 'Imagens Selecionadas: ' + qtd;
    _vl = document.getElementById('cart_bar_value').innerHTML = 'Valor Total: ' + vl.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
    displayIfNotEmpty();
    */
}

function addToCart(_btn,_img) {

    url = "/add_to_cart/";

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

        document.getElementById('btn-addtocart_'+_img).style.display = 'none';
        document.getElementById('btn-removetocart_'+_img).style.display = 'flex';
        document.getElementById('img_selection_highlight_'+_img).style.display='flex';
}

function removeFromCart(_btn,_img) {

    url = "/remove_to_cart/";

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

        document.getElementById('btn-addtocart_'+_img).style.display = 'flex';
        document.getElementById('btn-removetocart_'+_img).style.display = 'none';
        document.getElementById('img_selection_highlight_'+_img).style.display='none';
}

cart_link = document.getElementById('cart_link');
function go_to_cart(){

 url = "/create_order/";

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':getToken('csrftoken'),
        },
        body:JSON.stringify({'in_cart_list':Object(in_cart_list)})
    })
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        cart_link.click();
    });
}

hideRemoveButtons();
function hideRemoveButtons() {

    list_imgs = document.getElementsByClassName('imageToBuy');
    //console.log(list_imgs[8].getAttribute('onCart'))

    for (let i = 0; i < list_imgs.length; i++) {

        add = document.getElementById('btn-addtocart_'+list_imgs[i].id)
        rem = document.getElementById('btn-removetocart_'+list_imgs[i].id)
        overlay = document.getElementById('img_selection_highlight_'+list_imgs[i].id)

        console.log(list_imgs[i].getAttribute('onCart') == 'None');

        if(list_imgs[i].getAttribute('onCart') == 'None'){
            rem.style.display = 'none';
            overlay.style.display='none';
            add.style.display = 'flex';
        }else{
            add.style.display = 'none';
            overlay.style.display='flex';
            rem.style.display = 'flex';
        }
        
    }
}