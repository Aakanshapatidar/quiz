questions = [
    {
        "question": "1. What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .py", "C. .pyt", "D. .p"],
        "answer": "B"
    },
    {
        "question": "2. Which of the following is used to take input from the user?",
        "options": ["A. scanf()", "B. gets()", "C. input()", "D. read()"],
        "answer": "C"
    },
    {
        "question": "3. What is the output of print(3 + 4 * 2)?",
        "options": ["A. 14", "B. 11", "C. 10", "D. 9"],
        "answer": "B"
    },
    {
        "question": "4. Which one is a mutable data type in Python?",
        "options": ["A. tuple", "B. string", "C. list", "D. int"],
        "answer": "C"
    },
    {
        "question": "5. What does == do in Python?",
        "options": ["A. Assigns value", "B. Compares values", "C. Divides", "D. Checks data type"],
        "answer": "B"
    },
    {
        "question": "6. What will len(\"Hello\") return?",
        "options": ["A. 6", "B. 5", "C. 4", "D. Error"],
        "answer": "B"
    }
]
score =0
print("\n🎯 Python Quiz: Select the correct option (A/B/C/D)\n")
for q in questions:
    print(q["question"])
    for o in q["options"]:
        print(o)
    user_answer=input("enter your answer:")
    if user_answer==q["answer"]:

        print("you are correct")
        print("you got 1 point")
        score+=1
    else:
        print("you are wrong")
        print("the correct answer is",q["answer"])
        continue
print("you got" , score , "out of" , len(questions))