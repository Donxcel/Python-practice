class Quizz:
    def __init__(self, input):
        self.question_number = 0
        self.question_list = input
        self.score = 0

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            print('well done you have completed the game')
            print(f'your  finale score is {self.score}/{self.question_number}')
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.test = current_question.answer.lower()
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number} difficulty: {current_question.difficulty}\n: {current_question.text}(true/False): ").lower()

    def check_answer(self, answer, current):
        answer = self.user_answer
        current = self.test
        if answer == current:
            print('you got it right')
            self.score += 1
            print(f'your score is {self.score}/{self.question_number}')
        else:
            print('you got it wrong  the answer is: ', current)
            print(f'your score is {self.score}/{self.question_number}')

