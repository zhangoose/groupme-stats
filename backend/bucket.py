def bucket_by_person(message_list):
    """
    Parses messages json, organizing them by sender ID.
    """
    messages_by_person = {}

    for message in message_list:
        sender_id = message['sender_id']

        if messages_by_person.get(sender_id):
            messages_by_person[sender_id].append(message)
        else:
            messages_by_person[sender_id] = [message]

    return messages_by_person


