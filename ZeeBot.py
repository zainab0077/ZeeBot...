import nltk
import random
from nltk.chat.util import Chat, reflections
import datetime

# Define a list of pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How are you?"]),
    (r"how are you?", ["I'm good, thanks for asking! How about you?", "I'm doing well, how about you?"]),
    (r"what is your name?", ["I am a chatbot created by Zainab.", "You can call me Chatbot."]),
    (r"what do you do?", ["I am here to chat with you and help with whatever I can!", "I'm your friendly assistant, ready to talk anytime!"]),
    (r"what is your favorite color?", ["I like all colors, but blue is calming. What about you?", "I love the color green, it's so peaceful!"]),
    (r"tell me a joke", ["Why don’t skeletons fight each other? They don’t have the guts.", "Why was the math book sad? Because it had too many problems."]),
    (r"bye|exit", ["Goodbye! Take care!", "Take care! See you later!"]),
    (r"my name is (.*)", ["Nice to meet you, %1!", "Hello, %1! How are you today?"]),
    (r"how's the weather today?", ["Sorry, I cannot check the weather right now. But it's always sunny in here!"]),
    (r"what time is it?", [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."]),
    (r"tell me something interesting", ["Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old.", "Here’s a fun fact: Octopuses have three hearts and blue blood!"]),
    (r"how old are you?", ["I'm ageless, like time itself.", "I don't age, I just keep getting smarter!"]),
    (r"what are your hobbies?", ["I enjoy chatting, learning new things, and making conversations more fun!", "I love to read and engage in interesting conversations!"]),
    (r"what's your favorite movie?", ["I enjoy movies that make you think, like 'Inception' or 'The Matrix'. What about you?", "I love animated movies like 'Toy Story' and 'Finding Nemo'."]),
    (r"what's your favorite book?", ["I think '1984' by George Orwell is a thought-provoking book. What's your favorite?", "I enjoy reading mystery novels like 'Sherlock Holmes'."]),
    (r"where do you live?", ["I live in the world of data and information, always here to help you!", "I live in the cloud, always available for a chat!"]),
    (r"what's your favorite food?", ["I can't eat, but if I could, I'd love to try pizza!", "If I had to choose, I'd go for a nice burger."]),
    (r"what's your favorite place?", ["I think the mountains sound peaceful, a place to relax. What about you?", "I'd love to visit Paris, it's so beautiful!"]),
    (r"(.*)", ["Sorry, I didn't quite understand that. Can you ask me something else?", "Can you please rephrase that?"]),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I am your chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Take care!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Start the chat
start_chat()
