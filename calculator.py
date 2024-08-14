
import streamlit as st

# Set title
st.title("Simple Calculator")

# User input
num1 = st.number_input("Enter the first number:", format="%f")
operation = st.selectbox("Select operation:", ("+", "-", "*", "/"))
num2 = st.number_input("Enter the second number:", format="%f")

# Perform the calculation
result = None
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero")
    
    if result is not None:
        st.success(f"The result is: {result}")

# Display the result
if result is not None:
    st.write(f"Result: {result}")
