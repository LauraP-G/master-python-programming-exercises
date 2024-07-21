# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
  # Your code here
  decenas= number // 10
  unidades= number % 10
  return decenas, unidades
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
