import cv2
import streamlit as st
import numpy as np
import tempfile

# Use this line to capture video from the webcam
cap = cv2.VideoCapture(0)


# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")

frame_placeholder = st.empty()

# Add a "Stop" button and store its state in a variable
stop_button_pressed = st.button("Stop")

while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    # You can process the frame here if needed
    # e.g., apply filters, transformations, or object detection

    # Convert the frame from BGR to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(frame, channels="RGB")

    # Break the loop if the 'q' key is pressed or the user clicks the "Stop" button
    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed: 
        break

cap.release()
cv2.destroyAllWindows()
