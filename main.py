import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = 'your-key-here' #input your OpenAI API Key

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

# List of subdirectories to read from
subdirectories = [
    'ComponentInformation',
    'RepairInstructions',
    'ServiceIntervals',
    'SymptomsAndDiagnostics',
    'TroubleShootingTrees'
]

# Base directory path
base_dir = '/Users/sparshgarg/mechanicChatbot/TrainingDocuments/'

# Initialize an empty list to hold all documents
all_documents = []

# Loop through each subdirectory and read files
for subdirectory in subdirectories:
    directory_path = os.path.join(base_dir, subdirectory)
    documents = SimpleDirectoryReader(directory_path).load_data()
    all_documents.extend(documents)

# Now all_documents contains files from all subdirectories
print(all_documents)


index = GPTVectorStoreIndex.from_documents(documents)

# Save the index
index.storage_context.persist('/Users/sparshgarg/mechanicChatbot/TrainingDocuments')

from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults(
                  persist_dir='/Users/sparshgarg/mechanicChatbot/TrainingDocuments')

# load index
index = load_index_from_storage(storage_context)

# Chat Bot

import openai
import json


class Chatbot:
    def __init__(self, api_key, index, user_id):
        self.index = index
        openai.api_key = api_key
        self.user_id = user_id
        self.chat_history = []
        self.filename = f"{self.user_id}_chat_history.json"

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}"
                            for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}"
        query_engine = index.as_query_engine()
        response = query_engine.query(user_input)

        message = {"role": "assistant", "content": response.response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message

    def load_chat_history(self):
        try:
            with open(self.filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self):
        with open(self.filename, 'w') as f:
            json.dump(self.chat_history, f)


# Streamlit app
def main():
    st.title("Mechanic Chatbot")

    # User ID
    user_id = st.text_input("Your Name:")

    # Check if user ID is provided
    if user_id:
        # Create chatbot instance for the user
        bot = Chatbot("your-API-key ", index, user_id) #input your API key here as well.

        # Load chat history
        bot.load_chat_history()

        # Display chat history
        for message in bot.chat_history[-6:]:
            st.write(f"{message['role']}: {message['content']}")

        # User input
        user_input = st.text_input("Type your questions here :) - ")

        # Generate response
        if user_input:
            if user_input.lower() in ["bye", "goodbye"]:
                bot_response = "Goodbye!"
            else:
                bot_response = bot.generate_response(user_input)
                bot_response_content = bot_response['content']
                st.write(f"{user_id}: {user_input}")
                st.write(f"Bot: {bot_response_content}")
                bot.save_chat_history()
                bot.chat_history.append
                ({"role": "user", "content": user_input})
            bot.chat_history.append
            ({"role": "assistant", "content": bot_response_content})


if __name__ == "__main__":
    main()
