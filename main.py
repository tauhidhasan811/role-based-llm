import langchain
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

temp = PromptTemplate(
    template="Write a paragraph about {topic}",
    input_variables=['topi']
)

print(temp)
