import question_model
import data
import quiz_brain

questions_bank = []
for question in data.question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = question_model.Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = quiz_brain.QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(questions_bank)}")