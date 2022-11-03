import math
 
class Lead:
    def __init__(self, name, staff_size, estimated_revenue, effort_factor):
        self.name = name
        self.staff_size = staff_size
        self.estimated_revenue = estimated_revenue
        self.effort_factor = effort_factor

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

# 1 / (staff_size / estimated_revenue * (10 ** (digits_in_revenue - digits_in_staff_size)) * effort_factor)
    def lead_score(self):
        return 1 / (
            self.staff_size
            / self.estimated_revenue
            * (
                10
                ** (
                    self.__digit_length(self.estimated_revenue)
                    - self.__digit_length(self.staff_size)
                )
            )
            * self.effort_factor
        )

    def __digit_length(self, num):
        return len(str(math.floor(num)))