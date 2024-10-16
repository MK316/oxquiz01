import streamlit as st

# Define the correct answer (image name or number)
correct_image = "image_1"

# Display two images as buttons
st.write("Choose the correct image:")

col1, col2 = st.columns(2)

with col1:
    if st.button("button01"):
        selected_image = "images/button01"
        if selected_image == correct_image:
            st.success("Correct!")
        else:
            st.error("Wrong answer.")

with col2:
    if st.button("button02"):
        selected_image = "images/button02"
        if selected_image == correct_image:
            st.success("Correct!")
        else:
            st.error("Wrong answer.")

# Display the images (replace the URLs with your image paths)
col1.image("https://github.com/MK316/oxquiz01/raw/main/images/button01.png", use_column_width=True)
col2.image("https://github.com/MK316/oxquiz01/raw/main/images/button02.png", use_column_width=True)
