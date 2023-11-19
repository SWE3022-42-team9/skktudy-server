# skktudy AI Chatbot

## Quickstart 
### Setup `python` environment
```
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```
### Add OpenAI API key
```
Go to https://platform.openai.com/account/api-keys.
Click on the + Create new secret key button.
Next, enter an identifier name (optional) and click on the Create secret key button.
At root directory, add `.env` file with content OPENAI_API_KEY="key"
```

### Run Streamlit
```
streamlit run src/app.py
```

## Repository Structure
``` bash
.
├── .venv
├── .vscode
├── src
│   ├── app.py                  # Main streamlit app
│   ├── chatbot.py              # Main chatbot class
│   ├── output_parsers.py
│   └── templates.py
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

