def bucket_by_person(message_response):
    """
    Parses messages json, organizing them by person ID.
    """
    messages_by_person = {}

    try:
        all_messages = message_response['response']['messages']
    except KeyError:
        return {}

    for message in all_messages:
        sender_id = message['sender_id']

        if messages_by_person.get(sender_id):
            messages_by_person[sender_id].append(message)
        else:
            messages_by_person[sender_id] = [message]

    return messages_by_person



def no_bucket(message_response):
    """
    """
    try:
        return message_response['response']['messages']
    except KeyError:
        return []
