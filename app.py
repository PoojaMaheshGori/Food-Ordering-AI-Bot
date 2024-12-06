import chainlit as cl
import logging
from src.llm import handle_order_request

PROMPT_SUGGESTIONS = [
    "Show me the menu.",
    "What are today's specials?",
    "I want to order a pizza.",
    "Do you have vegan options?",
    "What are your delivery charges?",
    "Can I customize my burger?",
    "What desserts do you have?",
]

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@cl.on_chat_start
async def chat_start():
    """
    Triggered when a chat session starts.
    
    This function initializes the chat interface by:
    - Loading the content from `chainlit.md` if available.
    - Displaying a welcome message and predefined prompt suggestions.
    """
    try:
        # Load markdown file if it exists
        with open("chainlit.md", "r") as f:
            content = f.read()
        await cl.Message(content=content).send()
    except FileNotFoundError:
        logging.warning("chainlit.md not found. Proceeding without it.")
        await cl.Message(content="Welcome to our online food ordering service!").send()
    
    # Display a welcome message and prompt suggestions
    suggestions = "\n".join([f"- {prompt}" for prompt in PROMPT_SUGGESTIONS])
    await cl.Message(
        content=(
            "You can order any item you want from the menu or ask for suggestions. \n\n"
            "Here are some prompt suggestions:\n"
            f"{suggestions}\n\n"
        )
    ).send()


@cl.on_message
async def on_userMessage(message: cl.Message):
    """
    Triggered when a user sends a message.

    Processes the user's input, calls the order request handler, 
    and sends the appropriate response.
    
    Args:
        message (cl.Message): The incoming user message.
    """
    prompt = message.content

    try:
        # Handle the user's message and generate a response
        response = handle_order_request(prompt)
        await cl.Message(content=response).send()
    except Exception as e:
        # Log the error and send a user-friendly error message
        logging.error(f"Error handling user message: {e}")
        await cl.Message(content="Sorry, something went wrong. Please try again later.").send()
