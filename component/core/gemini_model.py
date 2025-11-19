from langchain_google_genai import ChatGoogleGenerativeAI

def model(model_name='models/gemini-2.5-flash'):
    model = ChatGoogleGenerativeAI(model=model_name)
    return model
    