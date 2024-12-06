# Chatbot Implementation using Chainlit

A Chainlit-based chatbot that uses OpenAI to simulate a conversational OrderBot for an online restaurant. The chatbot can handle customer interactions, showcase menus, take orders, and provide a seamless ordering experience.

---

## Features

* Greet customers and provide suggestions.
* Display a detailed restaurant menu.
* Take and summarize customer orders.
* Handle delivery or pickup instructions.
* Provide a conversational and user-friendly experience.

---

## Screenshots

![Chatbot Screenshot](image/README/1733396997568.png)
[View Full Chat Sample](image/chat_sample1.pdf)

---

## Getting Started

Follow the instructions below to set up and run the project.

### 1. **Create a Virtual Environment**

It is recommended to create a virtual environment to manage dependencies.

`conda create -n llmapp python=3.10 -y`

### 2. **Activate the Virtual Environment**

Activate the environment before proceeding with the installation.

`conda activate llmapp `

### 3. **Install Dependencies**

Install all required packages from `requirements.txt`.

`pip install -r requirements.txt `

### 4. **Set Up Environment Variables**

Create a `.env` file in the project root and configure the required variables:

`OPENAI_API_KEY=your_openai_api_key `

---

## How to Run?

### 1. **Initialize Chainlit**

To initialize the Chainlit environment, use the following command:

`chainlit init `

### 2. **Run the Chatbot**

Start the chatbot server by running:

`chainlit run app.py `

---

## Project Structure

```
├── app.py               # Main application file
├── src
│   ├── llm.py           # Handles OpenAI interactions
│   ├── prompt.py        # System instructions and menu data
├── chainlit.md          # Markdown for UI customization
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation

```

## Troubleshooting

1. **Missing `.env` File:**

   * Ensure you've created a `.env` file with the correct API key.
2. **Chainlit Not Found:** If the chainlit command isnt recognized, ensure its installed:

   `pip install chainlit`
3. **Dependency Issues:**

   * Ensure all dependencies are installed using `pip install -r requirements.txt`.
