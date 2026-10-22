
import unittest
from loader import *


class TestLoader(unittest.TestCase):

    def test_valid_locations(self):
        # Set up the geolocator to check the locations
        geolocator = get_geolocator()

        # These are the known locations and their expected details
        locations = [
            ("Museum of Modern Art", 40.7618552, -73.9782438, "museum"),
            ("USS Alabama Battleship Memorial Park", 30.684373, -88.015316, "park")
        ]

        # Go through each location and compare the results
        for name, expected_lat, expected_lon, expected_type in locations:
            with self.subTest(location=name):
                result = fetch_location_data(geolocator, name)

                # Check whether the location name matches
                self.assertEqual(result["location"], name)

                # Make sure latitude and longitude are available
                self.assertIsNotNone(result["latitude"])
                self.assertIsNotNone(result["longitude"])

                # Compare the coordinates with the expected values
                # A small difference is allowed since coordinates may vary
                self.assertAlmostEqual(
                    result["latitude"], expected_lat, delta=0.02
                )

                self.assertAlmostEqual(
                    result["longitude"], expected_lon, delta=0.02
                )

                # Check if the location type matches the expected type
                self.assertEqual(
                    result["type"], expected_type
                )

    def test_invalid_location(self):
        # Set up the geolocator for testing an invalid location
        geolocator = get_geolocator()

        # Try searching for a location that does not exist
        result = fetch_location_data(geolocator, "asdfqwer1234")

        # The location name should still be present in the result
        self.assertEqual(result["location"], "asdfqwer1234")

        # Since the location does not exist, these values should be None
        self.assertIsNone(result["latitude"])
        self.assertIsNone(result["longitude"])
        self.assertIsNone(result["type"])


if __name__ == "__main__":
    # Run the tests to check whether the loader works correctly
    unittest.main()
