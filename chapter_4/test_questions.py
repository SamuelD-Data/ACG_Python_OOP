from random import seed

from questions import Question, TrueFalseQuestion, MultipleSelectQuestion

import unittest

class TestQuestion(unittest.TestCase):
    def setUp(self):
        seed(1)
        self.question = Question("What's the answer to life, the universe, and everything?", [42, "Silver", "Wood", True], 42)

    def testStringOutput(self):
        self.assertEqual(str(self.question), """What's the answer to life, the universe, and everything?

1. Silver
2. Wood
3. 42
4. True
""")

    def testSelectionAndGrading(self):
        self.question.select("Silver")
        self.assertEqual(self.question.selected_answer, "Silver")
        self.assertFalse(self.question.grade())

        self.question.select(42)
        self.assertEqual(self.question.selected_answer, "42")
        self.assertTrue(self.question.grade())

class TestTrueFalseQuestion(unittest.TestCase):
    def setUp(self):
        seed(10000) # This specific seed will shuffle with False being the first option
        self.question = TrueFalseQuestion("Ice cream is the best dessert.", True)

    def testQuestionTextPrefixes(self):
        # If either True or False starts the question text then leave as is.
        # Otherwise prefix the question text with 'True/False:'
        self.assertEqual(self.question.question_text, "True/False: Ice cream is the best dessert.")
        question2 = TrueFalseQuestion("False or True: Up is down.", False)
        self.assertEqual(question2.question_text, "False or True: Up is down.")
        question3 = TrueFalseQuestion("True or False: Down is down.", True)
        self.assertEqual(question3.question_text, "True or False: Down is down.")

    def testOptionsAreTrueAndFalse(self):
        self.assertEqual(self.question.choices, [True, False])

    def testSelectionAndGrading(self):
        self.question.select(False)
        self.assertEqual(self.question.selected_answer, "False")
        self.assertFalse(self.question.grade())

        self.question.select(True)
        self.assertEqual(self.question.selected_answer, "True")
        self.assertTrue(self.question.grade())

    def testStringOutput(self):
        self.assertEqual(str(self.question), """True/False: Ice cream is the best dessert.

1. False
2. True
""")

class TestMultipleSelectQuestion(unittest.TestCase):
    def setUp(self):
        seed(1)
        self.question = MultipleSelectQuestion("Which of the following functions return a list?", ['str', 'print', 'random.sample', 'list'], ['list', 'random.sample'])

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

    def testStringOutput(self):
        self.assertEqual(str(self.question), """Which of the following functions return a list? (select 2)

1. print
2. random.sample
3. list
4. str
""")