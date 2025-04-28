## Preferhub Chatbot
This project is a Streamlit-based chatbot that answers user queries by utilizing content scraped from the Preferhub website. The system is built in two main components:

scrape.py – A Python script that scrapes the Preferhub website, extracts the text content, and saves it in a text file.
app.py – A Streamlit app that loads the scraped content and uses Azure OpenAI to generate responses to the user's queries based on that content.

## 🛠 Project Overview\

## 1. Scraping Phase: scrape.py
The scrape.py script is designed to scrape the Preferhub website and extract all its textual content. The main steps include:

- URL Scraping: Starting from the base URL of the Preferhub website, it recursively visits all internal links within the same domain.
- Content Extraction: Extracts the visible textual content of each page using BeautifulSoup and removes unnecessary formatting, resulting in clean text.
- Link Validation: Ensures that only valid internal links are scraped to avoid external websites or dead links.
- Data Storage: The extracted content is saved in a plain text file named preferhub_content.txt within the scraped_content directory. This file serves as the knowledge base for the chatbot.

## 2. Chatbot Phase: app.py
The app.py file is a Streamlit application that provides a user interface for interacting with the Preferhub chatbot. Here’s how it functions:

- Chat History: Users can engage in multiple chat sessions, and the chatbot remembers the chat history within the current session.
- Azure OpenAI Integration: The chatbot uses Azure OpenAI’s GPT model to process user queries and generate responses based on the scraped content. The content from the preferhub_content.txt file is passed as context to the model.
- User Interaction: Users type their questions, and the chatbot provides answers derived exclusively from the content in the scraped file. It is limited to this data and will politely decline any unrelated queries.
- System Instructions: The system prompt instructs the model to only use the content from Preferhub for answering questions, ensuring the responses stay relevant to the topic.

## 📝 Features
- Content Scraping: Automatically extracts textual content from the Preferhub website.
- Streamlit UI: An interactive user interface to ask questions and view responses.
- Azure OpenAI Integration: Uses the Azure OpenAI API for generating responses to user queries based on the scraped website content.
- Chat History: Keeps track of previous chats, allowing users to revisit past conversations.
- Error Handling: Handles basic request failures during the scraping process to ensure smooth operation.
- Customizable System Prompt: The behavior of the chatbot can be easily customized by modifying the system prompt used in the API call.

## 🚀 Getting Started
To run this project locally, follow the steps below.

$$ Prerequisites
Before running the project, ensure you have the following:
1. Python 3.7+: This project is compatible with Python 3.7 or later.
2. Azure OpenAI Credentials: You will need access to the Azure OpenAI API. Set up your credentials by creating an instance of the Azure OpenAI Service in the Azure portal. (or replace it with any open source api)
3. Libraries: Install the required libraries using the provided requirements.txt.

## Setup Instructions
1. Clone the repository
2. Install Dependencies
3. Configure your model endpoints
4. Run scrape.py for your desired link
5. Run app.py in streamlit

## 🧠 Customization
You can modify the chatbot's behavior and appearance in the following ways:

- Change the Starting URL: Update the start_url in scrape.py if you want to scrape a different website.
- Modify the System Prompt: You can customize the generate_system_prompt() function in app.py to adjust how the assistant responds to user queries.
- Edit the Scraping Logic: If you need to scrape additional content or handle more complex page structures, you can modify the scrape.py script.

