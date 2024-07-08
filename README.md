# AI-Powered PDF Analysis and Q&A System

This project is an AI-powered PDF analysis and Q&A system developed using Streamlit, AWS S3, Bedrock embeddings, and FAISS. It processes PDF documents, chunks the text, and stores vectors for efficient retrieval and question answering. The system is containerized using Docker, ensuring seamless deployment and scalability, with services exposed on different ports to enhance robustness and accessibility.

## Features

- **Streamlit Interface**: User-friendly web interface for uploading and analyzing PDF documents.
- **AWS S3 Integration**: Stores processed files and vector data in S3 for persistent storage.
- **Bedrock Embeddings**: Uses Amazon's Bedrock embeddings for text vectorization.
- **FAISS Vector Store**: Efficient storage and retrieval of text chunks using FAISS.
- **Dockerized Deployment**: Containerized application for easy deployment and scalability.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-pdf-analysis-qa.git
    cd ai-pdf-analysis-qa
    ```

2. **Set up environment variables:**
    Create a `.env` file in the project root directory and add your AWS S3 bucket name.
    ```env
    BUCKET_NAME=your-s3-bucket-name
    ```

3. **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```

## Usage

1. **Admin Interface**: 
    - Access the admin interface at `http://localhost:8083`.
    - Upload a PDF document to process and create a vector store.

2. **Client Interface**:
    - Access the client interface at `http://localhost:8084`.
    - Ask questions based on the processed PDF documents and get AI-powered responses.

## File Structure

- `admin.py`: Handles PDF upload, text chunking, and vector store creation.
- `app.py`: Handles question input and retrieves answers using the vector store.
- `Dockerfile`: Docker configuration for the admin and client services.
- `requirements.txt`: Python dependencies for the project.
- `docker-compose.yml`: Docker Compose configuration for multi-service setup.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer.

