📈 Multi-Agent Stock Analysis with Streamlit
-----
🚀 AI-driven stock insights using multiple intelligent agents & Streamlit UI!

Overview
This project leverages multi-agent intelligence powered by Groq API and Llama model to analyze stock data and provide investment recommendations.

💡 Tech Stack:
-
✅ Python
✅ Groq API (Llama Model)
✅ Streamlit (for interactive UI)

The system consists of three agents:
-
1️⃣ Stock Agent – Fetches real-time stock prices 📊
2️⃣ Company Lookup Agent – Retrieves company details & financial insights 🏢
3️⃣ Finance Agent – Analyzes trends & suggests whether to Buy / Hold / Sell 💡

🔹 Recent Run Results
-
Stock	Price	Recommendation
Apple (AAPL)	$213.49	✅ BUY
Tesla (TSLA)	$XXX.XX	✅ BUY

🛠️ Installation & Setup
1️⃣ Prerequisites
Ensure you have Python installed along with the following libraries:
pip install requests pandas groq python-dotenv streamlit


2️⃣ Setup API Key

----------------------------------------------------------------------------------

1️⃣ Create a .env file in the project root and paste your Groq API Key inside:
GROQ_API_KEY=your_api_key_here


2️⃣ Load the environment variables in your script using dotenv:

python
------
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
🎯 Running the Project
1️⃣ Clone the Repository and 


2️⃣ Run the Streamlit App
---->streamlit run app.py
This will launch an interactive web app where you can enter a stock ticker and get real-time recommendations!

🌟 Features
✅ Real-time stock price fetching
✅ AI-powered stock recommendations using Groq's Llama Model
✅ Interactive UI with Streamlit
✅ Support for multiple stocks
✅ Easy-to-use interface for financial analysis

🚀 Future Enhancements
✅ Sentiment analysis integration
✅ More financial indicators
✅ Cloud deployment for live tracking

📌 Let's connect! If you have ideas to enhance this project, feel free to contribute!

#AI #Finance #Groq #Llama #MultiAgentSystems #StockMarket #Python #Streamlit #MachineLearning
