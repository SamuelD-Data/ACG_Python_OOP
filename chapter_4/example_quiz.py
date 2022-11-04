from quiz import Quiz
from questions import Question, TrueFalseQuestion
from essay_question import EssayQuestion

# Passing values to the various question classes (Question, TFQuestion, EssayQuestion)
# Passing listed results of the 3 question class uses along with the percent that must 
# be matched or exceeded on average between the 3 quizzes to pass the quiz (60%)
question1 = Question("What's the answer to life, the universe, and everything?", [42, "Silver", "Wood", True], 42)
question2 = TrueFalseQuestion("Ice cream is the best dessert.", True)
question3 = EssayQuestion("How would you scale a web application?")
quiz = Quiz(questions=[question1, question2, question3], passing_percent=0.60)

# running code and printing results
if __name__ == "__main__":
    quiz.start()
    print("Grading\n")
    percent, passing = quiz.grade()
    print(f"Results:\n\nPass: {passing} (Score: {percent * 100}%)")
