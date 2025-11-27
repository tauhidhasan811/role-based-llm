# LLM Role-Based Prompting

This project enables Large Language Models (LLMs) to generate responses tailored to a user's specific role or domain. It leverages both Google and HuggingFace models to enhance accuracy and contextual relevance. The setup involves cloning the repository, configuring API keys in a `.env` file, and running a FastAPI server.

## Run Instructions

1.  **Clone the repository:**
    *   `git clone <repository_url>`
2.  **Navigate to the project directory:**
    *   `cd <project_directory>`
3.  **Install dependencies:**
    *   `pip install -r requirements.txt`
4.  **Configure environment variables:**
    *   Create a `.env` file in the root directory.
    *   Add necessary API keys (e.g., `GOOGLE_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`).
5.  **Run the FastAPI application:**
    *   Using `uvicorn` (install if not present: `pip install uvicorn`):
        *   `uvicorn main:app --reload` (for `main.py`)
        *   `uvicorn multipi_api:app --reload` (for `multipi_api.py`)

## Folder Structure

```
root
| ---> component
|      | ---> core
|      |      | ---> db_config.py
|      |      | ---> gemini_model.py
|      |      | ---> hug_model.py
|      | ---> services
|             | ---> prompt.py
| ---> .gitignore
| ---> 1.py
| ---> main.py
| ---> multipi_api.py
| ---> README.md
| ---> requirements.txt
```

## File Descriptions

*   `.gitignore`: Specifies files and directories to be ignored by Git, such as virtual environments and environment files.
*   `1.py`: A Python script that loads environment variables, prompts for a user role, and uses a Gemini model to generate a text response.
*   `main.py`: A FastAPI application with an `/api/query` endpoint that accepts user prompts and roles to generate LLM responses.
*   `multipi_api.py`: A FastAPI application supporting `/api/query` to interact with either Hugging Face or Gemini models based on user input.
*   `README.md`: This file, providing an overview, setup, and usage instructions for the repository.
*   `requirements.txt`: Lists all Python package dependencies required for the project, including FastAPI and Langchain components.
*   `component/core/db_config.py`: Defines database connection configurations for different environments.
*   `component/core/gemini_model.py`: Initializes and returns a Google Gemini conversational AI model instance.
*   `component/core/hug_model.py`: Initializes and returns a Langchain `ChatHuggingFace` model instance.
*   `component/services/prompt.py`: Contains a function to generate context-aware prompts for language models, incorporating system messages and user roles.