import requests, os, time, json

timezone = "CET"

locations = {
  "Oslo": (59.91273, 10.74609),
  "Ski": (59.7191555, 10.8347286),
  "Røstad": (59.31589, 10.76650)
}


def main():
  while True:
    lat, long = getLocation()
    weather_code, max_temp, min_temp, max_wind, min_wind = getForecast(lat, long)
    weather_code = WeatherCodeAsText(weather_code)
    max_temp = prettyTemp(max_temp)
    min_temp = prettyTemp(min_temp)
    os.system("clear")
    print(f"--- Været for i dag ---\n")
    print(weather_code)
    print(f"Min: {min_temp}")
    print(f"Max: {max_temp}")
    print(f"Min vind: {min_wind} - {get_beaufort(min_wind)}")
    print(f"Max vind: {max_wind} - {get_beaufort(max_wind)}")
    choice = input("\nSe en ny værmelding? j/n: ").strip().lower()
    if choice != "j":
      break
  
# Get the loactaion from the locations dictionary
def getLocation():
  os.system("clear")
  print("--- Steder ---\n")
  for index, location in enumerate(locations.keys(), start=1):
    print(f"{index}: {location}")
  selection = int(input("\nVelg et sted: "))
  location = list(locations.keys())[selection - 1]
  return locations[location]


# Get the weather for a latitude and longitude, return todays weather code, max and min temp
def getForecast(lat, long):
  result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=weathercode,temperature_2m_max,temperature_2m_min,windspeed_10m_max,windspeed_10m_min&wind_speed_unit=ms&timezone={timezone.upper()}")
  forecast = result.json()
  # print(json.dumps(forecast, indent=2))
  # time.sleep(30)
  
  weather_code = forecast["daily"]["weathercode"][0]
  max_temp = forecast["daily"]["temperature_2m_max"][0]
  min_temp = forecast["daily"]["temperature_2m_min"][0]
  max_wind = forecast["daily"]["windspeed_10m_max"][0]
  min_wind = forecast["daily"]["windspeed_10m_min"][0]
  return weather_code, max_temp, min_temp, max_wind, min_wind


# Get the temperature as a float, add emojis accordingly:
def prettyTemp(temp):
  if temp <= 0:
    return f"❄️ {temp}"
  elif 0 < temp <= 10:
    return f"🧥 {temp}"
  elif 10 < temp <= 20:
    return f"👕 {temp}"
  elif temp > 20:
    return f"🌡️ {temp}"


def get_beaufort(wind):
  beaufort_scale = [
    (0.3, "Stille"),
    (1.6, "Svak vind"),
    (3.4, "Lett bris"),
    (5.6, "Svak bris"),
    (8.0, "Moderat bris"),
    (10.8, "Frisk bris"),
    (13.9, "Liten kuling"),
    (17.2, "Stiv kuling"),
    (20.8, "Sterk kuling"),
    (24.5, "Liten storm"),
    (28.5, "Full storm"),
    (32.7, "Sterk storm"),
    (float('inf'), "Orkan")
  ]

  for threshold, description in beaufort_scale:
    if wind < threshold:
      return description


def WeatherCodeAsText(weather_code):
  weather_codes = {
    0: "Klar himmel",
    1: "For det meste klart",
    2: "Delvis overskyet",
    3: "Overskyet",
    45: "Tåke",
    48: "Rimfrost",
    51: "Yr: Lett",
    53: "Yr: Moderat",
    55: "Yr: Tett",
    56: "Isende yr: Lett",
    57: "Isende yr: Tett",
    61: "Regn: Lett",
    63: "Regn: Moderat",
    65: "Regn: Kraftig",
    66: "Isregn: Lett",
    67: "Isregn: Kraftig",
    71: "Snøfall: Lett",
    73: "Snøfall: Moderat",
    75: "Snøfall: Kraftig",
    77: "Snøfnugg",
    80: "Regnbyger: Lett",
    81: "Regnbyger: Moderat",
    82: "Regnbyger: Voldsom",
    85: "Snøbyger: Lett",
    86: "Snøbyger: Kraftig",
    95: "Tordenvær: Lett eller moderat",
    96: "Tordenvær med lett hagl",
    99: "Tordenvær med kraftig hagl"
  }
  return weather_codes.get(weather_code, "Ukjent værkode")

main()
