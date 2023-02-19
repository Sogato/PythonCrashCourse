def send_messages(msg, sent_msg):
    while msg:
        msg_p = msg.pop()
        print(msg_p)
        sent_msg.append(msg_p)


messages = ['Всем приввет!', 'Как дела?', 'Как себя чувствуешь?']
sent_messages = []
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)
