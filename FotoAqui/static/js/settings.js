//responsavel por alterar as tabs do perfil e editar perfil
tab_perfil = document.getElementsByClassName('my_perfil')[0];
tab_edit_perfil = document.getElementsByClassName('perfil_edit')[0];
tab_photograper = document.getElementsByClassName('reg_fotographer')[0];
tab_help = document.getElementsByClassName('help')[0];

Show_myPerfil();

function Show_myPerfil() {
    tab_perfil.style.display = "flex";
    tab_edit_perfil.style.display = "none";
    tab_photograper.style.display = "none";
    tab_help.style.display = "none";
}
function Show_editPerfil() {
    tab_perfil.style.display = "none";
    tab_edit_perfil.style.display = "flex";
    tab_photograper.style.display = "none";
    tab_help.style.display = "none";
}
function Show_photographer() {
    tab_perfil.style.display = "none";
    tab_edit_perfil.style.display = "none";
    tab_photograper.style.display = "flex";
    tab_help.style.display = "none";
}
function Show_help() {
    tab_perfil.style.display = "none";
    tab_edit_perfil.style.display = "none";
    tab_photograper.style.display = "none";
    tab_help.style.display = "flex";
}