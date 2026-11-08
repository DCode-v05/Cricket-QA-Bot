# Cricket QA Bot

A short LangChain script that answers cricket questions using only a fixed block of text, so the model can't pull in facts from anywhere else. I wrote it to get used to LangChain Expression Language and prompt-based grounding.

## How it works

Everything is in `app.py`:

1. `cricket_document_data` is a hand-written passage covering the basics of the game, the Test/ODI/T20 formats, player roles, major tournaments (World Cup, T20 World Cup, IPL, BBL) and a few scoring rules. It is wrapped in a LangChain `Document`.
2. The model is `ChatGoogleGenerativeAI` with `models/gemini-2.0-flash` at `temperature=0`. The key comes from `GEMINI_API_KEY`.
3. A `ChatPromptTemplate` puts the context in the system message ("Answer the question using only the provided context") and the question in the human message.
4. The chain is `{context, input} | qa_prompt | model | StrOutputParser()`. The whole document goes into the prompt on each call, which is fine because it is short. There is no retrieval step.
5. At the bottom the script runs five questions and prints each `Q:` and `A:`.

![Sample output](Output/Output.png)

## Setup

```bash
pip install -r requirements.txt
```

Create `.env` with `GEMINI_API_KEY=your_key` (a key from Google AI Studio), then:

```bash
python app.py
```

To ask something else, edit the `questions` list. To change what the bot knows, edit `cricket_document_data`.

## Limitations

The model is only told to stay within the context. Nothing checks that it does. The knowledge base is one short passage, and it names a few players but has no stats.
