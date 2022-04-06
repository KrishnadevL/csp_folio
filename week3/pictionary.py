# Done by Krish 

# using this input to determine difficulty to level 
dif_lvl = int(input("""
1. Easy
2. Medium
3. Hard
Please choose a difficulty level: """))


easy = [
  "        .-===-.",
  "        | . . |",
  "        | .'. |",
  "       ()_____()",
  "       ||_____||",
  "        W     W"
]
easy_ans = "chair"

medium = [
"                           __ ",
"    ,                    ,/ e\--o ",
"""  ((                   (  | __/ """,
"     \\~----------------| \_;/ ",
"     (                      / " ,
"      /) ._______________.  ) ",
"     (( (               (( ( ",
"      \`-)               \.-) "  
]
med_ans = "dog"

hard = [
"      .--..--..--..--..--..--. ",
"    .' \  (`._   (_)     _   \ ",
"  .'    |  '._)         (_)  | ",
"  \ _.')\      .----..---.   / ",
"  |(_.'  |    /    .-\-.  \  | ",
"  \     0|    |   ( O| O) | o| ",
"   |  _  |  .--.____.'._.-.  | ",
"   \ (_) | o         -` .-`  | ",
"    |    \   |`-._ _ _ _ _\ / ",
"     \    |   |  `. |_||_|   | ",
"     | o  |    \_      \     |     -.   .-. ",
"    |.-.  \     `--..-'   O |     `.`-' .' ",
"  _.'  .' |     `-.-'      /-.__   ' .-' ",
".' `-.` '.|='=.='=.='=.='=|._/_ `-'.' ",
"`-._  `.  |________/\_____|    `-.' ",
"   .'   ).| '=' '='\/ '=' | ",
"   `._.`  '---------------' ",
"           //___\   //___\ ",
"             ||       || ",
"             ||_.-.   ||_.-. ",
"            (_.--__) (_.--__) "
]
hard_ans = "spongebob"

if dif_lvl == 1:
  picture = easy
  ans = easy_ans
elif dif_lvl == 2:
  picture = medium
  ans = med_ans
elif dif_lvl == 3:
  picture = hard
  ans = hard_ans
else:
  print("Invalid Input")
  
  
try:
  n=1
  win = 0
  
  while n < len(picture)+1:
    a = 0
    for i in range(0,n):
      print(picture[a])
      a += 1
    
    user_ans = input("What is the picture? ")

    
    if user_ans == ans:
      win = 1
      
      break
    else:
      print("incorrect, try again")
      n += 1
  
  if win == 1:
    print("You got it in "+str(n)+" tries!")
  else: 
    print("You didnt get it in time!")
except NameError:
  print("try again")