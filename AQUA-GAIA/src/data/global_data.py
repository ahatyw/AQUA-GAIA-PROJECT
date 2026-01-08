import pandas as pd

def get_global_water_data():
    data = {
        "Country": [
            "India", "United States", "China", "Brazil",
            "Australia", "Germany", "South Africa", "Russia"
        ],
        "ISO": ["IND", "USA", "CHN", "BRA", "AUS", "DEU", "ZAF", "RUS"],
        "WaterQuality": [68, 82, 71, 74, 85, 88, 65, 70],
        "Pollution": [55, 35, 60, 48, 30, 25, 58, 52],
        "FreshwaterAvailability": [62, 78, 65, 80, 72, 83, 60, 68]
    }
    return pd.DataFrame(data)
