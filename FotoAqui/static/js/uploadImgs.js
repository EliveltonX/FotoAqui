var input_email = document.getElementById("id_client_email");
var file_input = document.getElementById("imgs");
var image_container = document.getElementById("upload_imgs_preview");
var numOfFiles = document.getElementById("numOfFiles");
var submitBtn = document.getElementById("uploadSubmitBtn");

file_input.setAttribute("onchange","preview()");
input_email.setAttribute("onchange","enableBtn()");
input_email.disabled = true;
submitBtn.disabled = true;


function preview() {
    image_container.innerHTML = "";
    numOfFiles.textContent = file_input.files.length + ' Imagens Selecionadas.';
    
    for(i of file_input.files){
        let reader = new FileReader();
        let figure = document.createElement("figure");
        let figCap = document.createElement("figcaption");
        figCap.innerText = i.name; 
        figure.appendChild(figCap);
        reader.onload=()=>{
            let img = document.createElement("img");
            img.setAttribute("src",reader.result);
            img.setAttribute("class",'img_preview');
            figure.insertBefore(img,figCap);
            
        }
        image_container.appendChild(figure);
        reader.readAsDataURL(i);
    }
    input_email.disabled = false;
}

function enableBtn() {
    if (input_email.value.length != 0) {
        submitBtn.disabled = false;
    }
}