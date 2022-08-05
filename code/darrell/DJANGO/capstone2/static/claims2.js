
// jshint esversion: 6 


const a = document.querySelector('a');
a.onclick = (e) => {
  e.preventDefault();
  console.log('clicked');
}



const claim_link = document.getElementsByClassName("nav-link");
const nav_submenu = document.getElementsByClassName("nav-submenu");
const tdDSLN = document.getElementById("dsln");


for (let i=0; i < claim_link.length; i++) {

    const claim = claim_link[i].parentElement;
  
    const nav_submenu = claim.nextElementSibling.classList.contains("nav-submenu");
    
    // console.log(tdDSLN[i]);
    // // if (tdDSLN[i] > 59) {
    // //     tdDSLN[i].style.backgroundColor = "#ff4364";
    // // } else {
    // //     tdDSLN[i].style.backgroundColor = "";
    // // }



    if (nav_submenu) {

        claim.classList.remove('nav-item');
        claim.classList.add('nav-item_has_email');

        claim_link[i].addEventListener("click", (e)=> {
        
           for (let j=0; j < nav_submenu.length; j++){

            //  nav_submenu[j] = e.target.parentElement.nextElementSibling;
                    if (nav_submenu[j].classList.contains("hide")){
                        nav_submenu[j].classList.remove('hide');
                        nav_submenu[j].classList.add('show');
                    } else {
                        nav_submenu[j].classList.remove('show');
                        nav_submenu[j].classList.add('hide');
                    }
            
            console.log(nav_submenu);
            }
        });
        
    } else {
        claim.classList.contains('nav-item');


    }

   

  
   

    

 
}       




    
















 
  

  
  
  

  

    
  
    








    