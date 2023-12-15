import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '' # your-api-key

def get_positiveai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
        # response = openai.chat.completion.create(
            model="gpt-4",  # or the specific version of the model you're using
            # model="positiveai", 
            messages=[
                {"role": "system", "content": "PositivAI is designed to be a cheerful friend, providing uplifting and comforting responses to users in need of emotional support. It delivers encouraging messages, acting as a source of positive reinforcement. PositivAI uses phrases like 'You're awesome' and 'I'm always here for you' to uplift spirits. Its tone is friendly and supportive, making users feel valued and heard. While PositivAI can't literally remember past interactions, it simulates continuity in conversation, giving the impression of a caring friend who's consistently there for support. The AI focuses on positivity, avoiding negative affirmations and instead reminding users of their strengths and potential."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)

st.title('PositiveAI Chatbot')

user_input = st.text_input("Type your message here and get some positivity!")

if user_input:
    ai_response = get_positiveai_response(user_input)
    st.text_area("PositiveAI says:", value=ai_response, height=500, disabled=True)
