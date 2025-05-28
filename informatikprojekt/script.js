//Bestellen

function buy(event) {
    event.preventDefault();
    let req = {};
    req["name"] = document.getElementById("firstname").value + " " + document.getElementById("lastname").value;
    req["mail"] = document.getElementById("mail").value;

    fetch("https://lajoka.de/informatikprojekt", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(req)
    })
        .then((response) => response.json())
        .then(async (data) => {
            console.log("ok");
        });

    document.querySelectorAll("input").forEach(i => i.value != "Bestellen" ? i.value = "" : null);
    document.querySelectorAll("input").forEach(i => i.type == "radio" ? i.checked = false : null);
    document.querySelector("option").selected = true;
    document.querySelector("#success").innerText = "Vielen Dank für Ihre Bestellung.";
}

//Galerie
function shrink(img) {
    img.style.transform = "scale(1)";
    img.style.zIndex = 0;
    
    if(img.classList.contains("big_gallery_image")){
        img.classList.remove("big_gallery_image")
    } else if(img.classList.contains("big_gallery_image_right")) {
        img.classList.remove("big_gallery_image_right")
    } else if(img.classList.contains("big_gallery_image_left")) {
        img.classList.remove("big_gallery_image_left")
    }
    
}
function enlarge(img, position) {
    img.style.transform = "scale(1.5)";
    img.style.zIndex = 1;
    img.style.opacity = 1;
    img.classList.add("big_gallery_image" + position)
}
function hide(img) {
    img.style.opacity = 0.6;
}
function show() {
    document.querySelectorAll(".gallery_image").forEach(img => img.style.opacity = 1);
}
function max_img(event) {
    const clicked_img = event.target;
    let position;
    document.querySelectorAll(".gallery_image").forEach((img, index) => {
        if (img != clicked_img) {
            shrink(img);
            hide(img);
        } else {
            position = getPosition(index);
        }
    });
    const img_scale = clicked_img.style.transform;
    if (img_scale == "scale(1.5)") {
        shrink(clicked_img);
        show();
    } else {
        enlarge(clicked_img, position);
    }
};
function getPosition(index){
    if(index % 3 == 0) {
        return "_left";
    } else if(index % 3 == 2){
        return "_right";
    } else {
        return "";
    }
}
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".gallery_image").forEach(img => img.addEventListener("click", max_img));
});
