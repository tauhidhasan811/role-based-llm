
# Role-Based LLM

This project generates **profession-relevant responses from LLMs**, tailored to the user’s specific role or domain. The system uses Google and HuggingFace models to provide more accurate and contextual outputs.

---

## 🚀 Project Setup & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tauhidhasan811/role-based-llm
```

### 2. Create a `.env` File

Add your API keys inside the file:

```
GOOGLE_API_KEY=""
HUGGINGFACE_API_KEY=""
```

### 3. Create a Virtual Environment

```bash
py -m venv your_env_name
```

### 4. Activate the Virtual Environment

```bash
your_env_name/Scripts/activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI Server

```bash
fastapi dev main.py
```

### 📌 API Access

* Base URL: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* Swagger Docs (API UI): **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📄 Postman Documentation

You can view the full API documentation using this Postman link:
`postman_url`

---

