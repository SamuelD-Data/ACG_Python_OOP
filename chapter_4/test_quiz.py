import unittest
import sys
import io

from unittest.mock import patch

from random import seed

from quiz import Quiz
from questions import Question, TrueFalseQuestion


# creating TestQuiz class
# setting questions using Question and T/FQuestion methods from questions.py file
# creating quiz by passing both questions and a passing_percent of 50% (i.e., must get 1 out
# of 2 questions correct to pass
class TestQuiz(unittest.TestCase):
    def setUp(self):
        seed(10000) # Don't change this
        self.question1 = Question("What's the answer to life, the universe, and everything?", [42, "Silver", "Wood", True], 42)
        self.question2 = TrueFalseQuestion("Ice cream is the best dessert.", True)
        self.quiz = Quiz(questions=[self.question1, self.question2], passing_percent=0.50)
        
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["True", "Silver"])
    def testStartPresentsQuestions(self, mock_stdout, mock_input):
        answer = "Silver"

        self.assertTrue(self.quiz.questions[0].selected_answer == None)
        self.quiz.start()

        sys.stdout.seek(0)
        written = sys.stdout.read()

        # Output debugging since stdout is mocked out
        # Uncomment these lines to see what is written
        # to the screen (besides what `input` prints)
        # with open("output.txt", "w") as f:
        #     f.write(written)
        
# confirming that double line breaks and list of choices are set correctly like in previous lab        
        self.assertTrue("""1. True/False: Ice cream is the best dessert.

1. True
2. False""" in written)

        self.assertTrue("""2. What's the answer to life, the universe, and everything?

1. 42
2. Silver
3. Wood
4. True""" in written)

# confirming if first item form self.quiz.questions is the same as value of answer class variable
        self.assertEqual(self.quiz.questions[0].selected_answer, answer)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["True", "42", "Wood", "True"])
    def testScore(self, mock_stdout, mock_input):
        # Answers will be set by mock of `input`
        self.quiz.start()
        self.assertEqual(self.quiz.score(), 2)

        # On the second run we'll select a wrong answer
        self.quiz.start()
        self.assertEqual(self.quiz.score(), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["True", "42", "Wood", "True", "Wrong", "Wrong"])
    def testGrade(self, mock_stdout, mock_input):
        # Answers will be set by mock of `input`
        self.quiz.start()
        percentage, passed = self.quiz.grade()
        self.assertEqual(percentage, 1.0)
        self.assertTrue(passed)

        # On the second run we'll select a wrong answer, matching passing score perfectly
        self.quiz.start()
        percentage, passed = self.quiz.grade()
        self.assertEqual(percentage, 0.5)
        self.assertTrue(passed)

        # Select no correct answers
        self.quiz.start()
        percentage, passed = self.quiz.grade()
        self.assertEqual(percentage, 0.0)
        self.assertFalse(passed)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["My answer is awesome", "True", "42", "n"])
    # @unittest.skip("Implementing EssayQuestion later")
    def testGradeWithEssayQuestion(self, mock_stdout, mock_input):
        from essay_question import EssayQuestion
        essay = EssayQuestion("How would you go about building a web application?")

        self.quiz.questions.append(essay)
        self.quiz.start()

        # Output debugging since stdout is mocked out
        # Uncomment these lines to see what is written
        # to the screen (besides what `input` prints)
        # sys.stdout.seek(0)
        # written = sys.stdout.read()
        # with open("output_with_essay.txt", "w") as f:
        #     f.write(written)

# testing that out from class essay (which is set to output from EssayQuestion and
# question above "How would you go about building.." is "My answer is awesome"
        self.assertEqual(essay.answer, "My answer is awesome")

# setting percentage and passed to output from self.quiz.grade()
# since self.quiz.grade() has 2 items outputted (percent and True or False depending on if percent is
# greater than or equal to passing percent (from quiz.py)
# testing if percentage is correct, i.e., percentage == .67 and that quiz is passed (since it should be)
# since in this case, percent should be greater than the passing_percent (e.g., .67 > 50)
        percentage, passed = self.quiz.grade()
        self.assertEqual(percentage, 0.67)
        self.assertTrue(passed)

if __name__ == "__main__":
    unittest.main()
