from random import sample

# creating question class which will be inherited by other classes
# setting needed attributes (question_text, choices, etc.)
class Question:
    def __init__(self, question_text, choices, correct_choice) -> None:
        self.question_text = question_text
        self.choices = choices
        self.correct_choice = str(correct_choice)
        self.selected_answer = None

# customizing str dunder method
# adding 2 linebreaks to the question text
# iterating over solution choices and outputting each with a number assigned to them
# e.g., "1. silver", "2. wood", etc.
    def __str__(self) -> str:
        output = self.question_text + "\n\n"

        for index, choice in enumerate(sample(self.choices, len(self.choices))):
            output += f"{index + 1}. {choice}\n"

        return output

# setting selected_answer to the value of choice as a string 
    def select(self, choice) -> None:
        self.selected_answer = str(choice)

# comparing selected answer to the correct choice
# returning bool (True or False) based on comparison 
    def grade(self) -> bool:
        return self.correct_choice == self.selected_answer

# TrueFalseQuestion class inherits from question class
# updating question_text value to be output of passing question_text to __prefix.. method
# using super() to initialize the attributes from the parent class instead of having
# to run individual lines for each attribute (e.g., self.question_text = question_text
class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_choice) -> None:
        question_text = self.__prefix_if_necessary(question_text)
        super().__init__(question_text, [True, False], correct_choice)

# __prefix... method checks if the question text begins with "false" or "true"
# if so, it returns the question text, otherwise it returns the question text
# with "True/False:" preceding it
    def __prefix_if_necessary(self, question_text) -> str:
        if question_text.lower().startswith("false") or question_text.lower().startswith("true"):
            return question_text
        else:
            return f"True/False: {question_text}"

# MultipleSelectQuestion inherits from the Question class
# updating question_text attribute to be a combination of the question text and correct choices
# this is done by calling the add_suffix method we're also creating
# using super() to initialize the attributes from the parent class
# using __sorted... method which is also created below, to return the correct_choices as a list of strings
class MultipleSelectQuestion(Question):
    def __init__(self, question_text, choices, correct_choices) -> None:
        question_text = self.__add_suffix(question_text, correct_choices)
        super().__init__(question_text, self.__sorted_string_list(choices), correct_choices)
        self.correct_choice = self.__sorted_string_list(correct_choices)

    def __add_suffix(self, question_text, correct_choices):
        return f"{question_text} (select {len(correct_choices)})"

    def __sorted_string_list(self, list_of_items):
        return list(sorted(map(str, list_of_items)))

    def select(self, choices) -> None:
        self.selected_answer = self.__sorted_string_list(choices)
