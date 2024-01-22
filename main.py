import art
print(art.logo)
import game_data
import random

def compare(choice,compare_a,compare_b):
  if compare_a['follower_count']>compare_b['follower_count']:
    return "A"
  else:
    return "B"


def game():
  win=False
  score=0
  compare_a=random.choice(game_data.data)
  compare_b=random.choice(game_data.data)
  
  
  while not win:
    compare_a=compare_b
    compare_b=random.choice(game_data.data)
    if compare_a==compare_b:
      compare_b=random.choice(game_data.data)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']},from {compare_a['country']}")

    print(art.vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']},from {compare_b['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice==compare(choice,compare_a,compare_b):
      score+=1
      print(f"You're right! Current score: {score}")
    else:
      win=True
      print(f"Sorry, that's wrong. Final score: {score}")

game()

   

