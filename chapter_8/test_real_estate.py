import unittest
import sys
import io

from copy import deepcopy
from json import load
from datetime import date, timedelta
from unittest.mock import patch

from real_estate import template, main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = None

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch(
        "builtins.input",
        side_effect=[
            "1600 Pennsylvania Ave NW",
            "",
            "Washington",
            "DC",
            "20500",
            "54,900",
            "5",
            "35",
            "3 Kitchens | 28 fireplaces | 3 elevators | 8 staircases",
            "n",
        ],
    )
    def testMainDoesntChangeTemplate(self, mock_stdout, mock_input):
        tomorrow = date.today() + timedelta(days=1)
        orig_template = deepcopy(template)

        main()

        self.assertEqual(orig_template, template)

        with open("1600-Pennsylvania-Ave-NW.json") as json_file:
            output = load(json_file)
            self.assertEqual(
                output,
                {
                    "listing_date": str(tomorrow),
                    "property": {
                        "address": {
                            "street_1": "1600 Pennsylvania Ave NW",
                            "street_2": "",
                            "city": "Washington",
                            "state": "DC",
                            "zip": "20500",
                        },
                        "square_footage": 54900,
                        "bedrooms": 5,
                        "bathrooms": 35,
                        "ammenities": [
                            "3 Kitchens",
                            "28 fireplaces",
                            "3 elevators",
                            "8 staircases",
                        ],
                    },
                    "broker": {
                        "name": "Tonya Sullivan",
                        "license_number": "ABCD1234",
                        "address": {
                            "street_1": "100 Fake St",
                            "street_2": None,
                            "city": "Boston",
                            "state": "MA",
                            "zip": "90210",
                        },
                        "referrer": None,
                    },
                },
            )

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch(
        "builtins.input",
        side_effect=[
            "1600 Pennsylvania Ave NW",
            "",
            "Washington",
            "DC",
            "20500",
            "54,900",
            "5",
            "35",
            "3 Kitchens | 28 fireplaces | 3 elevators | 8 staircases",
            "Y",
            "Kevin Bacon",
        ],
    )
    def testMainHandlesReferrer(self, mock_stdout, mock_input):
        tomorrow = date.today() + timedelta(days=1)
        orig_template = deepcopy(template)

        self.assertIsNotNone(orig_template)

        main()

        self.assertEqual(orig_template, template)

        with open("1600-Pennsylvania-Ave-NW.json") as json_file:
            output = load(json_file)

            self.assertEqual(
                output,
                {
                    "listing_date": str(tomorrow),
                    "property": {
                        "address": {
                            "street_1": "1600 Pennsylvania Ave NW",
                            "street_2": "",
                            "city": "Washington",
                            "state": "DC",
                            "zip": "20500",
                        },
                        "square_footage": 54900,
                        "bedrooms": 5,
                        "bathrooms": 35,
                        "ammenities": [
                            "3 Kitchens",
                            "28 fireplaces",
                            "3 elevators",
                            "8 staircases",
                        ],
                    },
                    "broker": {
                        "name": "Tonya Sullivan",
                        "license_number": "ABCD1234",
                        "address": {
                            "street_1": "100 Fake St",
                            "street_2": None,
                            "city": "Boston",
                            "state": "MA",
                            "zip": "90210",
                        },
                        "referrer": "Kevin Bacon",
                    },
                },
            )


if __name__ == "__main__":
    unittest.main()
