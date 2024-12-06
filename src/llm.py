from openai import OpenAI
from src.prompt import system_instruction
import logging

# Initialize the OpenAI client
client = OpenAI()

# Define the initial chat context with system instructions
chat = [{"role": "system", "content": system_instruction}]

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def handle_order_request(message: str, model: str = "gpt-3.5-turbo", temperature: float = 0) -> str:
    """
    Processes the user's order request by interacting with the OpenAI model.

    Args:
        message (str): The user's input message.
        model (str, optional): The model to use for the response. Defaults to "gpt-3.5-turbo".
        temperature (float, optional): Controls the randomness of the response. Defaults to 0.

    Returns:
        str: The assistant's response to the user's message.

    Raises:
        Exception: If the OpenAI API call fails or returns an invalid response.
    """
    try:
        # Append the user's message to the chat history
        chat.append({"role": "user", "content": message})
        
        # Call the OpenAI API to generate a response
        response = client.chat.completions.create(
            model=model,
            messages=chat,
            temperature=temperature
        )
        
        # Extract the assistant's response
        response_content = response.choices[0].message.content
        chat.append({"role": "assistant", "content": response_content})
        
        logging.info("Successfully generated response.")
        return response_content

    except Exception as e:
        # Log the error and raise an exception with a user-friendly message
        logging.error(f"Error generating response: {e}")
        raise Exception("An error occurred while processing your request. Please try again later.")
