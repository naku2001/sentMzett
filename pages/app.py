import streamlit as st
from textblob import TextBlob
from streamlit_extras.let_it_rain import rain

st.title('Sentiment Analysis Supermarket Products System')

message = st.text_area("Text")

if st.button("Analyze the Sentiment"): 
  blob = TextBlob(message) 
  result = blob.sentiment 
  polarity = result.polarity 
  subjectivity = result.subjectivity 
  if polarity < 0: 
    st.warning("The entered text has negative sentiments associated with it"+str(polarity)) 
#     rain( 
#     emoji="????", 
#     font_size=20,  # the size of emoji 
#     falling_speed=3,  # speed of raining 
#     animation_length="infinite",  # for how much time the animation will happen 
# ) 
  if polarity >= 0: 
    st.success("The entered text has positive sentiments associated with it."+str(polarity)) 
    # rain( 
    # emoji="????", 
    # font_size=20,  # the size of emoji 
    # falling_speed=3,  # speed of raining 
    # animation_length="infinite",  # for how much time the animation will happen 
    # ) 
  st.success(result)