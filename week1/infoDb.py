InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Soren",  
               "LastName": "Zhuang",  
               "DOB": "16 February 2005",  
               "Residence": "San Diego",  
               "Favorite_Colors":["Green","Black"]
              })  

InfoDb.append({  
               "FirstName": "Andrew",  
               "LastName": "Zhang",  
               "DOB": "26 June 2004",  
               "Residence": "Los Angeles",   
               "Favorite_Colors":["Red","Blue"] 
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite_Colors: ", end="")  # \t is a tab indent, end="" make sure no return occurs
  
    print(", ".join(InfoDb[n]["Favorite_Colors"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion

  # hack 2a: def for_loop()
# for loop iterates on length of InfoDb
def for_loop():
  for n in range(len(InfoDb)):
      print_data(n)

    
  # hack 2b: def while_loop(0)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDb):
      print_data(n)
      n += 1
  return

  # hack 2c : def recursive_loop(0)
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop(n + 1)
  return # exit condition

def InfoDb_loops():
  print()
  print("For loop:")
  for_loop()
  print("While loop:")
  while_loop(0)  # requires initial index to start while
  print("Recursive loop:")
  recursive_loop(0)  # requires initial index to start recursion
  
# Factorial of a number using recursion
def recur_factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    num = n * recur_factorial(n-1)
    return num

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def Factorial():
  num = int(input("Enter a number for factorial: "))
  # check if the number is negative
  if num < 0:
      print("Sorry, factorial does not exist for negative numbers.")
  else:
      print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

def fibonacci(n):  
  if n < 0:
    print("Please enter a positive integer")
  elif n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  elif n > 20:
    print("That's too many numbers, don't input over 20")
  else:  
    return(fibonacci(n-1) + fibonacci(n-2))  

def output_fibonacci():
  # take input from the user  
  nterms = int(input("How many terms would you like? "))  
  # check if the number of terms is valid  
  if nterms <= 0:  
     print("The Fibonacci sequence does not exist for negative numbers.")  
  else:  
     print("Your sequence:")
     for i in range(nterms):
         print(fibonacci(i), end=" ")
  print()