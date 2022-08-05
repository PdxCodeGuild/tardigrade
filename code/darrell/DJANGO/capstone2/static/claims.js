
// jshint esversion: 6 

// const claim = document.getElementsByClassName("nav-link");
//     claim.addEventListener("click", function (e) {
//         // let emailDiv = e.target.parentElement.parentElement.nextElementSibling;
//         e.target.style.backgroundColor = "red";
//          console.log("clicked");

//         });




        // console.log(e.target.name);
        // if (emailDiv.classList.contains("hide")){

        //         emailDiv.classList.remove('hide');
        //         emailDiv.classList.add('show');
        //     } else {
        //         emailDiv.classList.remove('show');
        //         emailDiv.classList.add('hide');
        //     }


alert("I am an alert box!");


const claim = document.getElementsByClassName("nav-link");

for (let i=0; i < claim.length; i++) {
    claim[i].addEventListener("click", (e)=> {
        // document.getElementById("demo").innerHTML = "Hello World";
        let nav_submenu = document.getElementsByClassName("nav-submenu");
         nav_submenu = e.target.parentElement.nextElementSibling;
                if (nav_submenu.classList.contains("hide")){
                    nav_submenu.classList.remove('hide');
                    nav_submenu.classList.add('show');
                } else {
                    nav_submenu.classList.remove('show');
                    nav_submenu.classList.add('hide');
                }
        
        console.log(nav_submenu);
    });

}

    





   // claim_link[i].addEventListener("click", (e)=> {
    
    // const nav_submenu2 = e.target.parentElement.nextElementSibling.classList.contains("nav-submenu");
    // console.log(nav_submenu2);

    //     if (nav_submenu2) {

        
    //         if (nav_submenu2.classList.contains('hide')){
    //         nav_submenu2.classList.remove('hide');
    //         nav_submenu2.classList.add('show');
    //         } else {
    //         nav_submenu2.classList.remove('show');
    //         nav_submenu2.classList.add('hide');
    //         }


    //     } else {

    //         alert("Sorry, this claim has no matching email.");

    //     }

    // });






    let DSLN = kishaData[i]["Days Since Last Note"];
    let tdDSLN = document.getElementById("DSLN");

    if (DSLN > 59) {
      tdDSLN.style.backgroundColor = "#ff4364";
    } else {
      tdDSLN.style.backgroundColor = "";
    }









 
  

  
  
  

  

    
  
    








    