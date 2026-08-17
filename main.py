questions= [["who is salman khan?" , "fighter", "Actor", "drug dealer", "mafia", 2] ,
["how many wonders in the world?", "6", "9", "7", "10" , 3],
["who is the best player of cricket?", "virat kohli", "Sachin tendulkar", "MS dhoni", "AB Deviliers", 1],
["what is the capital of India?", "pune", "Mathura", "mumbai", "Delhi",4],
["which planet is known as red planet?", "mars", "Earth","Sun","Moon",1],
["what is the name of the fastest animal?","donkey", "elephant", "cheetah", "horse", 4],
["which ocean is the largest?","indian ocean", "pacific ocean","atlantic ocean", "arctic oocean", 2]
]
prizes=[50000, 100000 , 200000 , 350000, 500000, 750000, 1000000 ]
i=0
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

 #check whether the answer is true or not.

    a=int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5]==a):
        print("correct answer")
    else:
        print(f"wrong answer! the correct answer is {question[5]}")
        print("Better luck next time!!")  
        break   
    print(f"You won {prizes[i]}")
    i += 1