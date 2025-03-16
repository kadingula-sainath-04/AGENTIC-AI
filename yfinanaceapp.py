import streamlit as st
import time
import random
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# Load API keys
load_dotenv()

# Function to get stock symbols
def lookup_company_symbol(company: str) -> str:
    symbols = {"Infosys": "INFY",
               "Tesla": "TSLA",
               "Apple": "AAPL",
               "Microsoft": "MSFT",
               "Amazon": "AMZN",
               "Google": "GOOGL"}
    return symbols.get(company, "Unknown")

# Stock Data Agent
stock_agent = Agent(
    name="Stock Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Fetch stock prices, fundamentals, and analyst recommendations."],
)

# Company Lookup Agent
company_lookup_agent = Agent(
    name="Company Lookup Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[lookup_company_symbol],
    instructions=["Find stock symbols for companies based on their names."],
)

# Main Finance Team Agent
finance_team = Agent(
    name="Finance Team",
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[stock_agent, company_lookup_agent],
    instructions=["Fetch stock data and company symbols together."],
)

# Function to handle API rate limits and retries
def run_with_retry(agent, query, retries=3, delay=10):
    for attempt in range(retries):
        try:
            response = agent.run(query)
            return response
        except Exception as e:
            st.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                wait_time = random.uniform(delay, delay + 5)
                st.warning(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                st.error("Max retries reached. Could not complete the request.")
                return None

# Streamlit UI
st.title("📈 Stock Market AI Assistant")
st.write("Get real-time stock prices, fundamentals, and analyst recommendations.")

company_name = st.text_input("Enter company name (e.g., Apple, Tesla, Google)")

if st.button("Get Stock Data"):
    if company_name:
        symbol = lookup_company_symbol(company_name)
        if symbol == "Unknown":
            st.error("Company symbol not found. Try another company.")
        else:
            st.success(f"Fetching data for {company_name} ({symbol})...")
            response = run_with_retry(finance_team, f"Get stock data for {company_name}")
            if response:
                st.write(response)
    else:
        st.warning("Please enter a company name.")


