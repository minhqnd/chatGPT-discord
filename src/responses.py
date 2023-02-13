import openai
import os
from src import log

logger = log.setup_logger(__name__)

# Set up API key
OPENAI_TOKEN = os.environ.get('BOT_TOKEN')
openai.api_key = OPENAI_TOKEN

# Define a list to store the conversation history
conversation_history = []

# Start the chat loop

def reset_chat():
    conversation_history = []

def logchat():
    return conversation_history

async def response(message) -> str:
    # Get the user's input
    user_input = message
    conversation_history.append(f"You: {user_input}")

    # Use the API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        # prompt=f"{' '.join(conversation_history)}",
        prompt=message,
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    ).choices[0].text

    # Add the response to the conversation history
    conversation_history.append(f"Bot: {response}")

    # Print the response
    # print(f"{response}")
    # print(f"{conversation_history}")
    logger.info(f"Prompt response:{response}")
    return response.replace("\n\n", "")
