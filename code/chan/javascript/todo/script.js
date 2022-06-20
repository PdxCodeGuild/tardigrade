// Add list item
function newListItem() {
    const list = document.createElement("li");
    let inputValue = document.getElementById("myInput").value;
    const myUL = document.getElementById("myList");
    console.log(inputValue);
    list.appendChild(document.createTextNode(inputValue));
    myUL.appendChild(list);

    //create span and add it
    const span = document.createElement("span");
    const x = document.createTextNode("X");
    span.className = "close";
    span.appendChild(x);
    list.appendChild(span);

    // Add event lsitener to new list items when clicking add
    for (let i = 0; i < close.length; i++) {
        close[i].addEventListener("click", function () {
            this.parentElement.style.display = 'none';
        });
    }
}

// Add checked and strike through
let myUList = document.querySelector("ul");
myUList.addEventListener('click', function (myEvent) {
    if (myEvent.target.tagName === 'LI') {
        myEvent.target.classList.toggle('checked');
    }
}, false);

// Get all elements with class="close"
let close = document.getElementsByClassName("close");

// loop through all elements with class close and hide the parent when clicked
for (let i = 0; i < close.length; i++) {
    close[i].addEventListener("click", function () {
        this.parentElement.style.display = 'none';
    });
}

