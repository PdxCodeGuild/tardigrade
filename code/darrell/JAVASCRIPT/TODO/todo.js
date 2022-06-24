
let textField = document.getElementById('user_input');
let incompleteUl = document.getElementById('incomplete_list');
let CompleteUl = document.getElementById('complete_list');
let LI = document.getElementsByTagName('li');



const btn1 = document.getElementById('btn1');
btn1.addEventListener("click", function() {
    let textValue = textField.value;
    const newLI = document.createElement('LI');
    newLI.innerHTML += `<li> <div id="list_text">${textValue}</div><nbsp/></div id="list_buttons"><button id='completed_btn'>Completed</button> <button id='deleted_btn'>Delete</button></div></li>`;
    incompleteUl.appendChild(newLI);
    

});

incompleteUl.addEventListener("click", function(event) {
    if (event.target.tagName === 'BUTTON' && event.target.innerText === 'Completed') {
        let targetLI = event.target.parentElement.parentElement.parentElement
        CompleteUl.appendChild(targetLI);
    } else if (event.target.tagName === 'BUTTON' && event.target.innerText === 'Delete') {
        let targetLI = event.target.parentElement.parentElement.parentElement
        incompleteUl.removeChild(targetLI);
        console.log(targetLI);
    }
});
 
