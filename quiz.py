#!/usr/bin/env python
# coding: utf-8

# In[ ]:


quiz = {
    1 : {
        "question" : "What is the first name of Iron Man?",
        "answer" : "Tony"
    },
    2 : {
        "question" : "Who is called the god of lightning in Avengers?",
        "answer" : "Thor"
    },
    3 : {
        "question" : "Who carries a shield of American flag theme in Avengers?",
        "answer" : "Captain America"
    },
    4 : {
        "question" : "Which avenger is green in color?",
        "answer" : "Hulk"
    },
    5 : {
        "question" : "Which avenger can change it's size?",
        "answer" : "AntMan"
    },
    6 : {
        "question" : "Which Avenger is red in color and has mind stone?",
        "answer" : "Vision"
    }
}
def check_ans(question, ans, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer \nTry again...")
        return False
    
def intro_message():
    print("Welcome to this fun food quiz! \nAre you ready to test your knowledge about food?")
    print("There are a total of 20 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to start the fun ;) ")
    return True

def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key , ':', ques_answer[key])



intro = intro_message()
while True:
    score = 0
    for question in quiz:
        print(quiz[question]['question'])
        answer = input("Enter Answer (To move to the next question, type 'skip') : ")
        if answer == "skip":
            break
        check = check_ans(question, answer, score)
        if check:
            score += 1
          
           
    break

