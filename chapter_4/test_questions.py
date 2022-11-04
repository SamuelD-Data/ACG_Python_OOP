# IMPORTANT NOTE: this is a copy of the test_questions.py file
# from chapter #3

from random import seed

# importing the classes from the questions.py file
from questions import Question, TrueFalseQuestion, MultipleSelectQuestion

import unittest

# TestQuestion class sets question attribute to output of passing the values below ("Whats the answer...", [42, ...]"
# to Question class from questions.py
class TestQuestion(unittest.TestCase):
    def setUp(self):
        seed(1)
        self.question = Question("What's the answer to life, the universe, and everything?", [42, "Silver", "Wood", True], 42)

# testing if question attribute is correct after output from question class
# note the 2 line breaks and listed values as described in the str method comments in the questinos.py file
    def testStringOutput(self):
        self.assertEqual(str(self.question), """What's the answer to life, the universe, and everything?
1. Silver
2. Wood
3. 42
4. True
""")

# checking if selected answer is set correctly 
# and if incorrect answer "silver" will return False (i.e., answer is incorrect)        
    def testSelectionAndGrading(self):
        self.question.select("Silver")
        self.assertEqual(self.question.selected_answer, "Silver")
        self.assertFalse(self.question.grade())

# checking if selected answer is set correctly 
# and if correct answer 42 will return True (i.e., answer is correct)                
        self.question.select(42)
        self.assertEqual(self.question.selected_answer, "42")
        self.assertTrue(self.question.grade())

# passing "Ice cream is..." to the TrueFalseQuestion class
# so "Ice cream is..." is the T/F question and True is the correct answer
# i.e., ice cream is the best dessert is true
class TestTrueFalseQuestion(unittest.TestCase):
    def setUp(self):
        seed(10000) # This specific seed will shuffle with False being the first option
        self.question = TrueFalseQuestion("Ice cream is the best dessert.", True)

# covered in existing comments below but to reiterate
# testing testQuestionTextPrefixes class to confirm it will not change a T/F question if it 
# begins with True or False. It should only add "True" or "False" to the begining of the question
# if either of those words isn't already present
    def testQuestionTextPrefixes(self):
        # If either True or False starts the question text then leave as is.
        # Otherwise prefix the question text with 'True/False:'
        self.assertEqual(self.question.question_text, "True/False: Ice cream is the best dessert.")
        question2 = TrueFalseQuestion("False or True: Up is down.", False)
        self.assertEqual(question2.question_text, "False or True: Up is down.")
        question3 = TrueFalseQuestion("True or False: Down is down.", True)
        self.assertEqual(question3.question_text, "True or False: Down is down.")

# testing if True and False are the choices available to T/F questions        
    def testOptionsAreTrueAndFalse(self):
        self.assertEqual(self.question.choices, [True, False])

# testing if True and False questions are both being graded correctly        
    def testSelectionAndGrading(self):
        self.question.select(False)
        self.assertEqual(self.question.selected_answer, "False")
        self.assertFalse(self.question.grade())

        self.question.select(True)
        self.assertEqual(self.question.selected_answer, "True")
        self.assertTrue(self.question.grade())

# like before, testing string output to ensure 2 line breaks and question choices are being listed        
    def testStringOutput(self):
        self.assertEqual(str(self.question), """True/False: Ice cream is the best dessert.
1. False
2. True
""")

# passing new attribute values and question to MultipleSelectQuestion class        
class TestMultipleSelectQuestion(unittest.TestCase):
    def setUp(self):
        seed(1)
        self.question = MultipleSelectQuestion("Which of the following functions return a list?", ['str', 'print', 'random.sample', 'list'], ['list', 'random.sample'])

# as with the other question type classes, again testing whether the correct
# grade is being assigned
    def testSelectionAndGrading(self):
        self.question.select(['str', 'print'])
        self.assertEqual(self.question.selected_answer, ['print', 'str'])
        self.assertFalse(self.question.grade())

        # Ordering of selections shouldn't matter
        self.question.select(['random.sample', 'list'])
        self.assertEqual(self.question.selected_answer, ['list', 'random.sample'])
        self.assertTrue(self.question.grade())

        self.question.select(['list', 'random.sample'])
        self.assertEqual(self.question.selected_answer, ['list', 'random.sample'])
        self.assertTrue(self.question.grade())

# again, testing string output to ensure 2 line breaks and question choices are being listed          
    def testStringOutput(self):
        self.assertEqual(str(self.question), """Which of the following functions return a list? (select 2)
1. print
2. random.sample
3. list
4. str
""")
