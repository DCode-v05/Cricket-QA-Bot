# Cricket QA Bot

## Project Description
The Cricket QA Bot is an AI-powered application designed to answer questions related to the sport of cricket. By leveraging the power of Google's Gemini-2.0-flash model and the LangChain framework, this tool processes a comprehensive knowledge base about cricket—covering rules, formats, player roles, and tournaments—to provide accurate, context-aware responses to user queries.

---

## Project Details

### Problem Statement
Finding specific, accurate information about cricket rules, formats (Test, ODI, T20), or player roles can sometimes be time-consuming when sifting through vast amounts of general web content. This project provides a focused solution that extracts relevant answers directly from a curated document, ensuring users get precise information instantly.

### Key Components
- **Knowledge Base:** Uses a structured text document containing essential cricket facts, including:
  - Game mechanics (batting, bowling, scoring).
  - Match formats (Test, ODI, T20).
  - Player roles (Batsman, Bowler, All-rounder, Wicketkeeper).
  - Major tournaments (ICC World Cups, IPL, BBL).
- **LangChain Integration:** Utilizes `LangChain` to manage the flow of data from the document to the LLM.
- **Model**: Powered by `Google Generative AI` (Gemini-2.0-flash) for high-quality natural language understanding and generation.
- **Prompt Engineering**: Employment of a specific `ChatPromptTemplate` to strictly ground the model's answers in the provided context, minimizing hallucinations.

### Workflow
1.  **Document Loading**: The raw text data serves as the context.
2.  **Chain Execution**: A `stuff_chain` processes the input question and context.
3.  **Generation**: The model generates an answer based *only* on the context provided.
4.  **Output**: The answer is parsed and displayed to the user.

---

## Tech Stack
- **Languages:** Python 3.x
- **Frameworks:** LangChain
- **AI Models:** Google Gemini (gemini-2.0-flash)
- **Utilities:** python-dotenv (for environment variable management)

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/DCode-v05/Cricket-QA-Bot.git
cd Cricket-QA-Bot
```

### 2. Install dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Application
Execute the main script to see the bot in action:
```bash
python app.py
```

---

## Usage
- The application currently answers a predefined set of questions to demonstrate its capabilities, such as:
  - "What are the different formats of cricket?"
  - "Who are some famous cricket players mentioned in the document?"
  - "What is the role of a bowler in cricket?"
- You can modify the `questions` list in `app.py` to ask different questions based on the provided context.

---

## Project Structure
```
Cricket QA Bot/
│
├── app.py                  # Main application script with logic and context
├── requirements.txt        # Python dependencies
├── Readme.pdf              # Additional project documentation/reference
├── Output/                 # Directory for output artifacts
└── README.md               # Project documentation
```

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request describing your changes.

---

## Contact
- **GitHub:** [DCode-v05](https://github.com/DCode-v05)
- **Email:** denistanb05@gmail.com
