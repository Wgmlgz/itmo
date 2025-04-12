// Calculate the Nth Fibonacci number
let n = 8 // Calculate the 8th Fibonacci number (F(8))
let a = 0
let b = 1
let i = 2

console.log("Calculating Fibonacci number F(n) for n = " + n)

if (n == 0) {
  console.log("Result F(0): " + a)
} else {
  if (n == 1) {
    console.log("Result F(1): " + b)
  } else {
    while (i <= n) {
      let temp = b
      b = a + b
      a = temp
      i = i + 1
    }
    console.log("Result F(n):" + b) // Should output 21 for n=8
  }
}