import streamlit as st
import time

# Define the array of headings
headings = [
    "Optimum tillage", "Optimum tillage", "Optimum tillage", "Optimum tillage", 
    "Optimum tillage", "Optimum tillage", "Optimum tillage", "Optimum tillage", 
    "Optimum tillage", "Optimum tillage", "Reduce the depth", "Reduce the depth", 
    "Gear: L2, Throttle: 70%", "Gear: L2, Throttle: 65%", "Gear: L2, Throttle: 65%", 
    "Optimum tillage", "Optimum tillage", "Optimum tillage", "Optimum tillage"
]

# Initialize an index to track the current heading
heading_index = 0

def show_fc_page():
    global heading_index

    # Display the first heading (this will remain constant)
    st.markdown("<h1 style='text-align: center; color: #b5101c;'>Real-time Tractor Advisory System</h1>", unsafe_allow_html=True)

    # Create a placeholder for the second heading
    placeholder = st.empty()

    # Loop through headings every 5 seconds
    while True:
        # Get the current heading
        current_heading = headings[heading_index]

        # Display the second heading in the placeholder
        placeholder.markdown(f"<h2 style='text-align: center; color: #4d3b02;'>{current_heading}</h2>", unsafe_allow_html=True)

        # Update the index for the next heading (wrap around if at the end)
        heading_index = (heading_index + 1) % len(headings)

        # Wait for 5 seconds before updating again
        time.sleep(5)

# Example usage
if __name__ == '__main__':
    show_fc_page()
