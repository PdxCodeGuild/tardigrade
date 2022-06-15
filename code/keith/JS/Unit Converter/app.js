 
 
 
 
 
 
 
 
 
 
 
 const units = {
    feet: 0.3048,
    miles: 1609.34,
    meters: 1,
    kilometers: 1000, 
    inches: .0254,
    yards: .9144
}



let user_input1 = prompt('Enter a unit of measurement: feet, miles, meters, kilometers, inches, yards:   ');
let user_input2 = prompt('Enter a number to be converted: ');
let user_input3 = prompt('Enter a unit of measurment to convert too: ')



 const result = parseInt(user_input2) * units[user_input1]

 console.log(result)
 alert(result)