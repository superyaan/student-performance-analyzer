import streamlit as st
import firebase_admin
from firebase_admin import credentials



if not firebase_admin._apps:
    # Initialize Firebase SDK
    cred = credentials.Certificate("viit-38a0b-5d9d4ab2ee01.json")
    firebase_admin.initialize_app(cred)




from firebase_admin import firestore

from firebase_admin import auth


def app():
# Usernm = []
    
    centered_style = """
        <style>
        .centered-title {
            text-align: center;
            white-space: nowrap; /* Prevent line breaks */
            
        }
        .centered-title h1 {
            line-height: 0.8em; /* Adjust line height */
            margin: 0; /* Remove any default margins */
        }
        </style>
    """
    st.markdown(centered_style, unsafe_allow_html=True)
    st.markdown("<div class='centered-title'><h1>VISHWAKARMA INSTITUTE OF  </h1><h1>INFORMATION TECHNOLOGY</h1></div>", unsafe_allow_html=True)    
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ""



    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        

        
        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password,uid=username)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            # st.button('Login', on_click=f)          
            st.button('Login', on_click=f)
            
            
    if st.session_state.signout:
                st.text('Name '+st.session_state.username)
                st.text('Email id: '+st.session_state.useremail)
                st.button('Sign out', on_click=t) 
            
                
    

                            
    def ap():
        st.write('Posts')
