from quiz import Quiz
from questions import Question, TrueFalseQuestion
from essay_question import EssayQuestion

question1 = Question("What's the answer to life, the universe, and everything?", [42, "Silver", "Wood", True], 42)
question2 = TrueFalseQuestion("Ice cream is the best dessert.", True)
question3 = EssayQuestion("How would you scale a web application?")
quiz = Quiz(questions=[question1, question2, question3], passing_percent=0.60)

if __name__ == "__main__":
    quiz.start()
    print("Grading\n")
    percent, passing = quiz.grade()
    print(f"Results:\n\nPass: {passing} (Score: {percent * 100}%)")