const userDistance = prompt("What is the distance?: ");
const userUnit = prompt("What is the unit of distance(ft/mi/m/km)?: ");
const unitToMeters = {
    ft : 0.3048,
    mi : 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254
  }
if (userUnit == "ft") {
    convertedDistance = userDistance * unitToMeters.ft;
} else if (userUnit == "mi") {
    convertedDistance = userDistance * unitToMeters.mi;
} else if (userUnit == "m")  {
    convertedDistance = userDistance * unitToMeters.m;
}  else if (userUnit == "km") {
    convertedDistance = userDistance * unitToMeters.km;
}  else if (userUnit == "yd") {
    convertedDistance = userDistance * unitToMeters.yd;
}  else if (userUnit == "in") {
    convertedDistance = userDistance * unitToMeters.in;
}

console.log(convertedDistance)
