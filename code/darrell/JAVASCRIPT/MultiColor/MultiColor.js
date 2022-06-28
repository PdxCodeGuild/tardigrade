

const btn = document.getElementById('newColor');
const btn2 = document.getElementById('newPageColor');
const body = document.getElementById('wrapper');
const bodyP =document.getElementById('body')
const heading = document.getElementById('heading');

btn.addEventListener("click", ()=>{

    let randomRed = Math.floor(Math.random() * (255-0) +0);
    let randomGreen = Math.floor(Math.random() * (255-0) +0);
    let randomBlue = Math.floor(Math.random() * (255-0) +0);
    

    let rgb = (`rgb(${randomRed}, ${randomGreen}, ${randomBlue})`);
    console.log(rgb);

    heading.style.color = rgb;
    heading.innerText = `Multi-Color Heading:  ${rgb}`;


})


btn2.addEventListener("click", ()=>{

    let randomRed = Math.floor(Math.random() * (255-0) +0);
    let randomGreen = Math.floor(Math.random() * (255-0) +0);
    let randomBlue = Math.floor(Math.random() * (255-0) +0);
    

    let rgb = (`rgb(${randomRed}, ${randomGreen}, ${randomBlue})`);
    console.log(rgb);

    body.style.backgroundColor = rgb;
    bodyP.innerText = `${rgb}`;




});