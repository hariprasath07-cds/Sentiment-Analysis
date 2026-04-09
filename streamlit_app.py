import streamlit as st
import requests

#page config
st.set_page_config(
    page_title="sentiment analysis",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Enter a movie review and get instant sentiment prediction!")

#input box
review = st.text_area("Enter your movie review here:",height=150)

#predict button
if st.button("Analyze Statement"):
    if review.strip() == "":
        st.warning("please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            # Call your Flask backend
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"reviews": review}
            )
            result = response.json()

            #Display result
            sentiment = result['prediction']
            #confidence = result['confidence']

            if "pos" in sentiment or "neg" in sentiment:
                st.success(f"sentiment : {sentiment}")
            else:
                st.error(f"sentiment : {sentiment}")

            # st.metric(label="confidence",value = confidence)    
                