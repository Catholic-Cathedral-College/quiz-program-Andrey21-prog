restart = 1


while restart == 1:
  
  i = 0
  print('WELCOME TO THE NOT GREATEST QUIZ GAME BY ME')
  
  user_name = input('What is your User Name?')
  
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

  
      print("Question 6: When was basketball made?\n")
      print("a:1737 ")
      print("b: 1891 ")
  
      response = input("What is your answer to this question?\n")
      if response == "b":
        print("Correct, way to go")
        score += 2
      else:
        print("sorry, not bad")
      score -= 1
      print("your score is {}\n".format(score))
  
  
  
      print("Question 7: 4. Who made basketball?\n")
      print("a: James Naismith ")
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
  
  
      print("Question 8: What is a turnover?\n")
      print("a:When the two teams switch.")
      print("b:  The different ways that possession of the ball goes from one team to another.")
      print("c:A player is transferred to the other team during a game.")
    
      
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
  
  
      print("Question 10: The main responsibility of the “center” player is to…\n")
      print("a: make baskets ")
      print("b: steal the ball and block attacks")
      print("c: Tennis")
      print("d:  secure rebounds and defend the paint")
  
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
        print('Bonus Question: MVP of 2018 NBA final was?')
        print('a: Cleveland Cavaliers')
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
  
      
  else:
    print("Question 6: It takes 16 seconds for the chug jug in Fortnite Battle royale?\n")
    print("a: True ")
    print("b: False ")
  
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, way to go")
      score += 2
    else:
      print("sorry, not bad")
    score -= 1
    print("your score is {}\n".format(score))
  
  
  
    print("Question 7: Which planet did Superman come from?\n")
    print("a: Krypton ")
    print("b: Kripton")
    print("c: crypton")
  
    response = input("What is your answer to this question?\n")
    if response == "a":
      print("Correct, nice job here have a point")
      score += 2
    else:
      print("sorry, next time")
    score -= 1
    print("your score is {}\n".format(score))
  
  
    print("Question 8: In a standard pack of cards, which king is the only one to not have a moustache?\n")
    print("a: king of heart")
    print("b: knig of spades")
    print("c: king of clubs")
    print("d: queen of heart")
      
    response = input("What is your answer to this question?\n") 
    if response == "a":
      print("Correct, don't stop!")
      score += 2
    else:
      print("sorry, but next time")
      score -= 1
    print("your score is {}\n".format(score))
  
  
    print("Question 9: What is the standard unit of distance in the metric system?\n")
    print("a: meter ")
    print("b: kilometer")
    print("c: miles")
    print("d: grams")
  
    response = input("What is your answer to this question?\n")
    if response == "a" or response == "b":
      print("Correct, nice job here have a point")
      score += 2
    else:
      print("sorry, next time")
    score -= 1
    print("your score is {}\n".format(score))
  
  
    print("Question 10: What game features the terms love, deuce, match and volley?\n")
    print("a: Soccer ")
    print("b: basketball")
    print("c: Tennis")
    print("d: badminton-maybe this one")
  
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, nice job here have a point")
      score += 2
    else:
      print("sorry, next time\n")
    score -= 1
  
    print("your Final score is {}!\n\n".format(score))
      
    print("THANKS FOR PLAYING!")
  
    PLAYERS_FEEDBACK = input(" Please rate this quiz out of ten and tell us what we could improve on \n")
  
    play_again = input("Do you want to restart/play again? Yes or No\n")
  
    if play_again == "Yes" or play_again == "yes":
        restart = 1 
    else:
        restart = 0
        exit()
  






