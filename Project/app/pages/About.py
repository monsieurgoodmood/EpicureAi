import streamlit as st


# [theme]
# base="light"
# primaryColor="#000000"
# secondaryBackgroundColor="#acecaf"
# textColor="#000000"

st.title("Epicure AI")

st.write(
    "Epicure AI is an innovative and intelligent kitchen companion designed to elevate your cooking experience."
    " Harnessing the power of advanced object detection using YOLOv8 technology, our app revolutionizes the way you approach meal preparation."
)

st.subheader("Key Features:")

st.write(
    "1. **Smart Kitchen Ingredients Scanning:** Snap a picture of your refrigerator contents, and Epicure AI's powerful YOLOv8-based object detection system identifies every ingredient with precision."
    "\n\n2. **Instant Recipe Suggestions:** Seamlessly receive personalized recipe suggestions based on the ingredients detected in your fridge. Say goodbye to wasted groceries and hello to creative culinary adventures."
    "\n\n3. **Can Cook Based on Your Dietary Needs:** Epicure AI caters to your specific dietary requirements, offering recipe suggestions that align with your nutritional preferences."
)

st.subheader("How It Works:")

st.write(
    "- **Capture:** Take a quick photo of the contents of your fridge using the Epicure AI app."
    "\n\n- **Detect:** Our cutting-edge YOLOv8 algorithm identifies each item in your fridge, creating a comprehensive list of ingredients."
    "\n\n- **Recommend:** Receive instant recipe suggestions based on the detected ingredients. Choose from a variety of cuisines and cooking styles."
    "\n\n- **Create:** Follow step-by-step instructions, cooking tips, and personalized modifications to create a delicious meal tailored to your preferences."
)

st.write(
    "**Elevate Your Culinary Journey with Epicure AI - Where Technology Meets Taste!**"
)
