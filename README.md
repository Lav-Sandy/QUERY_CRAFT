# 📊 Query Craft

Convert natural language questions into SQL queries and execute them instantly on your SQLite database using Google Gemini AI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-yellow.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue.svg)

## 🎯 Features

- **🤖 AI-Powered Query Generation** - Ask questions in English, get SQL queries automatically
- **💾 SQLite Integration** - Works seamlessly with SQLite databases
- **📈 Data Analysis** - Upload CSV files and analyze them with AI
- **🎨 Beautiful UI** - Clean, intuitive Streamlit interface
- **🔒 Secure** - No API costs (free Google Gemini API)
- **⚡ Fast Execution** - Instant query execution and results display

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- Google API Key (Free)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Lav-Sandy/QUERY_CRAFT.git
cd QUERY_CRAFT
```

2. **Create virtual environment:**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate  # macOS/Linux
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

Get your free API key from: [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Run the app:**
```bash
streamlit run GenAI.py
```

The app will open at `http://localhost:8501`

## 📖 Usage

### Query Craft Tab
1. Select **"SQLite Chat"** from the sidebar
2. Ask a question about your student database:
   - "How many students are enrolled?"
   - "Show all students in the Data Science class"
   - "Who are the top 5 students by grades?"
3. The AI generates SQL automatically
4. View the generated query and results

### Data Analysis Tab
1. Select **"Data Analysis"** from the sidebar
2. Upload a CSV file
3. Ask questions about your data
4. Get AI-generated insights

## 📁 Project Structure

```
QUERY_CRAFT/
├── GenAI.py              # Main Streamlit application
├── Sqlite.py             # SQLite database utilities
├── ask_csv.py            # CSV analysis helper
├── student.db            # Sample SQLite database
├── .env                  # Environment variables (git ignored)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🛠️ Technologies Used

- **Streamlit** - Web framework for data apps
- **Google Gemini API** - AI for query generation
- **LangChain** - LLM integration framework
- **SQLite** - Embedded database
- **Pandas** - Data manipulation

## 🔐 Security

- ✅ `.env` file is git-ignored (your API keys are safe)
- ✅ No sensitive data is exposed
- ✅ SQL queries are validated before execution
- ✅ All API communication is encrypted

## 💡 Example Queries

**Database Schema:**
```
Table: STUDENT
  - id (INTEGER)
  - NAME (TEXT)
  - CLASS (TEXT)
  - SECTION (TEXT)
  - MARKS (REAL)
```

**Example Questions:**
- "Count total students"
- "Show students from class Data Science"
- "List students with marks > 80"
- "Which section has the most students?"

## 📊 Free Tier Limitations

Google Gemini free tier includes:
- 60 requests per minute
- Unlimited daily usage (fair use policy)
- Perfect for personal/educational projects

## 🐛 Troubleshooting

**Issue: "GOOGLE_API_KEY is not set"**
- Make sure your `.env` file has the correct API key
- Run `pip install python-dotenv`

**Issue: "Database file not found"**
- Ensure `student.db` is in the project root
- Or modify the database path in code

**Issue: Query execution failed**
- Check your database schema matches the prompt
- Ensure SQLite is properly installed

## 🤝 Contributing

Feel free to fork and submit pull requests!

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Lav Sandy**
- GitHub: [@Lav-Sandy](https://github.com/Lav-Sandy)
- Email: lav.sandy30@gmail.com

## 🌟 Show Your Support

Give a ⭐ if you found this project helpful!

---

**Made with ❤️ using Google Gemini AI and Streamlit**
