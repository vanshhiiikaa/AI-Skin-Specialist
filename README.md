🧴 AI Skin Specialist

An AI-powered skincare assistant built with Python and Streamlit that provides personalized skincare guidance through text, voice, and skin-image inputs.

The application combines AI-powered analysis with an interactive web interface to help users explore common skincare concerns such as acne, oily skin, dryness, pigmentation, dark spots, sensitivity, redness, and anti-aging.

⚠️ Disclaimer: AI Skin Specialist is an informational skincare assistant. It does not provide medical diagnoses or replace advice from a qualified dermatologist or healthcare professional.
✨ Features
💬 AI Skincare Chat — Ask questions about skincare and receive AI-generated guidance.
🎤 Voice Input — Ask questions using your microphone.
📸 Skin Image Analysis — Upload a JPG, JPEG, or PNG image for AI-assisted visual analysis.
🧴 Skin Concern Selection — Choose from:
General skincare
Oily skin
Dry skin
Acne / Pimples
Pigmentation
Dark spots
Sensitive skin
Redness
Anti-aging
🤖 AI-Powered Responses — Get responses based on your selected concern and question.
💬 Conversation History — Review the current conversation during your session.
🔊 AI Voice Responses — Listen to generated skincare responses using text-to-speech.
🎨 Custom UI — Styled Streamlit interface with custom CSS.
🔐 Environment Variables — API credentials can be stored securely in .env rather than committed to the repository.
🛠️ Tech Stack
Python 3.13+
Streamlit — Web application interface
Google GenAI — AI-powered analysis
Anthropic — AI integration
gTTS — Text-to-speech responses
Streamlit Mic Recorder — Voice input
python-dotenv — Environment variable management

The project dependencies and Python version are defined in pyproject.toml. 
G
GitHub

📁 Project Structure
AI-Skin-Specialist/
│
├── Images/
│   └── Project images and assets
│
├── src/
│   └── ai_skin_specialist/
│       ├── __init__.py
│       └── analyzer.py
│
├── app.py
├── doct.brain.py
├── styles.css
├── test_gemini.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/vanshhiiikaa/AI-Skin-Specialist.git
cd AI-Skin-Specialist

2. Create a virtual environment
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

Using pip:

pip install -r requirements.txt


If you are using the project's pyproject.toml / uv.lock workflow, install the project dependencies with your preferred uv workflow.

🔑 Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key


Use the variable names expected by your local analyzer configuration.

⚠️ Security

Never commit .env to GitHub.

Your .gitignore should contain:

.env
venv/
__pycache__/
*.pyc


If an API key is accidentally committed, revoke/rotate it immediately and remove the secret from Git history.

🚀 Run the Application

Start Streamlit with:

streamlit run app.py


The application will open in your browser.

You can then:

Select a skin concern.
Type a skincare question or use voice input.
Optionally upload a skin image.
Click Get AI Response.
Review the AI-generated guidance.
Listen to the response using the audio player.

The current application implements text input, microphone input, image upload, AI analysis, chat history, and text-to-speech output directly in app.py. 
G
GitHub
+1

🧠 How It Works
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
           Text Input   Voice Input   Skin Image
                │            │            │
                └────────────┼────────────┘
                             ▼
                  ┌─────────────────────┐
                  │  Selected Concern   │
                  └──────────┬──────────┘
                             ▼
                  ┌─────────────────────┐
                  │   AI Skin Analyzer  │
                  └──────────┬──────────┘
                             ▼
                  ┌─────────────────────┐
                  │   AI Response       │
                  └──────────┬──────────┘
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
            Text Response         Voice Response

💡 Example Questions

You can ask questions such as:

"What is a good skincare routine for oily skin?"
"How can I reduce the appearance of dark spots?"
"What skincare routine is suitable for dry skin?"
"What ingredients are commonly used for acne-prone skin?"
"How should I care for sensitive skin?"
"What can I do about facial redness?"
🖥️ Application Interface

The application provides a dedicated skincare interface with a sidebar for selecting skin concerns, a chat area, voice input, image upload, AI responses, and audio playback. 
G
GitHub
+1

⚕️ Medical Disclaimer

AI Skin Specialist is designed for educational and informational purposes only.

It should not be used to:

Diagnose a medical condition.
Replace professional dermatological advice.
Recommend prescription medication without professional guidance.
Make emergency medical decisions.

If you have a persistent, severe, painful, rapidly changing, or concerning skin condition, consult a qualified dermatologist or healthcare professional.

🔒 Privacy & Security
Do not upload sensitive personal information.
Do not store API keys directly in source code.
Keep .env excluded from version control.
Treat uploaded skin images as sensitive personal data.
Use API credentials responsibly and rotate them if exposed.
🧪 Testing

The repository includes a Gemini-related test file:

python test_gemini.py


Make sure your required API credentials are configured before running API-dependent tests.

🔮 Future Improvements

Potential future enhancements include:

📊 Skin-health tracking over time
🧴 Personalized skincare routine generation
🛍️ Product recommendation system
📱 Mobile-friendly interface
🌐 Multi-language voice support
🧑‍⚕️ Dermatologist consultation integration
📈 User progress dashboard
🔐 Improved privacy controls
🧠 More advanced image-based skin analysis
☁️ Cloud deployment
🤝 Contributing

Contributions are welcome!

Fork the repository.
Create a feature branch:
git checkout -b feature/your-feature

Make your changes.
Commit your changes:
git add .
git commit -m "Add your feature"

Push the branch:
git push origin feature/your-feature

Open a Pull Request.
📄 License

This project is currently available for educational and development purposes.

Add an explicit open-source license such as MIT if you want others to reuse, modify, and distribute the project under defined terms.

👩‍💻 Author

Vanshika

GitHub:
https://github.com/vanshhiiikaa

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

AI Skin Specialist — Making skincare guidance more accessible with AI. 🧴🤖
