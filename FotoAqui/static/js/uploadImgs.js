var file_input = document.getElementById("imgs");
var image_container = document.getElementById("upload_imgs_preview");
var numOfFiles = document.getElementById("numOfFiles");

file_input.setAttribute("onchange","preview()");
image_container.setAttribute('display','none');


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
}