# importing tool specialized for running tests on code
import unittest

# importing lead from lead.py file 
from lead import Lead

# as noted in docstring, setUp creates 3 leads (apple, bob's burgers, small place) that will be used to test my code
class TestLead(unittest.TestCase):
    def setUp(self) -> None:
        """
        Create 3 leads with known lead scores for making all comparisons
        """
        self.apple = Lead("Apple", 50000, 2e12, 8.0)  # lead_score => 0.05
        self.bobs = Lead("Bob's Burgers", 100, 1000000, 4.0)  # lead_score => 0.25
        self.small = Lead("Small Place", 4, 90, 9.0)  # lead_score => 0.25

# running apple through lead method and checking that each value is properly assigned
# i.e., name = apple, staff_size = 50000, etc.
    def test_initialization(self):
        lead = Lead("Apple", 50000, 2e12, 8.0)
        self.assertEqual(lead.name, "Apple")
        self.assertEqual(lead.staff_size, 50000)
        self.assertEqual(lead.estimated_revenue, 2e12)
        self.assertEqual(lead.effort_factor, 8.0)

# testing that the lead score for each lead matches the 
# lead score that the provided formula should output
    def test_lead_score(self):
        self.assertEqual(self.apple.lead_score(), 0.05)
        self.assertEqual(self.bobs.lead_score(), 0.25)
        self.assertEqual(self.small.lead_score(), 0.25)

# these 6 methods test each of the comparison methods
# e.g., apple does not match bobs, etc.
    def test_ne_operator(self):
        self.assertTrue(self.apple != self.bobs)

    def test_eq_operator(self):
        self.assertTrue(self.small == self.bobs)

    def test_lt_operator(self):
        self.assertTrue(self.apple < self.bobs)

    def test_le_operator(self):
        self.assertTrue(self.apple <= self.bobs)
        self.assertTrue(self.small <= self.bobs)

    def test_gt_operator(self):
        self.assertTrue(self.bobs > self.apple)

    def test_ge_operator(self):
        self.assertTrue(self.bobs >= self.apple)
        self.assertTrue(self.bobs >= self.small)

# creating list of leads
# then testing if the sorted list remains in the correct order         
    def test_sorting(self):
        leads = [self.small, self.apple, self.bobs]
        self.assertEqual(list(sorted(leads)), [self.apple, self.small, self.bobs])


if __name__ == "__main__":
    unittest.main()
