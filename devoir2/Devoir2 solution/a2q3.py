import random

def performTest(operation): 
    counter = 0
    correctCounts = 0
    if operation == 0:
        print("Please give the answers to the following additions:")
        for counter in range(10): 
          num1 = random.randint(0,9)
          num2 = random.randint(0,9)  
          answer = int(input(str(num1) + " + " + str(num2) + " = "))
          sum = num1 + num2
          if sum == answer :
            correctCounts += 1
          else: 
            print("Incorrect – the answer is", sum)
    else:  
        print("Please give the answers to the following multiplications:")
        for counter in range(10):
          num1 = random.randint(0,9)
          num2 = random.randrange(0,9)
          answer = int(input(str(num1) + " * " + str(num2) + " = "))
          mult = num1 * num2
          if(mult == answer):
            correctCounts += 1
          else: 
            print("Incorrect – the answer is", mult)
    return correctCounts
    
correctCounts = 0
print("This software tests you with 10 questions …… ");
operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))
      
correctCounts = performTest(operation)
        
if correctCounts <= 6 :
  print("Please ask your teacher for help.")
else:
  print("Congratulations!")
