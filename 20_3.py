def print_only_new(message):
    old_messages = []
    while True:
        message = input()
        if message not in old_messages:
            print(message)
        old_messages.append(message)
