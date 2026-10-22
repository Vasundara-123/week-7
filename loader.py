
"""
Script to load geographical data into a pandas DataFrame
and save the results into a CSV file.
"""

from geopy.geocoders import Nominatim
import pandas as pd


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    # Create a geolocator using the given agent name
    return Nominatim(user_agent=agent)


def fetch_location_data(geolocator, loc):
    # Try to find the location using the geolocator
    try:
        location = geolocator.geocode(loc)

        # If the location is not found, return None for its details
        if location is None:
            return {
                "location": loc,
                "latitude": None,
                "longitude": None,
                "type": None
            }

        # If the location exists, collect its coordinates and type
        return {
            "location": loc,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": location.raw.get("type")
        }

    except Exception as e:
        # Handle any errors that occur while fetching the location
        print(f"Error fetching location {loc}: {e}")

        # Return empty values if the location details cannot be fetched
        return {
            "location": loc,
            "latitude": None,
            "longitude": None,
            "type": None
        }


def build_geo_dataframe(locations):
    # Set up the geolocator to search for the given locations
    geolocator = get_geolocator()

    # Collect the location details for each name in the list
    geo_data = [
        fetch_location_data(geolocator, loc)
        for loc in locations
    ]

    # Convert the collected data into a pandas DataFrame
    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    # Create the geolocator and list the locations to search for
    geo = get_geolocator()

    locations = [
        "Museum of Modern Art",
        "iuyt8765(*&)",
        "Alaska",
        "Franklin's Barbecue",
        "Burj Khalifa"
    ]

    # Build a DataFrame using the location details
    df = build_geo_dataframe(locations)

    # Save the DataFrame as a CSV file
    df.to_csv("./geo_data.csv")
