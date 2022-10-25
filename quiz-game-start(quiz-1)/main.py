from question_model import *
from data import *
from quiz_brain import Quizz

question_bank = []
for test in question_data:

    question_text = test["question"]
    question_answer = test['correct_answer']
    dif = test['difficulty']
    new_question = Question(question_text, question_answer,difficulty=dif)
    question_bank.append(new_question)
a = ''
b = ''
quiz = Quizz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer(a,b)