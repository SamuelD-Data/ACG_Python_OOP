class EssayQuestion:
  def __init__(self, question_text) -> None:
      self.question_text = question_text
      self.answer = None
      self.answer_is_sufficient = False

  def __str__(self) -> str:
      return self.question_text

  def select(self, answer) -> None:
      self.answer = str(answer)

  def grade(self) -> bool:
      print(f"{self.question_text}\n\nAnswer:\n{self.answer}\n")
      sufficient = input("Is this answer sufficient? [Yn]: ")
      sufficient = True if sufficient.lower().startswith("y") else False
      self.answer_is_sufficient = sufficient
      return self.answer_is_sufficient
