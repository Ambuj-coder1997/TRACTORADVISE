import streamlit as st
import random
import time
from datetime import datetime, timedelta
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
#from common import generate_engine_speed, generate_throttle_setting, generate_implement_depth, generate_actual_forward_speed, generate_latitude, generate_longitude

# Define the array of engine speed values
engine_speeds = [
    1525, 1548, 1536, 1582, 1535, 1562, 1549, 1548, 
    1500, 1527, 1411, 1248, 1619, 1650, 1681, 1500
]

# Initialize an index to keep track of the current position in the array
index = 0

def generate_engine_speed():
    global index
    # Get the current engine speed value
    speed = engine_speeds[index]
    # Update the index for the next call (wrap around if at the end)
    index = (index + 1) % len(engine_speeds)
    return speed

# Define the array of throttle setting values
throttle_settings = [
    65, 62, 61, 62, 63, 62, 65, 67, 
    61, 63, 60, 62, 82, 72, 75, 61
]

# Initialize an index to keep track of the current position in the array
throttle_index = 0

def generate_throttle_setting():
    global throttle_index
    # Get the current throttle setting value
    setting = throttle_settings[throttle_index]
    # Update the index for the next call (wrap around if at the end)
    throttle_index = (throttle_index + 1) % len(throttle_settings)
    return setting

# Define the array of implement depth values
implement_depths = [
    20.15, 19.65, 22.45, 21.62, 21.45, 25.65, 26.45, 23.97, 
    20.52, 22.14, 30.15, 32.68, 28.51, 26.48, 22.15, 20.52
]

# Initialize an index to keep track of the current position in the array
implement_depth_index = 0

def generate_implement_depth():
    global implement_depth_index
    # Get the current implement depth value
    depth = implement_depths[implement_depth_index]
    # Update the index for the next call (wrap around if at the end)
    implement_depth_index = (implement_depth_index + 1) % len(implement_depths)
    return depth

# Define the array of actual forward speed values
forward_speeds = [
    2.15, 2.36, 1.98, 2, 2.1, 2.3, 2.18, 2.49, 
    2.03, 2.11, 0.84, 0, 0.01, 0, 0, 2.03
]

# Initialize an index to keep track of the current position in the array
forward_speed_index = 0

def generate_actual_forward_speed():
    global forward_speed_index
    # Get the current forward speed value
    speed = forward_speeds[forward_speed_index]
    # Update the index for the next call (wrap around if at the end)
    forward_speed_index = (forward_speed_index + 1) % len(forward_speeds)
    return speed


def generate_latitude(current_lat):
    return current_lat + random.uniform(-0.0001, 0.0001)

def generate_longitude(current_long):
    return current_long + random.uniform(-0.0001, 0.0001)

# Define the array of slip values
slip_values = [
    9.56, 8.65, 10.45, 7.21, 9.84, 8.56, 7.48, 9.23, 
    8.54, 9.37, 89.51, 100, 98.65, 100, 100, 8.54
]

# Initialize an index to keep track of the current position in the array
slip_index = 0

def calculate_slip():
    global slip_index
    # Get the current slip value
    slip = slip_values[slip_index]
    # Update the index for the next call (wrap around if at the end)
    slip_index = (slip_index + 1) % len(slip_values)
    return slip


# Icon URLs for the table
icon_url = {
    "Gear Ratio": "https://fractory.com/wp-content/uploads/2020/09/Types-of-Gears.jpg",
    "Engine Speed": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTKyBS49iMPrJ85c0wm2X8ZQOU3K5CC4UIFh-9llBUeX0Q5Rxg8",
    "Throttle Setting": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqfyK_C2nQ7d2DbmoCG86HNJlPMjPmtkVkACmf2xovDLvVzjzW",
    "Implement Depth": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQXreG2Omv2h0DHS11b3KiY44Wij_WkqDJqIvjj-dPi4W-fQH1y",
    "Actual Speed": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTiwlixO0PSmDO-L67wHdYR0TChKAWNaRgYqa2nTrknkfv4nO7F",
    "Slip": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSvNzAhdKuoz6EivK0C1VqTLyUjccS8RU_t5PVG2rppTKTOftuM",
    "Latitude": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQobjC9X-TpXb8FtwTBAYyoKVzTdCLBtdSlsz-p0vTt2vd6ll1b",
    "Longitude": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQobjC9X-TpXb8FtwTBAYyoKVzTdCLBtdSlsz-p0vTt2vd6ll1b"
}

# Main function to display tractor parameters
def display_parameters():
    st.markdown(
        """
        <style>
        /* Set entire app background color to white */
        .main {
            background-color: white;
        }

        /* Set the table font and formatting */
        table {
            font-size: 25px;
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 10px;
        }

        th, td {
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: white;
            color: white;
        }

        /* Change background color of the table to white */
        table, th, td {
            background-color: white;
        }

        h3 {
            text-align: center;
            color: black;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1>Real-time Tractor Operating Parameters</h1>", unsafe_allow_html=True)

    # Dropdown for gear selection
    gear_options = {"L1": 160, "L2": 120, "L3": 80, "L4": 40, "H1": 30}
    gear = st.selectbox('Select the operating gear:', list(gear_options.keys()))
    x = gear_options[gear]

    # Initializing placeholders for output and map
    output_placeholder = st.empty()
    graph_placeholder = st.empty()
    map_placeholder = st.empty()

    current_lat = 22.31278
    current_long = 87.33152
    coordinates_list = []

    # Variables to store time for graphing
    time_stamps = []
    engine_speed_values = []
    throttle_values = []
    implement_depth_values = []
    forward_speed_values = []
    slip_values = []

    start_time = datetime.now()

    while True:
        current_time = (datetime.now() - start_time).total_seconds()

        # Generate the parameters
        engine_speed = generate_engine_speed()
        throttle_setting = generate_throttle_setting()
        implement_depth = generate_implement_depth()
        actual_speed = generate_actual_forward_speed()
        slip = calculate_slip()
        # Calculate Vt and slip
        #Vt = engine_speed / x
        #slip = 100 * (1 - ((actual_speed)/(Vt*3.14*1.6*(60/1000))))
        

        # Append data to the lists
        time_stamps.append(current_time)
        engine_speed_values.append(engine_speed)
        throttle_values.append(throttle_setting)
        implement_depth_values.append(implement_depth)
        forward_speed_values.append(actual_speed)
        slip_values.append(slip)

        # Update GPS coordinates
        current_lat = generate_latitude(current_lat)
        current_long = generate_longitude(current_long)
        coordinates_list.append({
            'latitude': current_lat,
            'longitude': current_long,
            'timestamp': datetime.now(),
            'speed': actual_speed
        })

        # Remove coordinates older than 10 seconds
        coordinates_list = [
            coord for coord in coordinates_list
            if coord['timestamp'] > datetime.now() - timedelta(seconds=10)
        ]

        # Create table with icons
        table_content = f"""
        <table>
            <tr>
            <td><b>Parameter</b></td>
            <td><b>Value</b></td>
            </tr>
            <tr>
                <td><img src="{icon_url['Gear Ratio']}" width="50"> Gear Ratio</td>
                <td>{gear}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Engine Speed']}" width="50"> Engine Speed (rpm)</td>
                <td>{engine_speed}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Throttle Setting']}" width="50"> Throttle Setting (%)</td>
                <td>{throttle_setting}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Implement Depth']}" width="50"> Implement Depth (cm)</td>
                <td>{implement_depth}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Actual Speed']}" width="50"> Actual Speed (km/h)</td>
                <td>{actual_speed}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Slip']}" width="50"> Slip (%)</td>
                <td>{slip:.2f}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Latitude']}" width="50"> Latitude (N)</td>
                <td>{current_lat}</td>
            </tr>
            <tr>
                <td><img src="{icon_url['Longitude']}" width="50"> Longitude (E)</td>
                <td>{current_long}</td>
            </tr>
        </table>
        """
        output_placeholder.markdown(table_content, unsafe_allow_html=True)

        # Plot the real-time data on the right with dots and shaded areas
        fig, ax = plt.subplots(5, 1, figsize=(10, 15), sharex=True)

        ax[0].plot(time_stamps, engine_speed_values, label="Engine Speed (rpm)", color='blue', marker='o')
        ax[0].fill_between(time_stamps, engine_speed_values, color='blue', alpha=0.2)

        ax[1].plot(time_stamps, throttle_values, label="Throttle Setting (%)", color='green', marker='o')
        ax[1].fill_between(time_stamps, throttle_values, color='green', alpha=0.2)

        ax[2].plot(time_stamps, implement_depth_values, label="Implement Depth (cm)", color='purple', marker='o')
        ax[2].fill_between(time_stamps, implement_depth_values, color='purple', alpha=0.2)

        ax[3].plot(time_stamps, forward_speed_values, label="Actual Speed (km/h)", color='orange', marker='o')
        ax[3].fill_between(time_stamps, forward_speed_values, color='orange', alpha=0.2)

        ax[4].plot(time_stamps, slip_values, label="Slip (%)", color='red', marker='o')
        ax[4].fill_between(time_stamps, slip_values, color='red', alpha=0.2)

        for i, axis in enumerate(ax):
            axis.legend(loc="upper right")
            axis.grid(True)

        ax[-1].set_xlabel("Time (s)")

        # Display plot
        graph_placeholder.pyplot(fig)

        # Create and display satellite map below plot
        m = folium.Map(location=[current_lat, current_long], zoom_start=15)
        for coord in coordinates_list:
            folium.Marker(
                location=[coord['latitude'], coord['longitude']],
                popup=f"Lat: {coord['latitude']}, Long: {coord['longitude']}, Speed: {coord['speed']} km/h"
            ).add_to(m)
        # Display map below the real-time graph
        with map_placeholder:
            folium_static(m, width=1000, height=500)

        time.sleep(3)  # Refresh rate of 3 seconds

def show_gps_page():
    display_parameters()

# Call the GPS page to run the app
if __name__ == "__main__":
    show_gps_page()
