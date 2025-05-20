//Bestellen

function buy(event) {
    event.preventDefault();
    let req = {};
    req["name"] = document.getElementById("firstname").value + " " + document.getElementById("lastname").value;
    req["mail"] = document.getElementById("mail").value;

    fetch("https://lajoka.de:3006/informatikprojekt", {
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
function shrink(img){
    img.style.transform = "scale(1)";
    img.style.zIndex = 0;
}
function enlarge(img){
    img.style.transform = "scale(1.5)";
    img.style.zIndex = 1;
    img.style.opacity = 1;
}
function hide(img){
    img.style.opacity = 0.6;
}
function show(img){
    document.querySelectorAll(".gallery_image").forEach(img => img.style.opacity = 1);
}
function max_img(event){
    const clicked_img = event.target;
    document.querySelectorAll(".gallery_image").forEach(img => {
        if(img != clicked_img){
            shrink(img);
            hide(img);
        }
    });
    const img_scale = clicked_img.style.transform;
    if(img_scale == "scale(1.5)"){
        shrink(clicked_img);
        show();
    } else {
        enlarge(clicked_img);
    }
};

document.querySelectorAll(".gallery_image").forEach(img => img.addEventListener("click", max_img));