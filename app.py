import streamlit as st
import datetime
import requests
import pandas as pd

'''
# Welcome to the Taxi Fare Prediction app!
'''

# Display a map of New York City
nyc_center = pd.DataFrame({
    'lat': [40.7128],
    'lon': [-74.0060]
})

st.map(nyc_center, zoom=10)

st.markdown('''

## This app allows you to input ride parameters to get an estimated fare for your taxi ride.
''')


# Date and time input
ride_date = st.date_input('Select the date of the ride', datetime.date.today())
ride_time = st.time_input('Select the time of the ride', datetime.datetime.now().time())

# Coordinates input
pickup_longitude = st.number_input('Pickup Longitude', format="%.6f")
pickup_latitude = st.number_input('Pickup Latitude', format="%.6f")
dropoff_longitude = st.number_input('Dropoff Longitude', format="%.6f")
dropoff_latitude = st.number_input('Dropoff Latitude', format="%.6f")

# Passenger count input
passenger_count = st.number_input('Passenger Count', min_value=1, step=1)

# Build the dictionary
params = {
        'pickup_datetime': f"{ride_date} {ride_time}",
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }


url = 'https://taxifare.lewagon.ai/predict'


if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('**Predicted Fare:**')


# Call the API using the requests package
response = requests.get(url, params=params)

st.header(f" ${round(response.json()['fare'],2)}")
