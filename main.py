import requests
from datetime import datetime, timezone
import smtplib
from time import sleep

MY_EMAIL = "email"
MY_PASSWORD = "password"

# Berlin coordinates
MY_LAT = 52.5200
MY_LONG = 13.4050

# Function to check if the ISS is close to the given coordinates
def is_iss_close_to_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    latitude = float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])

    # Check if the ISS is within 5 degrees of the given location
    if (MY_LAT - 5 <= latitude <= MY_LAT + 5) and (MY_LONG - 5 <= longitude <= MY_LONG + 5):
        return True
    return False

# Function to check if it is currently night at the given coordinates
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    sunrise = response.json()["results"]["sunrise"]
    sunset = response.json()["results"]["sunset"]

    # Convert sunrise and sunset to datetime objects in UTC
    sunrise_time = datetime.fromisoformat(sunrise).replace(tzinfo=timezone.utc)
    sunset_time = datetime.fromisoformat(sunset).replace(tzinfo=timezone.utc)

    # Get the current time in UTC
    time_now = datetime.now(timezone.utc)

    # Check if the current time is before sunrise or after sunset (i.e., it's night)
    if time_now >= sunset_time or time_now <= sunrise_time:
        return True
    return False

# Main loop that runs every 60 seconds to check if the ISS is nearby and it's night
while True:
    sleep(60)
    if is_iss_close_to_me() and is_night():
        # Establish a connection to the SMTP server to send an email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up! \n\nThe ISS is close to you!"
            )
