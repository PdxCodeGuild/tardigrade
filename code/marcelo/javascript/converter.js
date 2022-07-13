const dict = {
    ft: .3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254,
}

let distance = prompt("What is the distance?");
let unit = prompt("What are the units? (ft, mi, m, km, yd, in)");
let units = dict[unit];
console.log(distance + unit + ' ' + 'is' + ' ' + units * distance + 'm')
