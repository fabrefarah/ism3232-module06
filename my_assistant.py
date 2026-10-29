# my_assistant.py
# Author: Farah Fabre


class BusinessAssistant:
    """A small business assistant that uses an appointment tool."""

    def __init__(self, name, instructions, tool):
        """Set up the assistant, its tool, and its conversation history."""
        self.name = name
        self.instructions = instructions
        self.tool = tool
        self.history = []

    def respond(self, user_message):
        """Record a message, choose a reply, and record the response."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply based on the customer's request."""
        text = user_message.lower()

        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. I can help with appointments."

        if "appointment" in text or "time" in text or "open" in text:
            day = self.tool.find_day(text)

            if day is None:
                return "Which day would you like to check?"

            times = self.tool.times_for(day)

            if not times:
                return f"Sorry, there are no available appointments on {day.title()}."

            return f"On {day.title()}, we have appointments at {' and '.join(times)}."

        if "parking" in text or "refund" in text or "payment" in text:
            return "I can't handle that request here. I'll pass you to the front desk."

        return "I'm not sure how to help with that. I can check appointment times."
