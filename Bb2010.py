import streamlit as st
import math

st.set_page_config(page_title="Budget Buddy", page_icon="💰")

st.title("Budget Buddy 💰")
st.write("Keep track of your money and plan your savings!")

tab1, tab2 = st.tabs(["My Budget 💵", "My Savings 🎯"])

with tab1:
    st.header("Let's Plan Your Monthly Budget")

    income = st.number_input("How much do you earn each month?", min_value=0.0, value=0.0, step=100.0)

    st.subheader("Plan Your Monthly Expenses")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        food = st.number_input("Food:", min_value=0.0, value=0.0, step=50.0)
        transport = st.number_input("Transportation:", min_value=0.0, value=0.0, step=50.0)

    with col2:
        education = st.number_input("Education:", min_value=0.0, value=0.0, step=50.0)
        entertainment = st.number_input("Entertainment:", min_value=0.0, value=0.0, step=50.0)

    with col3:
        shopping = st.number_input("Shopping:", min_value=0.0, value=0.0, step=50.0)
        other = st.number_input("Other:", min_value=0.0, value=0.0, step=50.0)

    if st.button("Check My Budget"):
        total_expenses = food + transport + education + entertainment + shopping + other
        remaining_balance = income - total_expenses

        st.divider()
        st.subheader("Here Are Your Budget Results")

        m_col1, m_col2, m_col3 = st.columns(3)

        m_col1.metric("Monthly Income", f"{income:,.0f} EGP")
        m_col2.metric("Total Expenses", f"{total_expenses:,.0f} EGP")
        m_col3.metric("Money Left", f"{remaining_balance:,.0f} EGP")

        if total_expenses > income:
            st.error("Your expenses are higher than your income!")
        elif