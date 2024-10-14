# RAG-with-Ollama-and-ChromaDB
---
This project aims at building a chatbot that leverages a ***Retrieval-Augmented Generation (RAG)*** system to provide accurate and contextually relevant responses. By integrating ***Ollama*** with open-source language models and a retrieval system using ***ChromaDB***, the chatbot can access and utilize a knowledge base without relying on proprietary *APIs* or *keys*.

## Key Features:

- ***Open-Source Stack***: Utilizes entirely open-source tools and models.
- ***Local Deployment***: Runs on local machines or servers without external dependencies.
- ***RAG System***: Combines retrieval mechanisms with language generation for enhanced responses.
- ***Scalable***: Easily expandable with additional data and models.
- ***Simple UI***: Implements a user-friendly interface using *Streamlit*.

## System Architecture
***Block Diagram***

Below is a block diagram illustrating the system architecture of the *Ollama* Chatbot with a *RAG* system using *ChromaDB*, *FastAPI*, and *Streamlit*:`

A PLOT TO ADD

***Components***:

- ***Streamlit UI***: A user-friendly frontend interface for user interactions.
- ***FastAPI API***: Handles API requests, processes user queries, and communicates with other components.
- ***ChromaDB***: Serves as the vector store for storing and retrieving document embeddings.
- ***Ollama LLM***: Hosts and manages the language model locally to generate responses.

....

....

....

## Install and Configure Ollama
---
*Ollama* is a platform to run large language models locally. Follow these steps to install and set it up on Windows:

- ***Download Ollama***. 
1. Visit the [Ollama website](https://ollama.com/) and navigate to the Downloads section.
2. Download the Windows installer (```.exe``` file).

- ***Install Ollama***
1. Run the downloaded installer and follow the on-screen instructions to complete the installation.
2. Note: Ensure that you have administrative privileges during installation.

- ***Verify Installation***. Open Command Prompt or PowerShell and run:
```bash
ollama --version
```