from random import sample

# creating quiz class which holds questions, passing_percent as attributes
# while actual_score is a class variable since it's not being passed with the attributes question and passing_percent
class Quiz:
  def __init__(self, questions, passing_percent):
      self.questions = questions
      self.passing_percent = passing_percent
      self.actual_score = 0

# enumerating each question and adding two line breaks to the end of the ouput
  def start(self):
    for index, question in enumerate(list(sample(self.questions, len(self.questions)))):
        print(f"{index + 1}. {question}")
        answer = input("Answer: ")
        question.select(answer)
        print("\n\n")

# creating score method
# actual_score starts at 0 and increments by 1 every time a value of 
# True is returned by the grade method otherwise it will not increment
  def score(self):
    self.actual_score = 0
    for question in self.questions:
        if question.grade():
            self.actual_score += 1

    return self.actual_score

# calculating score by dividing actual_score by the number of questions
# rounding the grade and returning True or False so that it can be used 
# in the score method above. i.e., if 
  def grade(self):
    self.score()
    percent = round(self.actual_score / len(self.questions), 2)
    return (percent, percent >= self.passing_percent)
