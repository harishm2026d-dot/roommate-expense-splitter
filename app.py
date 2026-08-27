import streamlit as st

st.title("⚡ Smart Rent & Electricity Splitter")

# Section 1: Core Accommodation & Energy Inputs
rent = st.number_input("Enter Flat/Hostel Rent:", min_value=0.0, value=None)
food = st.number_input("Enter Food Expense:", min_value=0.0, value=None)
persons = st.number_input("Enter Number of People:", min_value=1, step=1, value=None)
units = st.number_input("Enter Total Electricity Units Used:", min_value=0.0, value=None)

# Initialize variables to a safe default of 0.0 so Python logic doesn't crash
a = b = c = d = e = 0.0
all_required_rates_filled = False

# Section 2: Smart Dynamic Tariff Inputs (Only show what is required)
if units is not None:
    st.subheader("🔌 Required Electricity Slab Rates")
    
    # Condition 1: Always need Rate A if units are greater than 0
    if units > 0:
        a = st.number_input("Rate for 0 to 200 units (a):", min_value=0.0, value=None)
        all_required_rates_filled = (a is not None)

    # Condition 2: Need Rate B only if units exceed 200
    if units > 200:
        b = st.number_input("Rate for 201 to 500 units (b):", min_value=0.0, value=None)
        all_required_rates_filled = (a is not None and b is not None)

    # Condition 3: Need Rate C only if units exceed 500
    if units > 500:
        c = st.number_input("Rate for 501 to 700 units (c):", min_value=0.0, value=None)
        all_required_rates_filled = (a is not None and b is not None and c is not None)

    # Condition 4: Need Rate D only if units exceed 700
    if units > 700:
        d = st.number_input("Rate for 701 to 1000 units (d):", min_value=0.0, value=None)
        all_required_rates_filled = (a is not None and b is not None and c is not None and d is not None)

    # Condition 5: Need Rate E only if units exceed 1000
    if units > 1000:
        e = st.number_input("Rate for above 1000 units (e):", min_value=0.0, value=None)
        all_required_rates_filled = (a is not None and b is not None and c is not None and d is not None and e is not None)

# Section 3: Safe Mathematical Execution Payload
if rent is not None and food is not None and persons is not None and units is not None and all_required_rates_filled:

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

    # Section 4: Display Output Summary
    st.subheader("📊 Final Calculations")
    st.metric(label="Electricity Bill", value=f"₹{electricity_bill:.2f}")
    st.metric(label="Total Expense", value=f"₹{total_expense:.2f}")
    st.metric(label="Each Person Pays", value=f"₹{per_person_share:.2f}")

else:
    # Informative landing prompt state
    st.info("👋 Please enter all visible core details and required rates above to compute.")
