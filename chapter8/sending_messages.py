def send_messages(messages):
    """Print each message, and move each message to sent_messages after printing."""
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages
messages = ['Hello', 'Hi', 'How are you?','Hey there!']
sent_messages = send_messages(messages[:])
print("\nThe following messages have been sent:") 
for message in sent_messages:
    print(message)