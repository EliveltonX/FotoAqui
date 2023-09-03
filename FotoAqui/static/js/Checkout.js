
ShowValues();

//para atualizar os valores de acordo com o calculo
function ShowValues() {
document.getElementById('total_price').innerText = 'Total: ' + value.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });;
}

function completeOrder() {
    var url = "complete_order/";
    var csrftoken = getToken('csrftoken'); 

    fetch(url,{
        method:'POST',
        headers: {
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'order_id':order_id})
    })
}