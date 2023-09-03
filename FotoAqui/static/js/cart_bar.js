var cart_bar = document.getElementById('cart_bar');
var in_cart_list = []


displayIfNotEmpty();


function show_cart_bar() 
{

    cart_bar.style.display = 'block';

}

function hide_cart_bar() {
    cart_bar.style.display = 'none'
}


function displayIfNotEmpty() {

    if (in_cart_list.length<=0) {
        hide_cart_bar();
    }else{
        show_cart_bar();
    }
}


function update_CartBar() {
    qtd = in_cart_list.length;
    vl = qtd*price;
    _qtd = document.getElementById('cart_bar_qtd').innerHTML = 'Imagens Selecionadas: ' + qtd;
    _vl = document.getElementById('cart_bar_value').innerHTML = 'Valor Total: ' + vl.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
    displayIfNotEmpty();


}

function addToCart(_btn,_img) {

if (in_cart_list.includes(_img)) {
    return
}
    in_cart_list.push(_img);
    document.getElementById('btn-addtocart_'+_img).style.display = 'none';
    document.getElementById('btn-removetocart_'+_img).style.display = 'flex';
    update_CartBar()
}

function removeFromCart(_btn,_img) {
    if (in_cart_list.includes(_img)) {
        in_cart_list.splice(in_cart_list.indexOf(_img),1);
        
        update_CartBar()
        document.getElementById('btn-addtocart_'+_img).style.display = 'flex';
        document.getElementById('btn-removetocart_'+_img).style.display = 'none';
    }
    return
   
}
function clear_cart_bar(_btn) {
    in_cart_list = [];
    hideRemoveButtons();
    update_CartBar();
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

    list_add = document.getElementsByClassName('btn-addToCart');
    list_rem = document.getElementsByClassName('btn-removeFromCart');

    for (let i = 0; i < list_add.length; i++) {
        list_rem[i].style.display = 'none';
        list_add[i].style.display = 'flex';
    }

}