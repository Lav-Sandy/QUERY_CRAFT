import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import pandas as pd
from PIL import Image
import sqlite3


load_dotenv()

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def headerlayout():
    
    my_logo2 = add_logo(logo_path=r"C:\Users\91897\OneDrive\Documents\GENAI.jpg", width=100, height=100)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.write(" ")
    with col3:
        st.image(my_logo2)


# Web App Title
    st.markdown("<h1 style = 'text-align:center; color: Black;font-size:50px;'>📊 DataGPT</h1>", unsafe_allow_html = True)
    
    st.markdown (""" **_Your AI-Powered Data Intelligence Platform_ <br>**
                 Effortlessly convert natural language questions into SQL queries and analyze your data with AI-driven insights.  <br> <br>
                 <b>Features:</b> <br>
                 🔍 <b>SQLite Query Generator</b> - Ask questions about your database in plain English<br>
                 📈 <b>Smart Data Analyzer</b> - Upload CSVs and get intelligent insights from your data<br>
                 🤖 <b>Powered by Google Gemini</b> - Advanced AI language models for accurate results<br>
                """,True)
                

def openai_chat_interface():
    st.title("🔍 SQL Query Generator")
    st.markdown("*Ask questions about your database in plain English*")
    st.markdown("*Convert Your Questions to SQL Queries Instantly*")

    def get_gemini_response(question, db_schema):
        """Convert English questions to SQL query using Gemini"""
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
        
        prompt = f"""You are an expert in converting English questions to SQL queries!
        
Database Schema:
{db_schema}

Important: 
- Return ONLY the SQL query, no markdown formatting or backticks
- Do NOT include the word "sql" in the output
- Make the query compatible with SQLite
- If you can't generate a query, explain why

Question: {question}
SQL Query:"""
        
        response = model.invoke(prompt)
        return response.content.strip()

    def read_sql_query(sql, db):
        """Retrieve results from the database"""
        try:
            conn = sqlite3.connect(db)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            return rows
        except Exception as e:
            return f"Error executing query: {str(e)}"

    def get_db_schema(db_path):
        """Get the schema of the SQLite database"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        schema = ""
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            schema += f"Table: {table_name}\n"
            for col in columns:
                schema += f"  - {col[1]} ({col[2]})\n"
            schema += "\n"
        
        conn.close()
        return schema

    question = st.text_input("Input: ", key="input", placeholder="Ask a question about your student database...")
    submit = st.button("Ask the Question", use_container_width=True)

    if submit and question:
        try:
            # Get database schema
            db_schema = get_db_schema("student.db")
            
            # Get the SQL query from Gemini
            sql_query = get_gemini_response(question, db_schema)
            
            # Display the generated SQL query
            st.subheader("Generated SQL Query:")
            st.code(sql_query, language="sql")
            
            # Execute the query
            response = read_sql_query(sql_query, "student.db")
            
            # Display results
            st.subheader("The Response Is:")
            if isinstance(response, str):  # Error message
                st.error(response)
            elif response:  # Results found
                for row in response:
                    st.write(row)
            else:
                st.info("No results found.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
 
def Ollama():
    # Using Google Gemini API for data analysis
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

    st.title("📊 Smart Data Analyzer")
    st.markdown("*Upload your CSV files and let AI analyze them for you*")

    uploader_file = st.file_uploader("Upload a CSV file", type= ["csv"])

    if uploader_file is not None:
        data = pd.read_csv(uploader_file)
        st.write(data.head(3))
        prompt = st.text_area("Enter your prompt about the data:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    # Create a summary instead of sending entire dataframe
                    summary = f"""
Rows: {len(data)}
Columns: {len(data.columns)}

Columns:
{list(data.columns)}

Sample (first 20 rows):
{data.head(20).to_string()}

Statistics:
{data.describe().to_string()}
"""
                    full_prompt = f"Here is a summary of the dataframe:\n{summary}\n\nUser Question: {prompt}"
                    response = llm.invoke(full_prompt)
                    st.write(response.content)
            else:
                st.warning("Please enter a prompt!")

def DEFAULT_VALUE():
    DEFAULT = '🏠 Home'
    return DEFAULT 
 
page_names_to_funcs = {
    "🏠 Home" : headerlayout,
    "🔍 Query Generator" : openai_chat_interface,
    "📊 Data Analyzer" : Ollama,

   }    
   
selected_page = st.sidebar.selectbox("🚀 Choose a Feature", page_names_to_funcs.keys())

    
if selected_page == "Home":    
    headerlayout()
else:
    page_names_to_funcs[selected_page]()  