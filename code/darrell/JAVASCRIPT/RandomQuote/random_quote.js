

const btn = document.getElementById('newQuote');
btn.addEventListener("click", ()=>{

fetch('https://favqs.com/api/qotd').then((response)=>{
  response.json().then((data)=> {
      const quote = document.getElementById('quote');
      const author = document.getElementById('author');
      console.log(quote);
      console.log(author);
      quote.innerText = data.quote.body;
        console.log(data.quote.body);
      author.innerText = data.quote.author;
        console.log(data.quote.author);
    });

});

});

let textField = document.getElementById('quoteInput');
let quotesUL= document.getElementById('quotesUL');
let LI = document.getElementsByTagName('li');
let quotesList = [];
const btn2 = document.getElementById('newQuotes');

btn2.addEventListener("click", ()=>{
    
    quotesUL.innerHTML = '';
    console.log("btn 2 clicked");
    let textValue = textField.value;
    console.log(textValue);
    

    const myHeaders = new Headers();

    myHeaders.append('Authorization',  'Token token="83ff6c5e1850ac35856e1869206dd66e"');
    
    fetch(`https://favqs.com/api/quotes?page=1&filter=${textValue}`, {
      method: 'GET',
      headers: myHeaders,
    })
     .then(response=>response.json())
     .then(data=>{

        console.log(data)  
      
        /*console.log(data.quotes[1].body);
        console.log(data.quotes[1].author);*/
        const quotes = data.quotes;

        console.log(quotes);

        for (let i=0; i < quotes.length; i++ ) {
            const newLI = document.createElement('LI');
            newLI.innerHTML += `<li> <div id='quoteListItem'><h3 id="authors">${quotes[i].author}</h3><p id="quotes"><i>${quotes[i].body}</i></p></div></li>  `;
            quotesUL.appendChild(newLI);
            textField.value ='';

        }
        

        
    })
      .catch(error=>{
        console.error('There has been a problem with your fetch operation:', error);
      });    

}); 