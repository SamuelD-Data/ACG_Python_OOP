# creating EssayQuestion class
# question_text is set as an attribute while answer
# and answer_is_sufficient are class variables set to none and False, respectively
class EssayQuestion:
  def __init__(self, question_text) -> None:
      self.question_text = question_text
      self.answer = None
      self.answer_is_sufficient = False

# str method is set to return question_text as a string      
  def __str__(self) -> str:
      return self.question_text

# returning answer as str
  def select(self, answer) -> None:
      self.answer = str(answer)

# printing question_text, 2 line breaks then answer
# sufficient class variable asks for input as to whether answer is sufficient as y or n
# sets sufficient class variable true if input value starts with a "y", otherwise false
# returns if answer is sufficient as True or False
  def grade(self) -> bool:
      print(f"{self.question_text}\n\nAnswer:\n{self.answer}\n")
      sufficient = input("Is this answer sufficient? [Yn]: ")
      sufficient = True if sufficient.lower().startswith("y") else False
      self.answer_is_sufficient = sufficient
      return self.answer_is_sufficient
