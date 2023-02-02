//constantes de DOM 
const body = document.getElementById("body-all");
const navbar = document.querySelector(".navbar");
const whois = document.querySelector("#whois");
const nost = document.querySelector('#nuestros');
const proyect = document.querySelector('#proyecto');
const footer = document.querySelector('.footer');


//funciones generacion genericas
function divflex() {
    let newdiv = document.createElement('div');
    newdiv.setAttribute('class', 'd-flex justify-content-center align-items-center flex-row flex-wrap');
    return newdiv;
}



//Header
function dibujarHeader(data) {
    const navband = data.band[0];
    const navul = data.nav;

    navbar.childNodes[1].textContent = navband;


    const dibujarMenu = (text, url) => {
        let newdiv = document.createElement('div');
        return newdiv.innerHTML = '<li class="nav-item"><a class="nav-link " href="' + url + '">' + text + '</a></li>';
    }


    for (let datos in navul) {
        let newdiv = document.createElement('div');
        newdiv.innerHTML = dibujarMenu(datos, navul[datos]);
        navbar.childNodes[5].childNodes[1].appendChild(newdiv);
    }
}

//whois

function dibujarwhois(data) {
    const h1 = whois.childNodes[1].childNodes[1].childNodes[3];
    const p = whois.childNodes[1].childNodes[1].childNodes[5];
    const h1Text = data.whois.h1;
    const pText = data.whois.p;

    console.log(data.whois)

    whois.childNodes[1].childNodes[1].childNodes[1].attributes[0].nodeValue = data.whois.img

    h1.textContent = h1Text;

    p.textContent = pText;

}


//Nuestros servicios

function dibujarnuestros(data) {
    const divmain = nost.childNodes[5];
    const contentNost = data.nuestros.content;

    let arryIcon = new Array();
    let arrytext = new Array();


    for (let datos in contentNost) {
        let contenido = contentNost[datos];
        for (let text in contenido) {
            text == 'icon' ? arryIcon.push(contenido[text]) : arrytext.push(contenido[text]);
        }

    }

    const icon = (url, alt) => {
        return '<div class="icon-svg"><img src="' + url + '" alt="' + alt + '"></div><br>';
    }


    const texto = (text) => {
        return '<div class="text-justify text-center" style="width: 80%;"><h4><strong>' + text.h4 + '</strong></h4><p>' + text.h4 + '</p></div>';
    }

    let contador = 0
    for (let datos in contentNost) {
        let divsvgCons = divmain.appendChild(divflex());
        divsvgCons.innerHTML = icon(arryIcon[contador], 'np') + texto(arrytext[contador]);
        contador++;
    }

    nost.childNodes[3].textContent = data.nuestros.h1;

}

//Nuestros proyectos

function dibujarproyectos(data) {
    const datos = data.proyectos
    proyect.childNodes[3].textContent = datos.h1


    const divImg = proyect.childNodes[5]

    for (let imgen in datos.img) {
        let newdiv = document.createElement('div')
        newdiv.setAttribute('class', 'img-proyect')
        newdiv.innerHTML = '<img src="' + datos.img[imgen] + '" alt="' + imgen + '" class="rounded d-block proyecto"></img>'
        divImg.appendChild(newdiv)
    }
}


//footer

function dibujarfooter(data){
    footer.textContent = data.text
}



//lector de json asincrona

const xhttp = new XMLHttpRequest();


xhttp.open('GET', './asset/main.json', true);

xhttp.send();

xhttp.onreadystatechange = function () {

    //validamos que la informacion se consiquiera correctamente
    this.readyState == 4 && this.status == 200 ? dibujar(JSON.parse(this.responseText)) : console.error('404 NOT FOUND : ' , this.status);

    //funcion para dibuhar en pantalla

    function dibujar(data) {


        dibujarHeader(data.header);
    
        dibujarwhois(data.main);

        dibujarnuestros(data.main);

        dibujarproyectos(data.main);

        dibujarfooter(data.footer)

    }

}
