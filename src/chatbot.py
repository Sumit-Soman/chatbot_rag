import os
import warnings
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

"""
    Set and validate the OpenAI API key.

    This function loads the OpenAI API key from environment variables using
    dotenv. If the API key is missing, it raises an error.

    Returns:
    str: The OpenAI API key.

    Raises:
    ValueError: If the API key is not found.
"""
def initialize_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key is missing.")
    return api_key

"""
    Read prompts from a text file.

    This function reads a file containing prompts, with each prompt on a new line,
    and returns a list of non-empty lines.

    Args:
    file_path (str): Path to the text file containing prompts.

    Returns:
    list: A list of prompts as strings.

    Raises:
    FileNotFoundError: If the file does not exist.
"""
def read_prompts(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

"""
    Setup chatbot with FAISS vector store and retrieval.

    This function initializes the chatbot by loading prompts, creating a FAISS
    vector store for prompt embeddings, and setting up a retriever for the vector store.

    Returns:
    tuple: A tuple containing the language model (ChatOpenAI) and retriever.
"""
def setup_chatbot():
    initialize_api_key()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    file_path = os.path.join(os.getcwd(), 'data/prompts.txt')
    prompts = read_prompts(file_path)
    vector_store = FAISS.from_texts(prompts, OpenAIEmbeddings())
    retriever = vector_store.as_retriever()
    return llm, retriever

"""
    Get chatbot response for a query.

    This function uses a RetrievalQA chain to fetch a response for the given query.
    If the query is "quit" or "bye", it returns a farewell message.

    Args:
    llm (ChatOpenAI): The language model instance.
    retriever (FAISS retriever): The retriever instance for the vector store.
    query (str): The user query.

    Returns:
    str: The chatbot's response.
"""
def get_response(llm, retriever, query):
    """Get chatbot response for a query."""
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    if query.lower() in ["quit", "bye"]:
        return "E-commerce Chatbot: Thank you for visiting. Have a great day!"
    return qa_chain.invoke(query)["result"]

"""
    Run the chatbot locally.

    This function starts an interactive session where users can input queries and
    receive responses from the chatbot until they type "quit" or "bye".
"""
def run_chatbot_locally():
    try:
        llm, retriever = setup_chatbot()
        print("E-commerce Chatbot: Welcome! How can I assist you today?")
        while True:
            query = input("You: ")
            if query.lower() in ["quit", "bye"]:
                print("E-commerce Chatbot: Thank you for visiting. Have a great day!")
                break
            response = get_response(llm, retriever, query)
            print(f"Chatbot: {response}")
    except Exception as e:
        print(f"Error: {e}")

# comment out if not running directly
if __name__ == "__main__":
    run_chatbot_locally()

