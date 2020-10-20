print("Welcome to the USSR Knowledge tester")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the USSR?")
  print("   a) United Soviet Socialism Republics")
  print("   b) Union of Soviet Socialist Republic")
  print("   c) Union of Soviet Socialist Republics")
  print("   d) idk")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. It is Union of Soviet Socialist Republics"
    score -=1
  elif answer == "b":
    output = "Wrong. It is Union of Soviet Socialist Republics, note - republics, not republic"
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "It is Union of Soviet Socialist Republics"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What group led the revolution against the Tsar with Lenin from 1917-1923?")
  print("   a) the Bolsheviks")
  print("   b) the 'whites'")
  print("   c) the France's 3rd armored division")
  print("   d) the RAF")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. They were fighting against the Bolsheviks"
    score -=1
  elif answer == "c":
    output = "Wrong. That division was created in 1951 and ended in 1991"
    score -=1
    
  elif answer == "d":
    output = "Wrong. RAF is Royal Air Force, who didn't led the revolution"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who succeeded Lenin?")
  print("   a) Nicholas II")
  print("   b) Yuri Andropov")
  print("   c) Konstantin Chernenko")
  print("   d) Josef Stalin")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Nicholas II was the last Tsar"
    score -=1
  elif answer == "b":
    output = "Wrong. Yuri Andropov is the 5th dictator in USSR"
    score -=1
  elif answer == "c":
    output = "Wrong. Konstantin Chernenko is the 6th dictator in USSR"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz, hope you learnt something and had fun!")
  
