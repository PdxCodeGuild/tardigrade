const btn = document.getElementById("btn")
const output = document.getElementById("output")
const animalChoice = document.getElementById('form')
const filterQuotes = document.getElementById('list')

let choice = null

animalChoice.addEventListener("click", (event) => {
    choice = event.target.value

})
console.log(animalChoice)


btn.addEventListener('click', () => {
    const myHeaders = new Headers();

    myHeaders.append('Authorization', 'Token token="83ff6c5e1850ac35856e1869206dd66e"');

    fetch(`https://favqs.com/api/quotes?page=2&filter=${choice}`, {
        method: 'GET',
        headers: myHeaders,
    })
        .then(response => response.json())  // turns my request into a readable format
        .then(data => {

            data.quotes.map(x => { 
                let quote = x.body
                // console.log(this.quote)
                const li = document.createElement('li')
                li.innerText = quote
                filterQuotes.appendChild(li)


            })
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });

})


