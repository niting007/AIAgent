from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from vector import retriever
from vector_person import personRetriever

model = OllamaLLM(model="llama3.2")


template = """
You are an due dilligence exeprt in answering questions about a restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

person_template = """
You are an expert in answering questions about a person

Here are some relevant information about the person: {reviews}

Here is the question to answer: {question}
"""

prompt = PromptTemplate.from_template(person_template)
chain = prompt | model


result = chain.invoke ({"reviews": [], "question": "What was the food like?"})

print(result)

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    reviews = personRetriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)