import streamlit as st
import pandas as pd
import time

@st.dialog("User Details")
def user_details():
    username = st.text_input("Enter your username here :")
    email = st.text_input("Enter your email address here :")
    if st.button("Login"):
        st.write(f"{username} has logged in")


def main():
    st.title("This is a title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.write("Welcome to my streamlit application built in Python")
    st.caption("This is a caption")

    st.code("""
    st.title("This is a title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.write("Welcome to my streamlit application built in Python")
    st.caption("This is a caption")
    a = 24
    b = 19
    st.write(f"{a} + {b} = {a + b}")
    """)

    with st.echo():
        st.write("This code is going to be executed")

    st.divider()
    # st.write("------------------------------")

    df = pd.read_csv("data.csv")
    st.dataframe(df)

    st.table(df.head())

    edited_df = st.data_editor(df)
    st.dataframe(edited_df)

    st.metric("Temperature in Degrees Celsius", 26, 2)

    st.metric("Rainfall in mm", 1400, -350)

    if st.button("Submit"):
        st.write("The button has been clicked")

    like_dislike = st.feedback()
    # st.write(like_dislike)
    if like_dislike == 0:
        st.write("You have disliked the content")
    elif like_dislike == 1:
        st.write("You have liked the content")

    stars = st.feedback("stars")
    if stars or stars == 0:
        if stars <= 1:
            st.write("Low Rating")
        elif stars == 2:
            st.write("Medium Rating")
        elif stars > 2:
            st.write("High Rating")

        activated = st.toggle("Activate")

        terms_conditions = st.checkbox("I have read the terms and conditions and agree to them")
        if terms_conditions:
            st.write("The user has agreed to the above terms and conditions")

        gender = st.radio("Select your Gender : ", ["Male", "Female", "Other"])
        if gender == "Male":
            st.write("The men's conference will be held on Saturday")
        elif gender == "Female":
            st.write("The girls' chat will be held on Friday")

    team = st.selectbox("Select your favourite team : ", ["Liverpool", "Arsenal", "Nottingham", "Chelsea"])
    breakfast = st.multiselect("What did you have for breakfast?", ["Eggs", "Tea", "Coffee", "Sausages", "Arrrow roots", "Milk", "Bacon", "Cereal"])

    size = st.select_slider("Select your cloth size : ", ["XS", "S", "M", "L", "XL", "2L", "3L"])

    st.number_input("Enter a number here :", 0, 10)

    st.slider("Enter your age here :", 18, 40, value=30 )

    date_set = st.date_input("Enter the appointment date : ")

    st.time_input("Enter the time you want to schedule the appointment : ")

    name = st.text_input("Enter your first name here : ")
    second_name = st.text_input("Enter your second name here : ")
    # st.write(f"Your name is {name} {second_name}")

    st.text_area("Write an essay on why you should be considered for the scholarship opportunity", height=180)

    st.file_uploader("Upload your dataset here : ")

    # st.camera_input("Take a photo of yourself")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("dog.jpg", width=200)
    with col2:
        st.image("dog.jpg", width=200)
    with col3:
        st.image("dog.jpg", width=200)



    trigger = st.selectbox("Select whether or not to have the dialog box", ["No", "Yes"])
    if trigger == "Yes":
        user_details()

    with st.expander("Click to see more details"):
        st.write("This is the first statement")
        st.write("This is the second statement")
        st.write("This is the third statement")
        st.write("This is the fourth statement")
        st.write("This is the fifth statement")

    # with st.sidebar:
    #     st.write("This is within the sidebar")

    # with st.spinner("Loading content"):
    #     time.sleep(5)
    #     st.write("The content has been loaded successfully")

    # # progress bar
    # for i in range(100):
    #     st.progress(i)
    #     time.sleep(0.1)

    # progress bar that fills and updates itself

    # progress_text = "Processing data"
    # my_bar = st.progress(0, text=progress_text)
    #
    # for percent_complete in range(100):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1, text=progress_text)
    # time.sleep(1)
    # my_bar.empty()

    st.toast("User signed up successfully", icon="👍")
    st.write("This is a laughing emoji :rolling_on_the_floor_laughing: :rolling_on_the_floor_laughing: :rolling_on_the_floor_laughing:")

    # st.balloons()

    # callout messages
    st.success("You have successfully logged in")
    st.info("Upload a .csv file")
    st.warning("The directory you are trying to save to does not exist")
    st.error("Failed to load the image")

if __name__ == "__main__":
    main()