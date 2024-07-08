import boto3
import streamlit as st
import os
import uuid



## s3 client 
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")


## bedrock
from langchain_community.embeddings import BedrockEmbeddings

## Text splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

## Pdf Loader
from langchain_community.document_loaders import PyPDFLoader

## import FAISS
from langchain_community.vectorstores import FAISS

bedrock_client = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock_client)

def generate_id():
    return str(uuid.uuid4())

# split the pages into chunks
def split_text(pages, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size,chunk_overlap = chunk_overlap)
    docs = text_splitter.split_documents(pages)
    return docs

def create_vector_store(request_id, documents):
    vectorstore_faiss=FAISS.from_documents(documents, bedrock_embeddings)
    file_name=f"{request_id}.bin"
    folder_path="/tmp/"
    vectorstore_faiss.save_local(index_name=file_name, folder_path=folder_path)

    ## upload to S3
    s3_client.upload_file(Filename=folder_path + "/" + file_name + ".faiss", Bucket=BUCKET_NAME, Key="my_faiss.faiss")
    s3_client.upload_file(Filename=folder_path + "/" + file_name + ".pkl", Bucket=BUCKET_NAME, Key="my_faiss.pkl")

    return True


def main():
    st.write("This is Admin site for chat with pdf demo")
    uploaded_file = st.file_uploader("choose a file","pdf")
    if uploaded_file is not None:
        request_id  = generate_id()
        st.write(f"Request_id: {request_id}")
        saved_file_name = f"{request_id}.pdf"
        with open(saved_file_name, mode = "wb") as w:
            w.write(uploaded_file.getvalue())

        loader = PyPDFLoader(saved_file_name)
        pages = loader.load_and_split()

        st.write(f"Total Pages in the Pdf: {len(pages)}")

        ##split texts
        splitted_docs = split_text(pages, 1000, 200)
        st.write(f"Splitted Docs length : {len(splitted_docs)}")
        st.write("============================================")
        st.write(splitted_docs[0])
        st.write("============================================")
        st.write(splitted_docs[1])


        st.write("Creating Vector Store")
        result = create_vector_store(request_id,splitted_docs)

        if result:
            st.write("PDF Processed Successfully.")
        else:
            st.write("Error Please Check Logs.")



if __name__ == "__main__":
    main()