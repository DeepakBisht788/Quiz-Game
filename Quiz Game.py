import random
k = [
{"text": "A slug's blood is green?", "answer": "True"},
{"text": "The loudest animal is the African Elephant?", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet?", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch?", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat?", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral?", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal?", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs?", "answer": "False"},
{"text": "Google was originally called 'Backrub'?", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'?", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times?", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog?", "answer": "True"}
]
score=0
chance=0
q=True
while k:
  d=random.choice(k)
  print("")
  x=input(f"Question :{d['text']} (True/False)").lower()
  if x==d['answer'].lower():
    print("you got it right!")
    print(f"The correct answer was:{d['answer']}")
    score+=1
    chance+=1
    print(f"Your current score is {score}/{chance}")
    k.remove(d)
  else:
    print("That's wrong.")
    print(f"The correct answer was:{d['answer']}")
    chance+=1
    print(f"Your current score is {score}/{chance}")
    k.remove(d)
    

  

