import streamlit as st
import random
import time

# pg cnfgr
st.set_page_config(
    page_title="Serenity - Mind Mingle AI",
    page_icon="🌿",
    layout="wide"
)


# custom styling
st.markdown("""
<style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
    }
    .main-header {
        font-size: 2.5rem;
        color: #2E8B57;
        text-align: center;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)




#demo ai response irl we'll connect it to an api
def get_bot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "sad": [
            "I'm sorry to hear that you're feeling sad. It's okay to feel this way sometimes. Do you want to talk about what's making you feel down?",
            "Sending you a virtual hug. 🌿 Remember, storms don't last forever. What can I do to help right now?",
        ],
        "stress": [
            "Stress can be overwhelming. Have you tried taking a deep breath? Let's try the 4-7-8 breathing technique together.",
            "Take a moment for yourself. You are doing the best you can. What is the biggest thing on your mind right now?",
        ],
        "anxious": [
            "Anxiety is tough, but you are tougher. Focus on your breathing. In... and out...",
            "Grounding can help. Can you tell me 3 things you see around you right now?",
        ],
        "happy": [
            "That is wonderful to hear! I'm so glad you're feeling good. What made your day special?",
            "Happiness looks good on you! Keep holding onto that positive energy. ☀️",
        ],
        "hello": [
            "Hello there! I'm Serenity. I'm here to listen and support you. How are you feeling today?",
            "Hi! Welcome to your safe space. How can I help you today?",
        ],
        "help": [
            "I am here to listen, but I am an AI. If you are in a crisis, please reach out to a professional or a helpline immediately.",
        ]
    }

    # checking keywords
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Default response
    return "I hear you. Thank you for sharing that with me. Tell me more about how you're feeling."



with st.sidebar:
    st.title("🌿 Serenity Control")
    st.markdown("---")

    st.subheader("Daily Mood Check-in")
    mood = st.select_slider(
        "How are you feeling right now?",
        options=["Stressed", "Anxious", "Neutral", "Good", "Great"]
    )

    if mood in ["Stressed", "Anxious"]:
        st.warning("Take a deep breath. You've got this.")
    elif mood in ["Good", "Great"]:
        st.success("Glad to see you shining!")
    else:
        st.info("Stay balanced.")

    st.markdown("---")
    st.subheader("Quick Resources")
    st.write(
        "• [Breathing Exercises](https://www.webmd.com/balance/stress-management/stress-relief-breathing-techniques)")
    st.write("• [Mindfulness Tips](https://www.mindful.org/)")
    st.write("• [Mental Health Assistance](https://www.nami.org/)")

    st.markdown("---")
    st.caption("Mind Mingle AI Project")


st.markdown('<div class="main-header">🌿 Serenity</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your Mental Health Companion powered by Mind Mingle AI</div>',
            unsafe_allow_html=True)

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hello! I'm Serenity. I'm here to provide a safe space for you to share your thoughts. How are you feeling today?"}
    ]

# display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# prompting area
if prompt := st.chat_input("Type your message here..."):
    # 1. Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # delayed
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)  # Delay for effect
            response = get_bot_response(prompt)
            st.write(response)

    #Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})