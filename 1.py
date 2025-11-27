from dotenv import load_dotenv
from component.services.prompt import prompt_generate
from component.core.hug_model import model
from component.core.gemini_model import model

load_dotenv()
user_role = input('Enter yoou role: ')

prompt = prompt_generate(user_prompt='what is tools', user_role=user_role)
#print(prompt)
#hug_model = model()
gen_model = model()
    #response = hug_model.invoke(prompt)
#print(gen_model)

response = gen_model.invoke(prompt)
print(response.content)

