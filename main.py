from dotenv import load_dotenv
from fastapi import FastAPI, Form
from component.services.prompt import prompt_generate
from component.core.hug_model import model
from component.core.gemini_model import model

load_dotenv()

app = FastAPI()

@app.post("/api/query")
async def query(user_prompt:str = Form(...),
                user_role:str = Form(...)):
    prompt = prompt_generate(user_prompt=user_prompt, user_role=user_role)
    print(prompt)
    hug_model = model()
    gen_model = model()
    #response = hug_model.invoke(prompt)
    print(gen_model)

    response = gen_model.invoke(prompt)


    return response
