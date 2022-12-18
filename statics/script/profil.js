let maj = document.getElementById("maj");
let annuler = document.getElementById("annuler");
let annulerPasswd = document.getElementById("annuler-passwd");
let annulerReini = document.getElementById("annuler-reini");
let oublier = document.getElementById("passwd-oublier");
let modif = document.getElementById("modif-passwd")
let d1 = document.getElementById("d1");
let d2 = document.getElementById("d2");
let d3 = document.getElementById("d3");
let d4 = document.getElementById("d4");

maj.addEventListener("click", () => {
  if(getComputedStyle(d1).display != "none"){
    d1.style.display = "none";
    d3.style.display = "none";
    d2.style.display = "block";
    d4.style.display = "none";
  } else {
    d1.style.display = "block";
    d2.style.display = "none";
    d3.style.display = "none";
    d4.style.display = "none";
  }
});

annuler.addEventListener("click", () => {
  if(getComputedStyle(d1).display != "none"){
    d1.style.display = "block";
    d3.style.display = "none";
    d2.style.display = "none";
    d4.style.display = "none";
  } else {
    d1.style.display = "block";
    d2.style.display = "none";
    d3.style.display = "none";
    d4.style.display = "none";
  }
});


modif.addEventListener("click", () => {
  if(getComputedStyle(d1).display != "none"){
    d1.style.display = "none";
    d3.style.display = "none";
    d2.style.display = "block";
    d4.style.display = "none";

  } else {
    d1.style.display = "none";
    d2.style.display = "none";
    d3.style.display = "block";
    d4.style.display = "none";
  }
});

annulerPasswd.addEventListener("click", () => {
  if(getComputedStyle(d1).display != "none"){
    d1.style.display = "none";
    d3.style.display = "none";
    d2.style.display = "block";
    d4.style.display = "none";

  } else {
    d1.style.display = "none";
    d2.style.display = "block";
    d3.style.display = "none";
    d4.style.display = "none";
  }
});

oublier.addEventListener("click", () => {
  if(getComputedStyle(d1).display != "none"){
    d1.style.display = "none";
    d2.style.display = "block";
    d3.style.display = "none";
    d4.style.display = "none";
  } else {
    d1.style.display = "none";
    d2.style.display = "none";
    d3.style.display = "none";
    d4.style.display = "block";

  }
});

annulerReini.addEventListener("click", () => {
  if(getComputedStyle(d1).display != "none"){
    d1.style.display = "none";
    d2.style.display = "block";
    d3.style.display = "none";
    d4.style.display = "none";
  } else {
    d1.style.display = "none";
    d2.style.display = "none";
    d3.style.display = "block";
    d4.style.display = "none";

  }
});
