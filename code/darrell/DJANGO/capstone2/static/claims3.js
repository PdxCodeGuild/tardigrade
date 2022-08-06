// jshint esversion: 6 

const tdDSLN = document.getElementsByClassName("item_div dsln");

for (let i=0; i < tdDSLN.length; i++) {

    console.log(tdDSLN[i].textContent);

    if (tdDSLN[i].textContent > 59) {
        tdDSLN[i].style.backgroundColor = "#ff4364";
    } else {
        tdDSLN[i].style.backgroundColor = "";
    }

}


