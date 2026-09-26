print("==========================")
print("  password guessing game  ")
print("==========================")

print('HINT- password % 10 == 0')

password = 5550      #this is the password which user has  to crack

attempt = 1

success = False

while attempt <= 5:
  Guess = int(input("enter the password: "))
  if (Guess == password):
    print("password is correct")
    success = True
    break

  elif (Guess < 1000):
    print("enter a 4 digit number")

  elif (Guess >= 10000):
    print("enter a 4 digit number")

  elif (1000 <= Guess <= 1999):
    print("try a much higher number")

  elif (2000 <= Guess <= 3999):
    print("try higher, around 5000+")

  elif (4000 <= Guess <= 4999):
    print("try higher, around 5000+")

  elif (5000 <= Guess <= 5549):
    print("try a bit higher")
  
  elif (5551 <= Guess <= 5600):
    print("try a bit lower ")

  elif (5601 <= Guess <= 6000):
    print("try bit lower,under 5600")
    
  elif (6001 <= Guess <= 8000):
    print("try a much lower number")

  elif (8001 <= Guess <= 9999):
    print("try much lower") 

  print(f"Attempts left: {5 - attempt}") 
  attempt = attempt + 1
  
if (success == False):
  print("Game over! You have used all your attempts")

