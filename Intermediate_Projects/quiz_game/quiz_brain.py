class QuizBrain:

    def __init__(self,quiz_list):
        self.quiz_list = quiz_list
        self.question_number = 0
        self.right_answer = 0

    def still_has_questions(self):
        return self.question_number < len(self.quiz_list)

    def next_question(self):
        question = self.quiz_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").capitalize()
        self.check_question(user_answer, question.answer)

    def check_question(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.right_answer += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong!")
        print(f"The correct answer was: {question_answer}\nYour current score is: {self.right_answer}/{self.question_number}")

