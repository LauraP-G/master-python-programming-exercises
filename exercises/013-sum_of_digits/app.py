# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  aux=0
  for i in str(num):
    
    aux+=int(i)

  return aux
  # return sum(int(digit) for digit in str(abs(num)))


# Invoke the function with any three-digit number
print(digits_sum(123))
