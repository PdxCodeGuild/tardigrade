
// Need to figure out how to deal with negative number that go past a 



function rotX(){
    let roationNumber = prompt('Input unit to convert to: ')
    let deCodeMessage = prompt('Enter the message that you would like encrypted?: ')
    let returnOutPut = []
    let alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let upperAlpha = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    if(roationNumber < 26){
        roationNumber = roationNumber/1
    } else{
        roationNumber = roationNumber % 26
    }

    while(returnOutPut.length < deCodeMessage.length){
        for (let x of deCodeMessage){
            if(alphabet.indexOf(x) !== -1){  
                let indexA = alphabet.indexOf(x)+roationNumber
                if(indexA < 26){
                    indexA = indexA
                    } else{
                        indexA = indexA % 26
                        }
                returnOutPut.push(alphabet[(indexA)])
            }else if(upperAlpha.indexOf(x) !== -1){
              let indexA = upperAlpha.indexOf(x)+roationNumber
              if(indexA < 26){
                indexA = indexA
                } else{
                    indexA = indexA % 26
                    }
              returnOutPut.push(upperAlpha[(indexA)])
              }else{
                returnOutPut.push(x)
                }
              
        }

    } 
    return returnOutPut
    
}
console.log(rotX())




