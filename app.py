
import streamlit as st
from predpage import show_predpage
from explorepage import show_explorepage
# from Notes import show_Notes


# page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore", "Notes"))

# if page == "Predict":
#     show_predpage()
# elif page == "Notes":
#     show_Notes()
# else:
#     show_explorepage()


page = st.sidebar.selectbox("Menu", ("Predict", "Explore"))

if page == "Predict":
    show_predpage()
else:
    show_explorepage()




# import streamlit as st
# from predpage import show_predpage
# from explorepage import show_explorepage
# from Notes import show_Notes

# page = st.sidebar.selectbox("Menu", ("Predict", "Explore", "Notes"))

# if page == "Predict":
#     show_predpage()
# elif page == "Notes":
#     show_Notes()
# else:
#     show_explorepage()



