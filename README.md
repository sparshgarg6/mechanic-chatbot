# Mechanic Chatbot

## Introduction
This project is a Streamlit-based chatbot that leverages OpenAI's GPT models to provide automated assistance in the field of mechanics. It reads documents from various subdirectories, indexes them, and uses this data to respond to user queries, making it a valuable tool for quick information retrieval in mechanical troubleshooting and repair.

## Features
- **Document Indexing**: Indexes documents from specified subdirectories for efficient data retrieval.
- **OpenAI GPT Integration**: Utilizes OpenAI's GPT models for generating chatbot responses.
- **Streamlit Interface**: Provides an easy-to-use web interface for user interactions.
- **Persistent Chat History**: Saves chat history for each user session.

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- OpenAI API Key

### Installation
1. Clone the repository:
   git clone https://github.com/sparshgarg6/mechanic-chatbot.git
2. Install required Python packages: pip install streamlit openai

### Setup
1. Place your training documents in the specified subdirectories under "TrainingDocuments".
2. Update the script with your OpenAI API Key in the designated place.

### Running the App
1. Navigate to the project directory.
2. Start the Streamlit app:
   1. streamlit run app.py
3. Interact with the chatbot via the Streamlit interface.

## Usage

Enter your name to start a session with the chatbot. You can ask questions related to mechanical troubleshooting and repairs, and the chatbot will respond based on the indexed documents.

## License

This project is released under the MIT License.

## Acknowledgments

- Thanks to OpenAI for providing the GPT models.
- Streamlit for the interactive web app framework.
