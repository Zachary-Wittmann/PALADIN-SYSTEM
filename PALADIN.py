import requests
import pandas as pd
import numpy as np


def calculate_distance_and_duration(origin, destination, api_key):
    """Calculate the distance and duration between two addresses."""
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&units=imperial&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK" and data["rows"][0]["elements"][0]["status"] == "OK":
        distance_miles = data["rows"][0]["elements"][0]["distance"]["text"]
        duration_text = data["rows"][0]["elements"][0]["duration"]["text"]
        # Simplified conversion; adjust as needed
        duration_minutes = int(duration_text.split()[0])
        return distance_miles, duration_text, duration_minutes
    else:
        return None, None, None  # Return None if no valid distance or duration is found


def find_nearest_for_each_address_and_form_clusters(df, api_key):
    addresses = df["incident>>address"].tolist()
    nearest_addresses = []
    distances_to_nearest = []
    times_to_nearest = []
    # Initialize a matrix to hold travel times between addresses
    time_matrix = pd.DataFrame(np.inf, index=addresses, columns=addresses)

    for origin_index, origin in enumerate(addresses):
        print(f"Processing {origin}...")  # Optional: for tracking progress
        min_distance = float("inf")
        nearest_address = None
        time_to_nearest = float("inf")

        for destination_index, destination in enumerate(addresses):
            if origin_index != destination_index:
                distance, duration, duration_minutes = calculate_distance_and_duration(
                    origin, destination, api_key
                )
                if duration_minutes is not None and duration_minutes < time_to_nearest:
                    time_matrix.at[origin, destination] = duration_minutes
                    min_distance = distance
                    nearest_address = destination
                    time_to_nearest = duration_minutes

        nearest_addresses.append(nearest_address)
        distances_to_nearest.append(min_distance)
        times_to_nearest.append(time_to_nearest)

    # Here you would implement the clustering logic based on `time_matrix`
    # For simplicity, let's assume you have a function `form_clusters(time_matrix)` that returns
    # a dictionary mapping addresses to cluster IDs
    # Implement this function based on your clustering logic
    clusters = form_clusters(time_matrix)

    df["Nearest_Address"] = nearest_addresses
    df["Distance_to_Nearest (miles)"] = distances_to_nearest
    df["Time_to_Nearest"] = times_to_nearest
    df["Cluster_ID"] = df["incident>>address"].map(clusters)

    print(df.head())


def form_clusters(time_matrix):
    # Placeholder clustering logic
    return {address: 1 for address in time_matrix.index}


# REPLACE the example DataFrame with reading from a CSV file
input_csv = "data/datashort.csv"  # Name of your input CSV file
df = pd.read_csv(input_csv)

# Replace with your actual Google Maps API key
api_key = ""

# Find the nearest address for each entry in the DataFrame
find_nearest_for_each_address_and_form_clusters(df, api_key)

# Save the updated DataFrame to a CSV file
output_csv = "data/updated_addresses_with_nearest.csv"
df.to_csv(output_csv, index=False)
print(f"Updated DataFrame saved to {output_csv}")
