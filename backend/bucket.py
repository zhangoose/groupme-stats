from datetime import datetime
from pytz import UTC


def bucket_by_user(message_list):
    """
    Parses messages json, organizing them by sender ID.
    """
    messages_by_user = {}

    for message in message_list:
        sender_id = message['sender_id']

        if messages_by_user.get(sender_id):
            messages_by_user[sender_id].append(message)
        else:
            messages_by_user[sender_id] = [message]

    return messages_by_user


def bucket_by_user_day(message_list):
    messages_by_user = bucket_by_user(message_list)
    messages_by_user_day = {}

    for sender_id, messages in messages_by_user.items():
        for message in messages:
            created_at_date = datetime.fromtimestamp(
                message['created_at'],
                tz=UTC
            ).date().isoformat()

            if messages_by_user_day.get(sender_id):
                if messages_by_user_day[sender_id].get(created_at_date):
                    messages_by_user_day[sender_id][created_at_date].append(message)
                else:
                    messages_by_user_day[sender_id][created_at_date] = [message]
            else:
                messages_by_user_day[sender_id] = {created_at_date: [message]}
    
    return messages_by_user_day
