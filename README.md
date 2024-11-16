# ISS Notifier

This project is a Python script that sends an email notification whenever the International Space Station (ISS) is close to your location and it is currently nighttime. It uses public APIs to track the ISS and calculate sunrise and sunset times, making it easy for you to catch a glimpse of the ISS.

## Features
- Checks if the ISS is within 5 degrees of your location.
- Determines if it is currently nighttime at your location.
- Sends an email notification when both conditions are met.

## Requirements
- Python 3
- Internet connection
- An email account for sending notifications, and the server address should be checked based on the email provider

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/utkualtintug/ISS-Notifier
   ```
2. Install the required Python libraries:
   ```sh
   pip install requests
   ```

## Usage
1. Replace `MY_EMAIL` and `MY_PASSWORD` in the script with your email credentials. Ensure to check the SMTP server details for your email provider (e.g., smtp.gmail.com for Gmail). Using your email and password directly can be insecure; consider using an application-specific password.

2. Update the coordinates (`MY_LAT` and `MY_LONG`) with your latitude and longitude. The default coordinates are for Berlin.

3. Run the script:
   ```sh
   python iss_notifier.py
   ```

The script will run in an infinite loop, checking every 60 seconds whether the ISS is close and whether it is nighttime. If both conditions are met, you will receive an email notification.

## API References
- [Open Notify API](http://api.open-notify.org/iss-now.json) - To get the current position of the ISS.
- [Sunrise-Sunset API](https://sunrise-sunset.org/api) - To get the sunrise and sunset times for your location.

## Important Notes
- **Security Warning**: The script currently uses plain text for your email credentials. This can be insecure, especially if the script is shared or deployed. Consider using environment variables or a secure credential manager.
- **Timezone Handling**: The sunrise and sunset times are in UTC. Ensure your current time (`time_now`) is correctly adjusted to UTC for accurate comparison.

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## Disclaimer
This script is intended for educational purposes only. Be mindful of the API usage limits and your email security.

