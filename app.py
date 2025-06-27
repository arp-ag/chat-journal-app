import streamlit as st
import json
from datetime import datetime
import os

st.set_page_config(page_title="Chat Journal", page_icon="💬")
st.title("💬 Chat Journal")
st.markdown("_Talk to yourself. Safely._")

# Load messages
if os.path.exists("journal.json"):
    with open("journal.json", "r") as f:
        messages = json.load(f)
else:
    messages = []

# Display messages
for msg in messages:
    st.write(f"**{msg['time']}** - {msg['text']}")

# Chat input
user_input = st.chat_input("What’s on your mind?")

if user_input:
    new_msg = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": f"{user_input}"
    }
    messages.append(new_msg)

    # Save
    with open("journal.json", "w") as f:
        json.dump(messages, f, indent=4)

    st.rerun()
