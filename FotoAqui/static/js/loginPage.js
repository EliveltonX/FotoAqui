
var window_login = document.getElementById('loginWindow')
var window_register = document.getElementById('registerWindow')

ToLogin();

function ToRegister(){

window_login.style.display = "none";
window_register.style.display = "block";

}

function ToLogin() {

    window_register.style.display = "none";
    window_login.style.display = "block";
    
}


