
var menuIcon_Hamb = document.getElementById('menuIcon_Hamb')
var mobileMenu = document.getElementById('mobileMenu')

ShowMenu_Mobile()
function ShowMenu_Mobile() {

    if (mobileMenu.style.display =="none") {
        mobileMenu.style.display = "flex"
    }
    else
    {
        mobileMenu.style.display = "none"
    }
   
}