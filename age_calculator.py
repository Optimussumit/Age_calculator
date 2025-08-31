import streamlit as st
from datetime import datetime, date, time


def calculate_age(birth_datetime):
    now = datetime.now()

    # Calculate total age difference
    delta = now - birth_datetime

    # Breakdown into parts
    years = now.year - birth_datetime.year
    months = now.month - birth_datetime.month
    days = now.day - birth_datetime.day
    hours = now.hour - birth_datetime.hour
    minutes = now.minute - birth_datetime.minute
    seconds = now.second - birth_datetime.second
    microseconds = now.microsecond

    # Adjust negatives
    if seconds < 0:
        seconds += 60
        minutes -= 1
    if minutes < 0:
        minutes += 60
        hours -= 1
    if hours < 0:
        hours += 24
        days -= 1
    if days < 0:
        months -= 1
        previous_month = now.month - 1 or 12
        days += (date(now.year if previous_month != 12 else now.year - 1, previous_month + 1, 1) - date(now.year if previous_month != 12 else now.year - 1, previous_month, 1)).days
    if months < 0:
        months += 12
        years -= 1

    return years, months, days, hours, minutes, seconds, microseconds


# Streamlit UI
st.set_page_config(page_title="Age Calculator", layout="centered")
st.title("📅 Age Calculator")

st.markdown("Enter your **birth date and time** to calculate your exact age.")

# Date input
birth_date = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

# Time input
hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=0, step=1)
minute = st.number_input("Minute (0-59)", min_value=0, max_value=59, value=0, step=1)
second = st.number_input("Second (0-59)", min_value=0, max_value=59, value=0, step=1)

# On submit
if st.button("Calculate Age"):
    try:
        birth_datetime = datetime.combine(birth_date, time(hour, minute, second))
        y, m, d, h, mi, s, ms = calculate_age(birth_datetime)

        st.success(f"🎉 You are **{y} years, {m} months, {d} days, {h} hours, {mi} minutes, {s} seconds, and {ms} microseconds** old.")
    except Exception as e:
        st.error(f"Error: {e}")
