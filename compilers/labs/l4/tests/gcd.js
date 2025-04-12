// Calculate GCD using the subtraction-based Euclidean algorithm
let num1 = 54
let num2 = 24

console.log("Calculating GCD of: " + num1 + " and " + num2)

let a = num1
let b = num2

while (a != b) {
  if (a > b) {
    a = a - b
  } else {
    b = b - a
  }
}
// When they are equal, that's the GCD

console.log("GCD is: " + a)
