class Factorial: 
  def __init__(self):
    self.factSeq = [0, 1]
    
  def __call__(self, n):
    if n < len(self.factSeq):
      return self.factSeq[n]
    else:
      num = n * self(n-1)
      return num

def OOP():
  num_input = int(input("Enter a number for factorial: "))
  factorial_of = Factorial()
  if num_input < 0:
      print("Sorry, factorial does not exist for negative numbers.")
  else:
      print("The factorial of", num_input, "is", factorial_of(num_input))