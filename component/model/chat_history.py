
from component.model.crud_repo import get_all

def GetAllChat(chat_id):
    user_text = get_all(cl_name='user_collection')
    ai_text = get_all( cl_name='ai_collection')
    history = {
        'user_message': user_text, 
        'ai_message': ai_text
    }
    return history