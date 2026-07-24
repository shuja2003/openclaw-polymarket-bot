import requests

def get_shanghai_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=31.23&longitude=121.47&daily=temperature_2m_max&timezone=Asia%2FShanghai"

    data=requests.get(url, timeout=10).json()

    temp = data["daily"]["temperature_2m_max"][0]

    return temp


if __name__ == "__main__":
    print("Shanghai forecast high:", get_shanghai_weather())
