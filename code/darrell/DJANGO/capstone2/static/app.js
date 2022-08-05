// // let claimsTable = document.getElementById('claimsTable');


// // let LI = document.getElementsByTagName('li');
// // let TR = document.getElementsByTagName('tr');
// // let TD = document.getElementsByTagName('td');
// // let TB = document.getElementsByTagName('tbody');
// // let firstTB = document.getElementById('firstTbody');


// // Promise.all([
// // 	fetch('KishaCaseNotes.json'),
// // 	fetch('outlookexport.json')
// // ]).then(res => {
// // 	return Promise.all(res.map(response=> {
// // 		return response.json();
// // 	}));
// // }).then(data => {
// //   console.log(data)
// //   let kishaData = data[0]
// //   let outlookexportData = data[1]
  
// //    //code here
// //    for (let i=0; i < 100; i++ ) {
        

// //   // console.log(`i: ${i}`);

// //   const newTR = document.createElement('TR');
// //   claimNumber = "#" + kishaData[i]["Claim #"];

     
// //     let claimsContents = 
// //       `<a href=""><tr><td><button name="${claimNumber}" id="toggleBtn" class="toggleBtn">+</button></td>
// //           <td><b><a href="">${claimNumber}</a></b></td>
// //           <td>${kishaData[i]["Lit Dates"]}</td>
// //           <td>${kishaData[i]["Claimant"]}</td>
// //           <td>${kishaData[i]["Coverage Letter"]}</td>
// //           <td>${kishaData[i]["DC Assigned?"]}</td>
// //           <td>${kishaData[i]["Date Coverage Letter Sent"]}</td>
// //           <td id="DSLN">${kishaData[i]["Days Since Last Note"]}</td>
// //           <td>${kishaData[i]["Follow-Up Date"]}</td>
// //           <td>${kishaData[i]["In Suit?"]}</td>
// //           <td>${kishaData[i]["Insured/Involved Facility"]}</td>
// //           <td>${kishaData[i]["Insurer/Policy"]}</td>
// //           <td>${kishaData[i]["Last Note"]}</td>
// //           <td>${kishaData[i]["Settlement Value"]}</td>
// //           <td>${kishaData[i]["State"]}</td>
// //           <td>${kishaData[i]["Action Required"]}</td>
// //           <td>${kishaData[i]["Bulk Insured?"]}</td>
// //           <td>${kishaData[i]["Claim Type"]}</td>
// //           <td><a href="">Edit</a></td>
// //           <td><a href="">Delete</a></td>
// //           </tr></a>
          
// //           `;

// //           //claimsTable.innerHTML += claimsContents;  
// //           firstTB.innerHTML += claimsContents;  

// //           let DSLN = kishaData[i]["Days Since Last Note"];
// //           let tdDSLN = document.getElementById("DSLN");

// //           if (DSLN > 59) {
// //             tdDSLN.style.backgroundColor = "#ff4364";
// //           } else {
// //             tdDSLN.style.backgroundColor = "";
// //           }





// //           //EMAIL FUNCTION STARTS HERE  

// //       //let emailTB = document.getElementById('emailTB');
   

        
// //        newTB = document.createElement('TB');
         
// //       for (let j=0; j < 10; j++ ) {

// //         // // console.log(`j: ${j}`);
               
// //         //    const emailBody = String(outlookexportData[j]['Body']);
// //         //    const emailSubject = String(outlookexportData[j]['Subject']);
// //         //    const regex = /(#([0-9]{6,7})+(-G[A-Z])*)/;
// //         //    const match = regex.exec(emailBody);
          
           
// //         //    if (match) {
// //         //      claimNum = match[0];
// //         //     //  console.log(`match: ${match[0]}----------${emailSubject}`);
// //         //    } else {
// //         //       // console.log('no matching claimNum ' + match);
// //         //    }
     
// //         //    const splitBody = emailBody.split('\n');
// //         //    const joinBody = splitBody.join('\n');
          
// //            // emailContents = `<li><a href=""><div id="emailUL"><h2 id="claimNum">${claimNum}</h2><h3 id="Subject">${outlookexportData[j]['Subject']}</h3>
// //            // <h4 id="From">From: ${outlookexportData[j]['From: (Name)']}:  ${outlookexportData[j]['From: (Address)']}</h4><pre>Message: ${joinBody}</pre></div></a></li><hr/>`;

// //           //  emailContents = `<ul id="emailULList"><li><a href=""><div id="emailUL"><h2 id="claimNum">${claimNum}</h2><h3 id="Subject">${outlookexportData[j]['Subject']}</h3>
// //           //  <h4 id="From">From: ${outlookexportData[j]['From: (Name)']}: ${outlookexportData[j]['From: (Address)']}</h4></div></a></li></ul>`;

// //           // 
// //           // 


// //            emailContents = `<tr id="emailTR"><td id="emailTD" colspan="8"><a href=""><div id="emailDiv"><h2 id="claimNum">${claimNum}</h2><h3 id="Subject">${outlookexportData[j]['Subject']}</h3>
// //            <h4 id="From">From: ${outlookexportData[j]['From: (Name)']}: ${outlookexportData[j]['From: (Address)']}</h4></div></a></td></tr>`;

          
// //           newTB.innerHTML += emailContents;
// //           // firstTB.append(newTB);
// //           // newTB.classList.add("hide");


// //           //   const parentTable = document.getElementById("claimsTable");
// //           //   parentTable.addEventListener("click", (e)=>{

// //           //   if (e.target.tagName === 'BUTTON') {

// //             firstTB.append(newTB);

// //           //  if (claimNumber == claimNum) {
           
// //           //   newTB.classList.add("hide");
// //           //   // console.log("Matching email");
// //           //   // console.log(claimNumber, claimNum);
// //           //  } else {
// //           //   // console.log("no matching email");
// //           //   // console.log(claimNum, claimNumber);
            
// //           //  }
           

// //           // }

          

        
      

         
           
           
          
       
// //         }
     
// //      //EMAIL FUNCTION ENDS HERE  
        
      
// //     //   });

// //     // // });
     
    

        
      
// //   }


  
      


      






// //   console.log(kishaData, outlookexportData );

// // }).catch(function (error) {
// // 	console.log(error);
// // });




//   const parentTable = document.getElementById("claimsTable");
//   parentTable.addEventListener("click", (e)=>{

//     const emailRow = document.getElementById("emailTR");
//     emailRow.classList.add("hide");

//     if (e.target.tagName === 'BUTTON' ) {
//       let emailTB = e.target.parentElement.parentElement.nextElementSibling;
//       console.log("Congrats, we found matching email for this claim!");
//       // console.log(emailTB);
//     //   console.log(claimNumber, claimNum);
//       console.log(e.target.name);
      
        
      
     

//       if (emailTB.classList.contains("hide")){

//       emailTB.classList.remove('hide');
//       emailTB.classList.add('show');
//       } else {
//       emailTB.classList.remove('show');
//       emailTB.classList.add('hide');

//       }
         

//     } else {
//       alert("Sorry, there is no matching email for this claim");
//       // console.log(e.target, "look at me");
//     //   console.log(e.target.name);
//     //   console.log(claimNumber, claimNum);
//     }




//     // if (e.target !== e.currentTarget) {
//     //   let clickedItem = e.target.id;
//     //   console.log(e.target);
//     //   const emailBtns = document.querySelectorAll(".toggleBtn");


//     //   // emailBtns.addEventListener("click", ()=>{

//     //     
//     // // });


//     // }

//     // e.stopPropagation();


//   });





 



















  
   
    

    
    
    

    

      
    
      
      

// // });








      