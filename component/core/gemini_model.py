from langchain_google_genai import ChatGoogleGenerativeAI

def model(model_name='models/gemini-2.5-flash'):
    model = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.5, 
        max_output_tokens=512, 
        top_p=0.8)  #model parameters adjusted 
    return model
    
