
import streamlit as st
import time



def convert_units(value, from_unit, to_unit, unit_type):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Yard": 1.09361},
        "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
        "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15},
        "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
        "Speed": {"m/s": 1, "km/h": 3.6, "mph": 2.23694},
    }
    
    if unit_type == "Temperature":
        return conversion_factors[unit_type][to_unit](value)
    else:
        return value * (conversion_factors[unit_type][to_unit] / conversion_factors[unit_type][from_unit])

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Adding custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            color: #333;
        }
        .stApp {
            background: linear-gradient(to right, #74ebd5, #acb6e5);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px;
        }
        .stSelectbox>div>div {
            background: #ffffff;
            border-radius: 10px;
            padding: 2px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔄 Unit Converter ")

# Adding animation
st.write("🎉 Celebrating Accurate Conversions! 🎉")
time.sleep(1)


# Unit categories
unit_categories = {
    "Length": ["Meter", "Kilometer", "Mile", "Yard"],
    "Weight": ["Gram", "Kilogram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day"],
    "Speed": ["m/s", "km/h", "mph"],
}

unit_type = st.selectbox("Select category", list(unit_categories.keys()))
from_unit = st.selectbox("From Unit", unit_categories[unit_type])
to_unit = st.selectbox("To Unit", unit_categories[unit_type])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_type)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    st.balloons()


st.caption("created by ❤️ Tayyaba Rafiq ")
