import unittest

from lead import Lead


class TestLead(unittest.TestCase):
    def setUp(self) -> None:
        """
        Create 3 leads with known lead scores for making all comparisons
        """
        self.apple = Lead("Apple", 50000, 2e12, 8.0)  # lead_score => 0.05
        self.bobs = Lead("Bob's Burgers", 100, 1000000, 4.0)  # lead_score => 0.25
        self.small = Lead("Small Place", 4, 90, 9.0)  # lead_score => 0.25

    def test_initialization(self):
        lead = Lead("Apple", 50000, 2e12, 8.0)
        self.assertEqual(lead.name, "Apple")
        self.assertEqual(lead.staff_size, 50000)
        self.assertEqual(lead.estimated_revenue, 2e12)
        self.assertEqual(lead.effort_factor, 8.0)

    def test_lead_score(self):
        self.assertEqual(self.apple.lead_score(), 0.05)
        self.assertEqual(self.bobs.lead_score(), 0.25)
        self.assertEqual(self.small.lead_score(), 0.25)

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

    def test_sorting(self):
        leads = [self.small, self.apple, self.bobs]
        self.assertEqual(list(sorted(leads)), [self.apple, self.small, self.bobs])


if __name__ == "__main__":
    unittest.main()
