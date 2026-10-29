# my_main.py
# Author: Farah Fabre

from my_assistant import BusinessAssistant
from my_tool import AppointmentTool

schedule = {
    "Monday": ["10:00 am", "2:30 pm"],
    "Tuesday": ["11:00 am"],
    "Wednesday": ["9:00 am", "1:00 pm"],
    "Friday": ["10:30 am"],
}

tool = AppointmentTool(schedule)

assistant = BusinessAssistant(
    "Robin",
    "Be friendly and helpful.",
    tool,
)

print("Type a message, or type quit to stop.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    reply = assistant.respond(message)
    print(f"Robin: {reply}")

print(f"Messages in this conversation: {len(assistant.history)}")
