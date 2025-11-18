from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


def prompt_generate(user_prompt, user_role):

    systemMessage = SystemMessage(
            content="Consider you are a chatbot based on user role. You will Answer based whic is more relevant or related with that spacific role."
        )
    humanMessage = SystemMessage(
        content=f"{user_prompt}"
        )
    temp = PromptTemplate(
        template="{system_message} User role {user_role} user Question: {human_message}",
        input_variables=['system_message', 'human_message', 'user_role']
        )
    prompt = temp.invoke(input={'system_message': systemMessage, 
                                'human_message': humanMessage,
                                'user_role': user_role})
    
    return prompt
