#This is an app to send an alert to the user when rain is forecasted
#Using an API
# Use your own email and password
import requests
#if you want to use Twilio:
#from twilio.rest import Client
#import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_API_key"
#it is strongly suggested you use an environmental key instead
#and import OS, and change it in the code
#api_key = OWM_API_KEY
#auth_token = OWM_AUTH_TOKEN
MY_LAT = 35.136361
MY_LONG = 129.098109
#I'm using email instead of Twilio:
MY_EMAIL = "your_email"
MY_PASSWORD = "your_password"
#If you're using Twilio:
# account_sid = “somelongstring”
# auth_token = “your_auth_token”
# client = Client(account_sid, auth_token)

weather_params{
    "lat" = MY_LAT, # type: ignore
    "lon" = MY_LONG,
    "appid" = api_key,
    "cnt" = 3
}

#Getting the data
response = requests.get(OWM_Endpoint, params=weather_params)
#Test: You should get a 200 code. If you got a 400, check your api key and your appid.
#print(response.status_code)
response.raise_for_status()
#To see the data in a better format, copy it out of your console and paste it into http://jsonviewer.stack.hu
weather_data = response.json()

#The id code is coded for precipitation and atmospheric conditions
#If the ID code is below 700, tell the user to bring an umbrella
will_rain = False
will_rain():
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        #send an SMS text (Twilio) or email that says "It is going to rain today. Remember to bring your ☂️."
        connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up☝️\n\nIt is going to rain today. Remember to bring your ☂️!"
        )
        
        # If you're using Twilio:
        # message = client.messages \
        #     .create(
        #         body="Something."
        #         from_="+phonenumber"
        #         to="+otherphonenumber"
        #         )
        # print(message.status)

        #Testing
        # Switch to a location where it is currently raining.
        # Check ventusky.com to find a place where it is raining
        # Then go to latlong.net to get the lat and lon to test
        #print("It is going to rain today. Remember to bring your ☂️.")

#Now we need to run this thing every morning at 6:00 AM to get the
#email or message using pythonanywhere.com
#Warning: You only get ONE project on the free tier. So delete the
#birthday wisher if you've done that here.
#Upload main.py and enter the command to run the code under python 3 main.py
#If you do this, change 3 lines of code to work with Twilio:
#from twilio.http.http_client import TwilioHttpClient
#Now create a proxy client above the account_sid
#proxy_client = "TwilioHttpClient()"
#proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

#also be sure Python Anywhere has your environment variables
#using export X_X=string; y_y-string; python3 main.py

#Now go to if will_rain and client = and type:
#client = Client(account_sid, auth_token, http_client=proxy_client)

#to test in Python Anywhere, change the time to the current UTC time
#where you are, then back to 7:00 AM
#to test type at the bottom:
#print message.status)





