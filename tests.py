"""Unit tests to test functionality of project.
"""

import unittest

import module1

class TestPAProject(unittest.TestCase):

    def test_gpa_gap(self):
        self.assertEqual(module1.gpa_gap(3.0, 3.2), 0.2)

    def test_science_gpa_gap(self):
        self.assertEqual(module1.science_gpa_gap(2.8, 3.0), 0.2)

    def test_pce_gap(self):
        self.assertEqual(module1.pce_gap(500, 1000), 500)

    def test_compare_schools(self):
        schools = [
            {
                "School": "Example PA Program",
                "Min_GPA": 3.2,
                "Min_Science_GPA": 3.0,
                "Required_PCE_hours": 1000

            }
        ]

        result = module1.compare_schools(3.0, 2.8, 500, schools)

        self.assertEqual(len(result),1)
        self.assertEqual(result[0]["School"], "Example PA Program")
        self.assertEqual(result[0]["PCE Hours Gap"], 500)            

if __name__ == "__main__":
    unittest.main()
    
        

                 
    