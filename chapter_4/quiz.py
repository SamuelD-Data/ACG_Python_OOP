from random import sample

class Quiz:
  def __init__(self, questions, passing_percent):
      self.questions = questions
      self.passing_percent = passing_percent
      self.actual_score = 0

  def start(self):
    for index, question in enumerate(list(sample(self.questions, len(self.questions)))):
        print(f"{index + 1}. {question}")
        answer = input("Answer: ")
        question.select(answer)
        print("\n\n")

  def score(self):
    self.actual_score = 0
    for question in self.questions:
        if question.grade():
            self.actual_score += 1

    return self.actual_score

  def grade(self):
    self.score()
    percent = round(self.actual_score / len(self.questions), 2)
    return (percent, percent >= self.passing_percent)