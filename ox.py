import streamlit as st

# Define the correct answer
correct_image = "button01"

# Display two images as buttons
st.write("Choose the correct image:")

# Create two columns for the images
col1, col2 = st.columns(2)

# Image and button for the first choice
with col1:
    st.image("https://github.com/MK316/oxquiz01/raw/main/images/button01.png", use_column_width=True)
    if st.button("Select Image 1"):
        selected_image = "button01"
        if selected_image == correct_image:
            st.success("Correct!")
        else:
            st.error("Wrong answer.")

# Image and button for the second choice
with col2:
    st.image("https://github.com/MK316/oxquiz01/raw/main/images/button02.png", use_column_width=True)
    if st.button("Select Image 2"):
        selected_image = "button02"
        if selected_image == correct_image:
            st.success("Correct!")
        else:
            st.error("Wrong answer.")
