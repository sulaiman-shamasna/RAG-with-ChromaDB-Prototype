from retriever import Retriever
import subprocess

class RAGChatbot:
    def __init__(self, retriever, model_name='llama2'):
        self.retriever = retriever
        self.model_name = model_name

    def generate_response(self, user_query):
        docs = self.retriever.retrieve(user_query)
        context = "\n\n".join(docs)

        prompt = f"Context:\n{context}\n\nUser: {user_query}\nChatbot:"

        try:
            process = subprocess.Popen(
                ['ollama', 'run', self.model_name],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=prompt)

            if stderr:
                print("Error:", stderr)
                return "I'm sorry, I couldn't process your request."

            return stdout.strip()
        except Exception as e:
            print("Exception:", e)
            return "An error occurred while generating the response."
