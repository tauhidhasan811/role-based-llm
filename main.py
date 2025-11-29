from dotenv import load_dotenv
from fastapi import FastAPI, Form
from component.model.crud_repo import insert
from component.core.hug_model import model
from component.core.gemini_model import model
from component.services.prompt import prompt_generate
from component.model.chat_history import GetAllChat

load_dotenv()

app = FastAPI()

@app.post("/api/query")
async def query(user_prompt:str = Form(...),
                user_role:str = Form(...),
                chat_id:int = Form(...)):
    prompt = prompt_generate(user_prompt=user_prompt, user_role=user_role)
    print(prompt)

    ur_data = {
        'text': user_prompt,
        'chat_id' : chat_id
    }
    ur_id = insert(ur_data, cl_name='user_collection')
    #hug_model = model()
    #response = hug_model.invoke(prompt)
    gen_model = model()
    response = gen_model.invoke(prompt)
    res_text = response.content
    ai_data = {
        'text': res_text,
        'chat_id' : chat_id,
        'ur_id': ur_id
    }
    ai_id = insert(ai_data, cl_name='ai_collection')
    data = {
        'text': res_text,
        'ur_id': ur_id,
        'ai_id': ai_id
    }
    print(data)
    return data

@app.post("/api/chat/")
async def get_chat_history(chat_id: int = Form(...)):
    try: 
        chats = GetAllChat(chat_id=chat_id)
        return chats
    except Exception as ex:
        message = {"error": ex}
        return message