import streamlit as st

# Define the login page
def show_login():
    st.title("Login")
    login_method = st.radio("Choose a login method:", ("Phone Number", "Gmail Account"))

    if login_method == "Phone Number":
        phone_number = st.text_input("Enter your phone number:")
        if st.button("Login"):
            st.session_state.step = 'outfit_preferences'
            st.session_state.login_detail = phone_number
            st.experimental_rerun()
    else:
        gmail_account = st.text_input("Enter your Gmail account:")
        if st.button("Login"):
            st.session_state.step = 'outfit_preferences'
            st.session_state.login_detail = gmail_account
            st.experimental_rerun()

# Define the outfit preferences page
def show_outfit_preferences():
    st.title("Outfit Preferences")

    st.header("Choose your outfit preferences for different occasions:")
    occasion = st.selectbox("Select an occasion:", ["Casual", "Formal", "Party", "Sports"])
    color_scheme = st.color_picker("Pick a color scheme:")

    if st.button("Show Recommendations"):
        st.write(f"Here are some outfit recommendations for the {occasion} occasion in {color_scheme}:")
        st.image("https://via.placeholder.com/150", caption="Shirt Example")
        st.image("https://via.placeholder.com/150", caption="T-shirt Example")
        st.image("https://via.placeholder.com/150", caption="Shoes Example")
        st.image("https://via.placeholder.com/150", caption="Jewellery Example")

        st.header("Accessories")
        st.write("Related products:")
        st.image("https://via.placeholder.com/150", caption="Accessory 1")
        st.image("https://via.placeholder.com/150", caption="Accessory 2")

# Define the AiFit page
def show_aifit():
    st.title("AiFit - Create Your Outfit")

    uploaded_shirt = st.file_uploader("Upload your shirt:", type=['png', 'jpg', 'jpeg'])
    uploaded_tshirt = st.file_uploader("Upload your t-shirt:", type=['png', 'jpg', 'jpeg'])
    uploaded_shoes = st.file_uploader("Upload your shoes:", type=['png', 'jpg', 'jpeg'])
    uploaded_jewellery = st.file_uploader("Upload your jewellery:", type=['png', 'jpg', 'jpeg'])

    if st.button("Create Outfit"):
        if uploaded_shirt and uploaded_tshirt and uploaded_shoes and uploaded_jewellery:
            st.write("Here's your outfit:")
            st.image(uploaded_shirt, caption="Shirt")
            st.image(uploaded_tshirt, caption="T-shirt")
            st.image(uploaded_shoes, caption="Shoes")
            st.image(uploaded_jewellery, caption="Jewellery")
        else:
            st.error("Please upload all clothing items to create an outfit.")

        st.header("Accessories")
        st.write("Accessories that match with your clothing:")
        st.image("https://via.placeholder.com/150", caption="Accessory 1")
        st.image("https://via.placeholder.com/150", caption="Accessory 2")

# Main logic to display content based on the step
def main():
    if 'step' not in st.session_state:
        st.session_state.step = 'login'
    if 'login_detail' not in st.session_state:
        st.session_state.login_detail = ''

    if st.session_state.step == 'login':
        show_login()
    elif st.session_state.step == 'outfit_preferences':
        show_outfit_preferences()
    elif st.session_state.step == 'aifit':
        show_aifit()

    if st.session_state.step != 'login':
        st.sidebar.title("Menu")
        selection = st.sidebar.radio("Go to:", ["Outfit Preferences", "AiFit"])
        if selection == "Outfit Preferences":
            st.session_state.step = 'outfit_preferences'
        elif selection == "AiFit":
            st.session_state.step = 'aifit'
        st.experimental_rerun()

if __name__ == "__main__":
    main()
