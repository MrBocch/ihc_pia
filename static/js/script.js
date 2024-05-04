document.getElementById("icon-menu").addEventListener("click", mostrar_menu);

function mostrar_menu() {
    document.getElementById("move-content").classList.toggle('move-container-all');
    document.getElementById("show-menu").classList.toggle('show-lateral');
}

// Obtener el elemento del encabezado
var header = document.querySelector("header");
var logoHeader = document.querySelector(".logo-header");
var initialHeaderHeight = header.clientHeight;
var headerText = document.querySelector(".logo h1");

// Añadir un event listener para el desplazamiento
window.addEventListener("scroll", function () {
    var scrollPosition = window.scrollY || window.pageYOffset;

    if (scrollPosition > initialHeaderHeight) {
        header.style.height = "50px";
        logoHeader.style.display = "none";
    } else {
        header.style.height = initialHeaderHeight + "px";
        logoHeader.style.display = "block";

        headerText.style.display = "block";
        headerText.style.alignItems = "initial";
    }
});

//Enlaces de redes sociales
const enlacesRedesSociales = {
    facebook: "https://www.facebook.com/tupagina",
    whatsapp: "https://wa.me/tunumerodetelefono",
    instagram: "https://www.instagram.com/tuinstagram",
    twitter: "https://twitter.com/tutwitter"
};

document.addEventListener("DOMContentLoaded", function() {
    // Obtén los elementos <a> y actualiza sus atributos href
    document.getElementById("enlace-facebook").href = enlacesRedesSociales.facebook;
    document.getElementById("enlace-whatsapp").href = enlacesRedesSociales.whatsapp;
    document.getElementById("enlace-instagram").href = enlacesRedesSociales.instagram;
    document.getElementById("enlace-twitter").href = enlacesRedesSociales.twitter;
});
