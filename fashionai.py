import streamlit as st

# Step 1: Login Page
def login_page():
    st.title("Login")
    login_method = st.radio("Choose a login method:", ("Phone Number", "Gmail Account"))
    
    if login_method == "Phone Number":
        phone_number = st.text_input("Enter your phone number:")
        if st.button("Login"):
            st.success(f"Logged in with phone number: {phone_number}")
            st.session_state['logged_in'] = True
    else:
        gmail_account = st.text_input("Enter your Gmail account:")
        if st.button("Login"):
            st.success(f"Logged in with Gmail: {gmail_account}")
            st.session_state['logged_in'] = True

# Step 2: Outfit Preferences
def outfit_preferences():
    st.title("Outfit Preferences")
    
    st.header("Choose your outfit preferences for different occasions:")
    occasion = st.selectbox("Select an occasion:", ["Casual", "Formal", "Party", "Sports"])
    color_scheme = st.color_picker("Pick a color scheme:")
    
    if st.button("Show Recommendations"):
        st.write(f"Here are some outfit recommendations for {occasion} occasion in {color_scheme}:")
        st.image("https://via.placeholder.com/150", caption="Outfit 1")
        st.image("https://via.placeholder.com/150", caption="Outfit 2")
        
        st.header("Advertisements")
        st.write("Related products:")
        st.image("https://via.placeholder.com/150", caption="Ad 1")
        st.image("https://via.placeholder.com/150", caption="Ad 2")

# Step 3: AiFit - Outfit Generator
def aifit():
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
        
        st.header("Advertisements")
        st.write("Related products:")
        st.image("https://via.placeholder.com/150", caption="Ad 1")
        st.image("https://via.placeholder.com/150", caption="Ad 2")

# Main App Logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login_page()
else:
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Go to:", ["Outfit Preferences", "AiFit"])
    
    if selection == "Outfit Preferences":
        outfit_preferences()
    elif selection == "AiFit":
        aifit()
