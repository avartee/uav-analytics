import json
from datetime import datetime

FILTER_DATE = datetime(2026, 5, 1)

def filter_data(data):
    past_incidents = [
        item for item in data.get('pastIncidents', [])
        if datetime.strptime(item['date'], '%Y-%m-%d') >= FILTER_DATE
    ]
    forecast_targets = [
        item for item in data.get('forecastTargets', [])
        if datetime.strptime(item['date'], '%Y-%m-%d') >= FILTER_DATE
    ]
    return {"pastIncidents": past_incidents, "forecastTargets": forecast_targets}

if __name__ == "__main__":
    try:
        with open('data.json', 'r') as f:
            raw_data = json.load(f)
            processed_data = filter_data(raw_data)
        
        with open('data.json', 'w') as f:
            json.dump(processed_data, f, indent=4)
        print("Data successfully filtered.")
    except Exception as e:
        print(f"Error processing data: {e}")
