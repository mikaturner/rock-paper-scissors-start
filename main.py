import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Rock, Paper, Scissors.  A Battle to the DEATH!!!\n")
your_choice = int(input("What Do You Choose? Type O for rock, 1 for paper, or 2 for scissors: "))

computer_choice = random.randint(0, 2)

rock_paper_scissors = [rock, paper, scissors]

# 0 = rock; 1 = paper; 2 = scissors
# Win conditions for computer vs player [0,2],[1,0],[2,1]

#tie
if computer_choice == your_choice:
  print(f"The computer chose {rock_paper_scissors[computer_choice]} and you chose {rock_paper_scissors[your_choice]} It's a tie")
#computer
elif (computer_choice == 0 and your_choice == 2) or (computer_choice == 1 and your_choice == 0) or (computer_choice == 2 and your_choice == 1):
  print(f"The computer chose {rock_paper_scissors[computer_choice]} and you chose {rock_paper_scissors[your_choice]} The computer wins")
# error
elif your_choice >=3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
#player
else:
  print(f"The computer chose {rock_paper_scissors[computer_choice]} and you chose {rock_paper_scissors[your_choice]} You Win")