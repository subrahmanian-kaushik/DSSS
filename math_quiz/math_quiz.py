import random


def number(min, max): #Selecting a random number using random lib for math quiz
 return random.randint(min, max)  #retruning a random integer for quiz


def math_operator():#Selecting a random math operator using random lib for math quiz
    return random.choice(['+', '-', '*']) #returning a random maths function for quiz


def problem_answer(n1, n2, o): 
    problem = f"{n1} {o} {n2}"
    if o == '+': # Addition
        answer = n1 + n2
    elif o == '-': #Subtraction
     answer = n1 - n2
    else: #Multiplication
        answer = n1 * n2
    return problem, answer # return the correct answer

def math_quiz():
    points = 0
    total=5 #total question
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total): #run loop for total questions
        num1 = number(1, 10) #Function to select a random number for maths quiz
        num2 = number(1, 20)#Function to select a random number for maths quiz
        question = math_operator()#Function to select a random math operator for maths quiz

        PROBLEM, ANSWER = problem_answer(num1, num2, question) #calls function C to get the problem and correct answer
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input!! Please enter a number!!")
            continue


        if useranswer == ANSWER: # checks whether the answer is correct or wrong
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{total}")# print the points of user

if __name__ == "__main__":
    math_quiz()
