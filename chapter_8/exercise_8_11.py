def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ['Всем приввет!', 'Как дела?', 'Как себя чувствуешь?']
sent_messages = []
send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
