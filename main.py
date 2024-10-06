import streamlit as st

from streamlit_option_menu import option_menu


import test, your,individual, subject

st.set_page_config(
        page_title="Student_Analysis",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar: 
            # st.image("./logo.png", width=150)
            
            st.markdown('<img class="logo" src="https://www.vcacs.ac.in/assets/images/logo/VIIT01.webp" alt="Custom Logo" style="height: 200px; position: absolute; align-item:center; top: -130px; left: 10px;z-index: 1;">', unsafe_allow_html=True)      
            app = option_menu(
                menu_title='MENU',
                options=['Account','Home','Subject','Uploads'],
                icons=['person-circle','chat-fill','person-circle','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'skyblue'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "black"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
            
        if app == "Account":
            test.app()  
           
        # if app == 'Home':
        #     your.app()
        
    
        if app == 'Subject':
            subject.app()
        

        if app == 'Uploads':
            individual.app()

             
    run()            
    
         
