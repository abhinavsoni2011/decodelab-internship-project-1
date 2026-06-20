#Rule-Based AI Chatbot

A simple command-line Rule-Based AI Chatbot built with Python. This project demonstrates the use of dictionaries, loops, conditional statements, and user input handling to create a basic chatbot.

##Features

* Multi-language greetings support
* Dictionary-based response system
* Continuous conversation using a while loop
* Input sanitization using "lower()" and "strip()"
* Default response for unknown commands
* Exit command to end the chatbot

##Project Structure
```text
.
├── chatbot.py
└── README.md
```
##Code Overview

The program uses:

* Dictionary to store chatbot responses
* while loop to keep the chatbot running
* if-else statements for control flow
* input() for user interaction
* .get() method for response lookup and fallback handling

How to Run

1. Make sure Python is installed on your system.
2. Clone the repository:
```bash
git clone https://github.com/abhinavsoni2011/decodelab-internship-project-1.git
```
3. Navigate to the project folder:
```
cd decodelab-internship-project-1
```
4. Run the program:
```bash
python chatbot.py
```
##Example Usage
```text
=== Rule-Based AI Chatbot ===
Type 'exit' to quit.

You: hello
AI Bot: Hello! How can I help you?

You: namaste
AI Bot: Namaste! Aap kaise hain?

You: hola
AI Bot: ¡Hola! ¿Cómo estás?

You: how are you
AI Bot: I am fine. Thank you!

You: xyz
AI Bot: Sorry, I don't understand that command.

You: exit
AI Bot: Goodbye!
```
##Learning Objectives

This project helps beginners understand:

* Python Dictionaries
* Loops ("while")
* Conditional Statements ("if-else")
* User Input Handling
* String Manipulation
* Basic AI Chatbot Concepts

##Future Improvements

* Add more languages and responses
* Support multiple intents for one response
* Store chat history
* Add GUI using Tkinter
* Integrate with AI APIs

##Author

Abhinav Soni
B.Tech CSE Student
GIT Jaipur