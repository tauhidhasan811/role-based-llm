import langchain
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens= 500
)
model=ChatHuggingFace(llm=llm)

temp = PromptTemplate(
    template="Write a paragraph about {topic}",
    input_variables=['topic']
)

prompt = temp.invoke({'topic': 'cow'})

response = model.invoke(prompt)
print(f"Templete : {temp}\n\n")
print(f"Prompt : {prompt}\n\n")
print(f"Response : {response}")