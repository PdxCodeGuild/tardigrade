// -----------------------------------------------------------------------------------
// VERSION 1
// -----------------------------------------------------------------------------------

// NOTE-TO-SELF(NTS): Three parentheses are needed to parseInt or parseString an input

// const feet = parseInt((prompt("What is the distance in feet? ")))
// const feetToMeters = (feet * 0.3048)
// document.write(feet + "ft is " + feetToMeters + "m(s).")

// -----------------------------------------------------------------------------------
// VERSION 2
// -----------------------------------------------------------------------------------

// const distance = prompt("What is the distance? ")
// const units = prompt("What are the units? ['ft', 'mi', 'm', 'km': ")

// const conversionLibrary = {
//     ft: 0.3048,
//     mi: 1609.34,
//     m: 1,
//     km: 1000,
// }

// finalCalculaton = (distance * conversionLibrary[units])
// document.write(distance + " " + units + " is " + finalCalculaton + " m(s).")

// -----------------------------------------------------------------------------------
// VERSION 3
// -----------------------------------------------------------------------------------

const distance = prompt("What is the distance? ")
const units = prompt("What are the units? ['ft', 'mi', 'm', 'km', 'yd, 'in': ")

const conversionLibrary = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254,
}

finalCalculaton = (distance * conversionLibrary[units])
document.write(distance + " " + units + " is " + finalCalculaton + " m(s).")
