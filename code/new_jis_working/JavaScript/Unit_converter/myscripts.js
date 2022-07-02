//v1 <-------------------------------------------------------------------------
//1 ft = .3048 km
// const convertor = {
//     m: .3048

// }

// let ft = prompt('Input number of feet to convert')
// let convertedFeet = parseInt(ft) * convertor.km

// console.log(convertedFeet, "m is equal to", ft, "feet")


//v2 <--------------------------------------------------------------------------
// const convertor = {
//     ft: 0.3048,
//     mi: 1609.34,
//     m: 1,
//     km: 1000,

// }

// let unit = prompt('Input unit to convert to: ')
// let numberValue = prompt('Input distance: ')

// let convertedValue = parseInt(numberValue) * convertor[unit]

// console.log(numberValue +""+ unit + " is equal to " + convertedValue + " meters.")


//v3 <--------------------------------------------------------------------------
//1 yard is 0.9144 m
//1 inch is 0.0254 m

const convertor = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: .9144,
    in: .0254,

}

let unit = prompt('Input unit to convert to: ')
let numberValue = prompt('Input distance: ')

let convertedValue = parseInt(numberValue) * convertor[unit]

console.log(numberValue +" "+ unit + " is equal to " + convertedValue + " meters.")
