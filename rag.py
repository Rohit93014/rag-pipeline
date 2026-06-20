# from dotenv import load_dotenv

# from langchain_groq import ChatGroq
# from langchain_community.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain.chains import RetrievalQA

# load_dotenv()

# # Load Document
# loader = TextLoader("text.txt", encoding="utf-8")
# docs = loader.load()

# # Split Document
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# chunks = splitter.split_documents(docs)

# # Embeddings
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # Vector Store
# db = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings
# )

# retriever = db.as_retriever()

# # Groq LLM
# llm = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     temperature=0
# )


# # RAG Chain
# qa = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever
# )

# # Query
# query = input("Ask Question: ")

# result = qa.invoke({
#     "query": query
# })

# print("\nAnswer:")
# print(result["result"])





from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

load_dotenv()

# Load Document
loader = TextLoader("text.txt", encoding="utf-8")
docs = loader.load()

# Split Document
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector Store
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = db.as_retriever()

# Groq LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# RAG Chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# Function for API
def get_answer(query):
    result = qa.invoke({
        "query": query
    })
    return result["result"]


# Run directly from terminal
if __name__ == "__main__":
    query = input("Ask Question: ")

    answer = get_answer(query)

    print("\nAnswer:")
    print(answer)