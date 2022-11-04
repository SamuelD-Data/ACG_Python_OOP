# importing math for digit length method
import math
 
# creating lead class
# class will have attributes prescribed in instructions (name, staff_size, etc.)
# ultimate goal of class is to calculate a score that reflects how valuable a sales lead is (lead score)
class Lead:
    def __init__(self, name, staff_size, estimated_revenue, effort_factor):
        self.name = name
        self.staff_size = staff_size
        self.estimated_revenue = estimated_revenue
        self.effort_factor = effort_factor

# setting instance methods for each comparison operator (==, !=, >, etc.)
# i.e., I'm overwriting the existing method functionality and substituting with my own
# e.g., instead of == comparing as normal, it will compare the lead score of each element that is passed to it
    def __eq__(self, other):
        return self.lead_score() == other.lead_score()

    def __ne__(self, other):
        return self.lead_score() != other.lead_score()

    def __lt__(self, other):
        return self.lead_score() < other.lead_score()

    def __le__(self, other):
        return self.lead_score() <= other.lead_score()

    def __gt__(self, other):
        return self.lead_score() > other.lead_score()

    def __ge__(self, other):
        return self.lead_score() >= other.lead_score()

# creating lead score method calculate lead score using formula given in tutorial
    def lead_score(self):
        return 1 / (self.staff_size / self.estimated_revenue * (10 ** (self.__digit_length(self.estimated_revenue)
                    - self.__digit_length(self.staff_size))) * self.effort_factor)
   
# rounds number down to nearest integer then converts to string
# returns the length of the string
    def __digit_length(self, num):
        return len(str(math.floor(num)))
