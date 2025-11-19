from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

def model(repo_id="openai/gpt-oss-120b"):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        task="text-generation"
    )

    model= ChatHuggingFace(llm=llm)

    return model
