import streamlit as st

st.title("⚡ Smart Rent & Electricity Splitter")

# Section 1: Basic Accommodation Inputs
rent = st.number_input("Enter Flat/Hostel Rent:", min_value=0.0, value=None)
food = st.number_input("Enter Food Expense:", min_value=0.0, value=None)
persons = st.number_input("Enter Number of People:", min_value=1, step=1, value=None)

# Section 2: Custom Electricity Tariff Slab Inputs
st.subheader("🔌 Electricity Slab Rates")
a = st.number_input("Rate for 0 to 200 units (a):", min_value=0.0, value=None)
b = st.number_input("Rate for 201 to 500 units (b):", min_value=0.0, value=None)
c = st.number_input("Rate for 501 to 700 units (c):", min_value=0.0, value=None)
d = st.number_input("Rate for 701 to 1000 units (d):", min_value=0.0, value=None)
e = st.number_input("Rate for above 1000 units (e):", min_value=0.0, value=None)

units = st.number_input("Enter Total Electricity Units Used:", min_value=0.0, value=None)

# Check if the user has filled in ALL the input fields
if (rent is not None and food is not None and persons is not None and 
    units is not None and a is not None and b is not None and 
    c is not None and d is not None and e is not None):

    # YOUR EXACT CALCULATION LOGIC (100% Unchanged)
    if units <= 200:
        electricity_bill = units * a
    elif units <= 500:
        electricity_bill = (200 * a) + ((units - 200) * b)
    elif units <= 700:
        electricity_bill = (200 * a) + (300 * b) + ((units - 500) * c)
    elif units <= 1000:
        electricity_bill = (200 * a) + (300 * b) + (200 * c) + ((units - 700) * d)
    else:
        electricity_bill = (
            (200 * a) + (300 * b) + (200 * c) + (300 * d) + ((units - 1000) * e)
        )

    total_expense = rent + food + electricity_bill
    per_person_share = total_expense / persons

    # Section 3: Clean & Simple Output Layout (No columns, just line-by-line metrics)
    st.subheader("📊 Final Calculations")
    
    st.metric(label="Electricity Bill", value=f"₹{electricity_bill:.2f}")
    st.metric(label="Total Expense", value=f"₹{total_expense:.2f}")
    st.metric(label="Each Person Pays", value=f"₹{per_person_share:.2f}")

else:
    # This message shows until the user fills in every box
    st.info("👋 Please fill in all the input boxes above to calculate the bill.")

