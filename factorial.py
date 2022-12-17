def factorial_of(num):
  factorial = 1
  for i in range(factorial, num+1):
    factorial *= i
  return factorial

print(factorial_of(5))
print(factorial_of(10))