let claimsTable = document.getElementById('claimsTable');

let LI = document.getElementsByTagName('li');
let TR = document.getElementsByTagName('tr');
let TD = document.getElementsByTagName('td');

Promise.all([
	fetch('KishaCaseNotes.json'),
	fetch('outlookexport.json')
]).then(res => {
	return Promise.all(res.map(response=> {
		return response.json();
	}));
}).then(data => {
  console.log(data)
  const kishaData = data[0]
  const outlookexportData = data[1]
  
   //code here




  console.log(kishaData, outlookexportData )
}).catch(function (error) {
	console.log(error);
});


// console.log(kishaData)
// {
    
    
//     for (let i=0; i < 10; i++ ) {
        

//       console.log(`i: ${i}`);

//       const newTR = document.createElement('TR');
//       const claimNumber = "#" + data[i]["Claim #"];

       
//       let claimsContents = 
//         `<a href=""></a><tr>
//             <td><b><a href="">${claimNumber}</a></b></td>
//             <td>${data[i]["Lit Dates"]}</td>
//             <td>${data[i]["Claimant"]}</td>
//             <td>${data[i]["Coverage Letter"]}</td>
//             <td>${data[i]["DC Assigned?"]}</td>
//             <td>${data[i]["Date Coverage Letter Sent"]}</td>
//             <td>${data[i]["Days Since Last Note"]}</td>
//             <td>${data[i]["Follow-Up Date"]}</td>
//             <td>${data[i]["In Suit?"]}</td>
//             <td>${data[i]["Insured/Involved Facility"]}</td>
//             <td>${data[i]["Insurer/Policy"]}</td>
//             <td>${data[i]["Last Note"]}</td>
//             <td>${data[i]["Settlement Value"]}</td>
//             <td>${data[i]["State"]}</td>
//             <td>${data[i]["Action Required"]}</td>
//             <td>${data[i]["Bulk Insured?"]}</td>
//             <td>${data[i]["Claim Type"]}</td>
//             <td><a href="">Edit</a></td>
//             <td><a href="">Delete</a></td>
//             </tr></a>
//             <tbody id="emailTB">Tb</tbody>
//             `;

//             claimsTable.innerHTML += claimsContents;  

            
//             //EMAIL FUNCTION STARTS HERE  

//       //  let emailTB = document.getElementById('emailTB');
//        let emailTB = document.querySelector('tbody');

//        fetch("outlookexport.json")
//        .then(response => response.json())
//        .then(data2 => {
       
         
//         const newLI = document.createElement('LI');
           
//         for (let j=0; j < 10; j++ ) {

//           console.log(`j: ${j}`);
                 
//              const emailBody = String(data2[j]['Body']);
//              const regex = /(#[0-9]+(-G[A-Z])*)/;
//              const match = regex.exec(emailBody);
             
//              if (match) {
//                claimNum = match[0];
//                //  console.log(claimNum);
//              } else {
//                //  console.log('no match');
//              }
       
//              const splitBody = emailBody.split('\n');
//              const joinBody = splitBody.join('\n');
            
//              // emailContents = `<li><a href=""><div id="emailUL"><h2 id="claimNum">${claimNum}</h2><h3 id="Subject">${data2[j]['Subject']}</h3>
//              // <h4 id="From">From: ${data2[j]['From: (Name)']}:  ${data2[j]['From: (Address)']}</h4><pre>Message: ${joinBody}</pre></div></a></li><hr/>`;

             

//              emailContents = `<ul id="emailULList"><li><a href=""><div id="emailUL"><h2 id="claimNum">${claimNum}</h2><h3 id="Subject">${data2[j]['Subject']}</h3>
//              <h4 id="From">From: ${data2[j]['From: (Name)']}: ${data2[j]['From: (Address)']}</h4></div></a></li></ul>`;

            
//              // let emailULList = document.getElementById('emailULList');

//             //  while (claimNumber == claimNum) {
//              emailTB.innerHTML = "hello world";
//              // emailULList.innerHTML += emailContents;
//              // emailULList.appendChild(newLI);
//             //  }
         
//            }
       
//              console.log(data2);
        
//        }); 
//        //EMAIL FUNCTION ENDS HERE  


            

//             console.log(data);

         
                  
//           // claimsTable.appendChild(newTR);
        
//     }

    

      
    
      
      

// });








      