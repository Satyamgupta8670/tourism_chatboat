import streamlit as st
import joblib
import pandas as pd
from PIL import Image  # For handling images
import time  # For animations

# Load the trained model
model = joblib.load("chatbot_model1.pkl")

# Load the data for responses
data = pd.read_csv("part2.csv")

# Streamlit app for the chatbot
st.title("🌏 Travel Chatbot")
st.subheader("Your personal travel assistant for exploring India!")
st.write(
    """
    Welcome to the Travel Chatbot! This bot is here to answer your questions about travel destinations, 
    best travel times, and things to do across India. Type your query below and let's get started!
    """
)

# Add an introductory image
image = Image.open("download.jpeg")  # Replace with your image path
st.image(image, use_column_width=True, caption="Explore India with us!")

# Add a loading animation
def show_typing_animation():
    with st.spinner("Bot is typing..."):
        time.sleep(2)  # Simulate a delay for better user experience

# Function to get response based on user input
def get_response(user_input):
    # Predict the intent
    intent = model.predict([user_input])[0]
    # Find a response that matches the intent
    response = data[data['Response Category'] == intent].sample(1)['Answers'].values[0]
    return response

# User input section
user_input = st.text_input("You: ", placeholder="Ask me about travel destinations, best times to visit, and more!")

# If there is user input, get and display the response
if user_input:
    show_typing_animation()  # Add the animation before showing the response
    response = get_response(user_input)
    st.success(f"Bot: {response}")

# Add a footer
st.markdown(
    """
    ---
    *Created with ❤️ using Streamlit. Explore the beauty of India like never before!*
    """
)
