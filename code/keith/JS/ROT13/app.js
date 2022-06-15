

function ROT13(str){
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     
    let cyphString = '';

    for (let i = 0; i < str.length; i++){
       let index = alphabet.indexOf(str[i]);
       
       if (index == -1){
           cyphString += str[i];
       } else {
           let newChar =  (index + 13) %  26;
           cyphString += alphabet[newChar]
       }




    } 


    return cyphString; 

}



console.log(ROT13('NGGNPX NG QNJA'));