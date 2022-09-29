restart = 1


while restart == 1:
  
 
  # this is the while loop for the question asking the player if they are ready?
  i = 0
  # this is code below prints the introduction/title of the quiz/game
  print('Welcome your in Andrey\'s quiz game.')
 
  # input code for the user's name
  user_name = input('What is your Name?')
 
  # code that prints instructions for completing the quiz
  print ('\nHi There ' + user_name + '! Lets\'s play a Question and Answer game or you could say a QUIZ!\n')
  print ('So you basically you have a question in front of you.\n\nYou have options and you write if it is (a,b,c, or d) not (A, B, C, or D)')

 
 
  # score initialization
  score = 0
 
  # asking the player if he/she is prepared to answer the questions
  while i<1:
    ready = input("Are You Ready? Type 'yes' or 'no'\n")
    if ready == 'yes' or ready == 'Yes':
      print('let\'s go then\n')
      i = 1
   
  # player's choice for difficulty
  user_level_choice = input('So lets start from level 1. Type level 1:\n')
  if user_level_choice == 'level 1':
    # Start of question 1
    print("Question 1: The number of players in a court from 1 team??\n")
    print("a: Players 12")
    print("b: Players 9")
    print("c: Players 5")
    print("d: Players 1")
 
    # Code defining whether player's input is right or wrong for question 1 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, knowledge always pays off")
      score += 2
    else:
      print("sorry incorrect, don't worry many questions left to go!, try again")
    score -= 1
    print("your score is {}\n".format(score))
 
    # Start of question 2
 
    print("Question 2: The first African American to play NBA games was?\n")
    print("a: Boston Celtics")
    print("b: Miami Heat")
    print("c: Earl Lloyd")
    print("d: Toronto Raptors")
 
    # Code defining whether player's input is right or wrong for question 2 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, next time")
    score -= 1
    print("your score is {}\n".format(score))
 
    # Start of question 3
 
    print("Question 3: different variety of shots in basketball are what?\n")
    print("a: 15 feet")
    print("b: 10 feet")
    print("c: 13 feet")
    print("d: 12 feet")
 
    # Code defining whether player's input is right or wrong for question 3 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "d":
      print("Correct, good job")
      score += 2
    else:
      print("sorry incorrect")
    score -= 1
    print("your score is {}\n".format(score))
 
    # Start of question 4`
 
    print("Question 4: who is the most famous basketball league")
    print("a: Stephen Curry")
    print("b: Lemon ")
    print("c: Shaquille O'Neal")
    print("d: James Naismith")
 
    # Code defining whether player's input is right or wrong for question 4 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, for the loss of your points")
    score -= 1
    print("your score is {}\n".format(score))
 
 
    # Start of question 5
    
 
    print("Question 5: In NBA season 2017 2018 who was the most valuable player \n")
    print("a: Steve Kerr")
    print("b: Magic Johnson")
    print("c: Chris Paul")
    print("d: Larry Bird")

 # Code defining whether player's input is right or wrong for question 4 and if right he gets a point else loses 1 point
    
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, for the loss of your points")
    score -= 1
    print("CONGRATULATIONS YOUR SCORE IS {}\n".format(score)) 
    level_2 = input("You have reached level 2, do you wish to continue or exit?\n")
    if level_2 == "continue" or level_2 == "yes":
      print ('have 2 free points for keeping up\n!')
      score += 2
      print ('your score is {}\n\n'.format(score))  

 
    level_2 = input("You have reached level 2, do you wish to continue or exit?\n")
    if level_2 == "continue" or level_2 == "yes":
      print ('have 2 free points for keeping up\n!')
      score += 2
      print ('your score is {}\n\n'.format(score))  

 
      print("Question 6: When was basketball made?\n")
      print("a: 1737")
      print("b: 1891 ")
 
      response = input("What is your answer to this question?\n")
      if response == "b":
        print("Correct, way to go")
        score += 2
      else:
        print("sorry, not bad")
      score -= 1
      print("your score is {}\n".format(score))
 
 
 
      print("Question 7:Who made basketball?\n")
      print("a: James Naismith")
      print("b: William Morgan")
      print("c: Jim Thorpe")
 
      response = input("What is your answer to this question?\n")
      if response == "a":
        print("Correct, nice job here have a point")
        score += 2
      else:
        print("sorry, next time")
      score -= 1
      print("your score is {}\n".format(score))
 
 
      print("Question 8:What is a turnover?\n")
      print("a:  When the two teams switch.")
      print("b:  The different ways that possession of the ball goes from one team to another..")
      print("c:  A player is transferred to the other team during a game.")
   
     
      response = input("What is your answer to this question?")
      if response == "b":
        print("Correct, don't stop!")
        score += 2
      else:
        print("sorry, but next time")
      score -= 1
      print("your score is {}\n".format(score))
 
      print("Question 9: What does BEEF mean?\n")
      print("a: Balance, Eyes, Elbow, Follow Through")
      print("b: Basketball, Elbow, Endline, Free-Throw")
      print("c: Box and One, Euro Step, Elevator Screen, Field Goal")
     
 
      response = input("What is your answer to this question?\n")
      if response == "a" or response == "b":
        print("Correct, nice job here have a point")
        score += 2
      else:
        print("sorry, next time")
      score -= 1
      print("your score is {}\n".format(score))
 
 
      print("Question 10: The main responsibility of the center player is to…\n")
      print("a: make baskets")
      print("b: steal the ball and block attacks")
      print("c: secure rebounds and defend the paint")
      print("d: Tennis")
 
      response = input("What is your answer to this question?\n")
      if response == "c":
        print("Correct, nice job here have a point\n\n")
        score += 2
      else:
        print("sorry, next time\n")
      score -= 1
      print('your score is {}'.format(score))
     
      if score>8:
        print('Wow amazing performance try this bonus question!\n\n')
 
      if score>8 :
        print('Bonus Question: MVP of 2018 NBA final was\n')
        print('a: Cleveland Cavalier')
        print("b: Papatoetoe High School")
        print("c: PHS")
        print("d: None of the above\n")

 
      if score>8 :
        response = input("What is your answer to this question?\n")
      if response == "c":
        print("Out-standing performance keep it up!\n")
        score += 2
      else:
        print("No worries no one's perfect but we can be perfect\n")
      score -= 1
      print("your Final score is {}!\n\n".format(score))
       
      print("THANKS FOR PLAYING!")
 
      PLAYERS_FEEDBACK = input(" Please rate this quiz out of ten and tell us what we could improve on \n")
 
      play_again = input("Do you want to restart? Yes or No\n")
 
      if play_again == "Yes" or play_again == "yes":
          exec(open("./Python quiz by Tanish.py").read())
      else:
          exit()
 
 
      print("Great choice\n\n")
    else:
      quit()

