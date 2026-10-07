import os

import streamlit as st

from gtts import gTTS
from streamlit_mic_recorder import speech_to_text

from src.ai_skin_specialist.analyzer import analyze_skin

st.set_page_config(
    page_title="AI Skin Specialist",
    page_icon="🧴",
    layout="centered",
)

def load_css():
    with open("styles.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.header("🧴 Skin Specialist")

    st.write("Choose your skin concern:")

    skin_concern = st.selectbox(
        "Skin concern",
        [
            "General skincare",
            "Oily skin",
            "Dry skin",
            "Acne / Pimples",
            "Pigmentation",
            "Dark spots",
            "Sensitive skin",
            "Redness",
            "Anti-aging",
        ],
    )

    st.divider()

    st.subheader("⚕️ Important")

    st.caption(
        "This AI provides general skincare information "
        "and is not a substitute for professional medical advice."
    )


# -----------------------------
# CHAT HISTORY
# -----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.markdown(
    """
    <div class="hero-card">
        <div class="hero-icon">🧴</div>
        <h1>AI Skin Specialist</h1>
        <p>Your personal AI-powered skincare assistant</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    ### 🌸 How can I help you?

    You can:
    - 💬 Ask a skincare question
    - 🎤 Ask using your voice
    - 📸 Upload a skin image
    - 🤖 Get AI-powered skincare guidance
    - 🔊 Listen to the AI response
    """
)

st.info(
    "⚠️ This is an AI-assisted skincare tool and does not "
    "provide a medical diagnosis."
)

# -----------------------------
# CLEAR CHAT
# -----------------------------

if st.session_state.chat_history:

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()


# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------

if st.session_state.chat_history:

    st.divider()
    st.subheader("💬 Conversation")

    for chat in st.session_state.chat_history:

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.write(chat["answer"])


# -----------------------------
# TEXT INPUT
# -----------------------------

st.markdown(
    """
    <div class="section-card">
        <h3>💬 Ask a question</h3>
        <p>Type your skincare question below.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


user_text = st.text_input(
    "Type your question",
    placeholder="Example: What is a good skincare routine for oily skin?",
)


# -----------------------------
# VOICE INPUT
# -----------------------------

st.markdown(
    """
    <div class="section-card">
        <h3>🎤 Ask using your voice</h3>
        <p>Speak naturally and let the AI understand your question.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


voice_text = speech_to_text(
    language="en",
    start_prompt="🎤 Start recording",
    stop_prompt="⏹️ Stop recording",
    just_once=True,
    use_container_width=True,
    key="voice_input",
)

if voice_text:
    st.success(f"You said: {voice_text}")
    user_text = voice_text


# -----------------------------
# IMAGE INPUT
# -----------------------------

st.divider()

st.markdown(
    """
    <div class="section-card">
        <h3>📸 Skin image</h3>
        <p>Upload an image if you want visual skin analysis.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


uploaded_file = st.file_uploader(
    "Upload a skin image if you want visual analysis",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded skin image",
        use_container_width=True,
    )


# -----------------------------
# AI RESPONSE
# -----------------------------

st.divider()

if st.button(
    "🤖 Get AI Response",
    use_container_width=True,
):

    if not user_text and uploaded_file is None:

        st.error(
            "Please ask a question or upload a skin image."
        )

    else:

        temp_image_path = None

        try:

            if uploaded_file is not None:

                temp_image_path = "uploaded_skin_image.jpg"

                with open(temp_image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

            with st.spinner("AI is thinking..."):

                question_with_concern = f"""
                User's selected skin concern: {skin_concern}

                User's question:
                {user_text if user_text else "Please analyze the uploaded skin image."}
                """

                result = analyze_skin(
                    image_path=temp_image_path,
                    user_question=question_with_concern,
                )


            # -----------------------------
            # TEXT RESPONSE
            # -----------------------------

            st.subheader("🤖 AI Response")

            st.write(result)

            st.session_state.chat_history.append(
                {
                    "question": user_text if user_text else "Skin image analysis",
                    "answer": result,
                }
            )


            # -----------------------------
            # AUDIO RESPONSE
            # -----------------------------

            st.subheader("🔊 AI Voice Response")

            audio_file = "ai_response.mp3"

            tts = gTTS(
                text=result,
                lang="en",
            )

            tts.save(audio_file)

            with open(audio_file, "rb") as audio:

                st.audio(
                    audio.read(),
                    format="audio/mp3",
                )

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )

        finally:

            if (
                temp_image_path
                and os.path.exists(temp_image_path)
            ):
                os.remove(temp_image_path)
