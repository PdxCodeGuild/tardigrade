// Creating varaibles to access the elements from the html file to manipulate// 
let addToDoButton = document.getElementById('addToDo')
let toDoContainer = document.getElementById('toDoContainer')
let doneListContainer = document.getElementById('doneListContainer')
let inputField = document.getElementById('inputField')

addToDoButton.addEventListener('click', function(){
    let paragraph = document.createElement('p')
    let deleteBtn = document.createElement('button')
    let completedBtn = document.createElement('button')
    deleteBtn.innerText = "Delete"
    completedBtn.innerText = "Cross/Uncoss"
    paragraph.innerText = inputField.value 
    toDoContainer.appendChild(paragraph) 
    toDoContainer.appendChild(completedBtn)
    toDoContainer.appendChild(deleteBtn)
    inputField.value = ""
    completedBtn.addEventListener('click', function(event){
        if (paragraph.style.textDecoration == ""){
            paragraph.style.textDecoration = "line-through"
            doneListContainer.appendChild(paragraph) 
            doneListContainer.appendChild(completedBtn)
            doneListContainer.appendChild(deleteBtn)
        }else{
            paragraph.style.textDecoration = ""
            toDoContainer.appendChild(paragraph) 
            toDoContainer.appendChild(completedBtn)
            toDoContainer.appendChild(deleteBtn)
        }
    })
    deleteBtn.addEventListener('click', function(){
        toDoContainer.removeChild(paragraph)
        toDoContainer.removeChild(completedBtn)
        toDoContainer.removeChild(deleteBtn)
    })
    deleteBtn.addEventListener('click', function(){
        doneListContainer.removeChild(paragraph)
        doneListContainer.removeChild(completedBtn)
        doneListContainer.removeChild(deleteBtn)
    })
})

