# InquisiAI: Your Research Assistant

InquisiAI is a research-focused conversational assistant built using **LangChain**, **Streamlit**, and **Groq LLaMA 3**. It empowers users—especially students, researchers, and academics—to ask deep scholarly questions and get responses synthesized from **Arxiv**, **Wikipedia**, and the open web.

![InquisiAI UI](https://github.com/ayeshamafrah-design/inquisi-ai/blob/main/inquisi.png)

---

## 🎯 Key Features

- 🧠 **Academic Search Mode**: Toggle to focus only on scholarly sources (Arxiv + Wikipedia).
- 🔍 **Live Search Support**: Retrieves real-time data using DuckDuckGo (if enabled).
- 📚 **Chat Interface**: Interactive chat history with memory.
- 💬 **Groq LLaMA 3 Integration**: Uses LLaMA 3 model via Groq API for low-latency responses.
- ✅ **Streamlit UI**: Clean and intuitive interface for research exploration.

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayeshamafrah-design/inquisi-ai.git
   cd inquisi-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Groq API key**
   - Create a `.env` file and add:
     ```
     GROQ_API_KEY=your_key_here
     ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---


## 📄 Dependencies

- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq LLaMA 3](https://groq.com/)
- [Arxiv API](https://arxiv.org/help/api/)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)

---

## ⚠️ To use InquisiAI, you’ll need a free Groq API Key.
Get one here: https://console.groq.com/keys
Paste it into the app sidebar when prompted.

---

## 🧠 Inspiration

This project is independently designed and academically inspired. While based on LangChain's core capabilities, the idea, branding, interface, and research-focused purpose are original.

---


## 📜 License

MIT License – for academic and non-commercial use.
