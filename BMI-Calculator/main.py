import streamlit as st

st.set_page_config(
    page_icon="🧮", page_title="BMI Calculator", layout="centered")

st.title("🧮 BMI Calculator by Hafiz Siddiqui")
st.markdown("Calculate your BMI (Body Mass Index)")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (Kg):", min_value=0.0, format="%.2f")
with col2:
    height = st.number_input("Height (m):", min_value=0.0, format="%.2f")


if st.button("Calculate BMI"):
    if weight == 0.0 or height == 0.0:
        st.warning("Please enter a valid weight and height")
    else:
        bmi = weight / (height ** 2)
        st.subheader("Your BMI is:")
        st.markdown(f"**{bmi:.2f}**")

        if bmi < 18.5:
            st.error("You are underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("🎉 Your weight is normal")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight")
        else:
            st.error("Obesity 🏮")
