from dotenv import load_dotenv
from component.services.prompt import prompt_generate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()
prompt = prompt_generate(user_prompt='How are you',user_role='doctor')

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

response = model.invoke(prompt)
print(f"\n\nResponse is : {response}")

print(f"\n\Content is : {response.content}\n\n")