import time
import matplotlib.pyplot as plt
import streamlit as st
import random
import time

def generate_throttle_values():
    return random.randint(55, 62)

def generate_engine_speed_values():
    return random.randint(1400, 1601)

def generate_implement_depth_values():
    return round(random.uniform(10.14, 22.46), 2)

def generate_forward_speed_values():
    return round(random.uniform(2.14, 3.46), 2)

# Function to calculate slip percentage
def calculate_slip():
    return round(random.uniform(12.15, 14.46), 2)

# Gear ratios (as per the provided list)
gear_ratios = [160, 120, 80, 40, 30]
# Icon URLs for the table
icon_url = {
    "Engine Torque": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQhkTm5C6-djVM3yJ6DZ--Yc3axxHSxT8RHVYB4Dthor-vWVhc4",
    "Fuel Consumption": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqc4p4DyeU5I0AzNnl7w1rYwsQrq3vV4ylviuU9JSy7g63vv0L",
    "Engine Power": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT0tSZjxD2nNXkGho7aCY3RdK-2SKylAUgV_XXxGGvnb3nIqhmq",
    "Specific Fuel Consumption": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXJIQWbLE_0DwM4BmilBbQIFC08CrGHqnKgMZM4Gv6YjuF0DdK",
    "Fuel Consumption per Tilled Area": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSUYRAAJNfkU0TtLoT7qmjouHO46frWiqYOppmIGytCzbORik9",
    "Implement Draft": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfbucYctsmUEAm34Ja4Xxgb1nVtv5comnkGPqqvwJVJAl7L0RY",
    "Drawbar Power": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkoQm9oof_qXb12jIbTZI3U5iI5MRV21ONG9GoW0LI65XZ1svq",
    "Tractive Efficiency": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8mr5HjL2hNmNZzCD63O5KszeL0khnYGNUd09ang3WgtXCUCZm",
}

# Function to generate the HTML table with icons and larger font size
def generate_table_html(params):
    table_content = """
    <table style="font-size: 18px; width: 100%; text-align: left;">
        <tr><th>Parameter</th><th>Value</th></tr>
    """
    table_content += f"""
    <tr>
        <td><img src="{icon_url['Engine Torque']}" alt="icon" style="width: 40px; height: 40px;"> Engine Torque (Nm)</td>
        <td>{params['engine_torque']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Fuel Consumption']}" alt="icon" style="width: 40px; height: 40px;"> Fuel Consumption (L/h)</td>
        <td>{params['fuel_consumption']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Engine Power']}" alt="icon" style="width: 40px; height: 40px;"> Engine Power (hp)</td>
        <td>{params['engine_power']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Specific Fuel Consumption']}" alt="icon" style="width: 40px; height: 40px;"> Specific Fuel Consumption (g/bhp-hr)</td>
        <td>{params['specific_fuel_consumption']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Fuel Consumption per Tilled Area']}" alt="icon" style="width: 40px; height: 40px;"> Fuel Consumption per Tilled Area (L/ha)</td>
        <td>{params['fuel_consumption_area']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Implement Draft']}" alt="icon" style="width: 40px; height: 40px;"> Implement Draft (kN)</td>
        <td>{params['implement_draft']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Drawbar Power']}" alt="icon" style="width: 40px; height: 40px;"> Drawbar Power (hp)</td>
        <td>{params['drawbar_power']:.2f}</td>
    </tr>
    <tr>
        <td><img src="{icon_url['Tractive Efficiency']}" alt="icon" style="width: 40px; height: 40px;"> Tractive Efficiency (%)</td>
        <td>{params['tractive_efficiency']:.2f}</td>
    </tr>
    """
    table_content += "</table>"
    return table_content

# Dummy function to simulate parameter calculation
def calculate_parameters():
    throttle = generate_throttle_values()
    engine_speed = generate_engine_speed_values()
    forward_speed = generate_forward_speed_values()
    implement_depth = generate_implement_depth_values()
    gear_ratio = random.choice(gear_ratios)

    slip = calculate_slip()

    # Calculate engine torque (Nm)
    #z = 24.49 * throttle + 42.483
    #r = z - engine_speed

    ent = round(random.uniform(150.45, 180.19), 2)

    # Fuel consumption (L/h)
    fcp = round(random.uniform(2.14, 3.46), 2)

    # Engine power (hp)
    enp = round(random.uniform(23.09, 25.16), 2)

    # Specific fuel consumption (kg/hp-hr)
    sfc = round(random.uniform(180, 185), 2)

    # Fuel consumption per tilled area (L/ha)
    FC = round((fcp * 10) / (0.6 * forward_speed),2)

    # Drawbar power (hp)
    dbp = round(enp*(random.uniform(0.68, 0.75)), 2)

    draft = round(3.6*0.746*dbp/forward_speed, 2)

    # Implement draft (kN)
    #draft = round(1.3*0.00078 * (652 + 5.1 * forward_speed ** 2) * 0.6 * implement_depth, 2)

    # Tractive efficiency (%)
    te = round(dbp * (100 - slip) / (0.9 * enp),2)

    return {
        'engine_torque': ent,
        'fuel_consumption': fcp,
        'engine_power': enp,
        'specific_fuel_consumption': sfc,
        'fuel_consumption_area': FC,
        'implement_draft': draft,
        'drawbar_power': dbp,
        'tractive_efficiency': te,
        'throttle': throttle,
        'engine_speed': engine_speed,
        'forward_speed': forward_speed,
        'implement_depth': implement_depth,
        'slip': slip
    }
 
# Main function to display tractor parameters
def display_parameters():
    st.markdown("<h1>Real-time Tractor Field Performance Prediction</h1>", unsafe_allow_html=True)

    # Initialize placeholders for output and graph
    output_placeholder = st.empty()
    graph_placeholder = st.empty()

    # Initialize lists to store data for plotting
    throttle_values = []
    engine_speed_values = []
    forward_speed_values = []
    implement_depth_values = []
    slip_values = []
    engine_torque_values = []
    fuel_consumption_values = []
    engine_power_values = []
    specific_fuel_consumption_values = []
    fuel_consumption_area_values = []
    implement_draft_values = []
    drawbar_power_values = []
    tractive_efficiency_values = []
    time_stamps = []

    # Infinite loop for continuous data generation
    while True:
        time_stamp = len(time_stamps)  # Using the list length as a time index

        # Calculate new parameters
        params = calculate_parameters()

        # Append new values to lists
        throttle_values.append(params['throttle'])
        engine_speed_values.append(params['engine_speed'])
        forward_speed_values.append(params['forward_speed'])
        implement_depth_values.append(params['implement_depth'])
        slip_values.append(params['slip'])
        engine_torque_values.append(params['engine_torque'])
        fuel_consumption_values.append(params['fuel_consumption'])
        engine_power_values.append(params['engine_power'])
        specific_fuel_consumption_values.append(params['specific_fuel_consumption'])
        fuel_consumption_area_values.append(params['fuel_consumption_area'])
        implement_draft_values.append(params['implement_draft'])
        drawbar_power_values.append(params['drawbar_power'])
        tractive_efficiency_values.append(params['tractive_efficiency'])
        time_stamps.append(time_stamp)

        # Generate the table with icons and larger font
        table_html = generate_table_html(params)
        output_placeholder.markdown(table_html, unsafe_allow_html=True)

        # Plot the real-time data on the right with dots and shaded areas
        fig, ax = plt.subplots(8, 1, figsize=(10, 15), sharex=True)

        ax[0].plot(time_stamps, engine_torque_values, label="Engine Torque (Nm)", color='green', marker='o')
        ax[0].fill_between(time_stamps, engine_torque_values, color='green', alpha=0.2)

        ax[1].plot(time_stamps, fuel_consumption_values, label="Fuel consumption (L/h)", color='blue', marker='o')
        ax[1].fill_between(time_stamps, fuel_consumption_values, color='blue', alpha=0.2)

        ax[2].plot(time_stamps, engine_power_values, label="Engine power (hp)", color='orange', marker='o')
        ax[2].fill_between(time_stamps, engine_power_values, color='orange', alpha=0.2)

        ax[3].plot(time_stamps, specific_fuel_consumption_values, label="Specific fuel consumption (g/bhp-hr)", color='purple', marker='o')
        ax[3].fill_between(time_stamps, specific_fuel_consumption_values, color='purple', alpha=0.2)

        ax[4].plot(time_stamps, fuel_consumption_area_values, label="Fuel consumption per tilled area (L/ha)", color='red', marker='o')
        ax[4].fill_between(time_stamps, fuel_consumption_area_values, color='red', alpha=0.2)

        ax[5].plot(time_stamps, implement_draft_values, label="Implement draft (kN)", color='pink', marker='o')
        ax[5].fill_between(time_stamps, implement_draft_values, color='pink', alpha=0.2)

        ax[6].plot(time_stamps, drawbar_power_values, label="Drawbar power (hp)", color='orange', marker='o')
        ax[6].fill_between(time_stamps, drawbar_power_values, color='orange', alpha=0.2)

        ax[7].plot(time_stamps, tractive_efficiency_values, label="Tractive efficiency (%)", color='blue', marker='o')
        ax[7].fill_between(time_stamps, tractive_efficiency_values, color='blue', alpha=0.2)

        for axis in ax:
            axis.legend(loc="upper right")
            axis.grid(True)

        ax[-1].set_xlabel("Time")

        # Display plot
        graph_placeholder.pyplot(fig)

        # Pause for a short time to simulate real-time behavior
        time.sleep(1)

# Run the real-time display function
if __name__ == "__main__":
    display_parameters()
