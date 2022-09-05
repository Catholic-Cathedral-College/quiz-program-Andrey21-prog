restart = 1


while restart == 1:
  
  
  
  i = 0
  
  print('WELCOME TO MY QUIZ ')
  
  
  user_name = input('What is your Name?')
  
  
  print ('\nHI THERE ' + user_name + '! LET\'S PLAY A GAME or you could say a QUIZ!\n')
  print ('So you basically you have a question in front of you.\n\nYou have options and you write if it is (a,b,c, or d) not (A, B, C, or D)')
  print ('and if you get it correct you get a point.\n\n if you get it incorrect you lose a point and remember this is case sensitive.\n')
  print ('Also if you start from level 1 you have a chance of attempting the BONUS QUESTION!\n')
  
  
  score = 0
  
  
  while i<1:
    ready = input("Are You Ready? Type 'yes' or 'no'\n")
    if ready == 'yes' or ready == 'Yes':
      print('let\'s go then\n')
      i = 1
    
  
  user_level_choice = input('What level do you like to start from, Easy or Hard. Type level 1 or level 2:\n')
  if user_level_choice == 'level 1': 
    
    print("Question 1: The number of players in a court from 1 team? \n")
    print("a: Players 12 ")
    print("b: Players 9  ")
    print("c: Players 5 ")
    print("d: Players 1 \n")
  
    
    response = input("What is your answer to this question?\n")
    if response == "a":
      print("Correct, knowledge always pays off")
      score += 2
    else:
      print("sorry incorrect, don't worry many questions left to go!, try again")
    score -= 1
    print("your score is {}\n".format(score))
  
    
  
    print("Question 2:The first African American to play NBA games was? \n")
    print("a:Boston Celtics ")
    print("b:Miami Heat ")
    print("c:Earl Lloyd ")
    print("d:Toronto Raptors \n")
  
   
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, next time")
    score -= 1
    print("your score is {}\n".format(score))
  
    
  
    print("Question 3:different variety of shots in basketball are what? \n")
    print("a: 15 feet")
    print("b: 10 feet")
    print("c: 13 feet")
    print("d: 12 feet\n")
  
   
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, good job")
      score += 2
    else:
      print("sorry incorrect")
    score -= 1
    print("your score is {}\n".format(score))
  
    
    print("Question 4: who is the most famous basketball league? \n")
    print("a: Stephen Curry ")
    print("b: Lemon ")
    print("c: Shaquille O'Neal")
    print("d: James Naismith \n")
  
    
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, for the loss of your points")
    score -= 1
    print("your score is {}\n".format(score))
  
  
   
  
    print("Question 5:In NBA season 2017 2018 who was the most valuable player \n")
    print("a: Steve Kerr")
    print("b: Magic Johnson")
    print("c:Chris Paul")
    print("d: Larry Bird\n")
  
   
    response = input("What is your answer to this question?\n")
    if response == "a" or response == "a":
      print("Correct, continue with the streak")
      score += 2
    else:
      print("sorry incorrect, don't get upset always can get free points for a next level")
    score -= 1
    print("your score is {}\n\n".format(score))
  
  
    level_2 = input("You have reached level 2, do you wish to continue or exit?\n")
    if level_2 == "continue" or level_2 == "yes":
      print ('have 2 free points for keeping up\n!')
      score += 2
      print ('your score is {}\n\n'.format(score))