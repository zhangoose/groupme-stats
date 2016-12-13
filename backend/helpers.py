from errors import GroupmeAPIError


def validate_list_messages_args(args):
    """
    Validates the URL params for /groups/<id>/messages endpoint.

    Returns True/False.
    """
    BUCKET_BY_OPTIONS = [
        "user", "user_day", None
    ]

    if not args.get('start_date') and not args.get('end_date'):
        return False
    if args.get('bucket_by') not in BUCKET_BY_OPTIONS:
        return False
    return True


def filter_messages(api, group_id, start_date, end_date):
    """
    Uses the Groupme `api` given to call Groupme for messages from epoch
    represented `start_date` to `end_date`.

    Messages in this list should have timestamps [start_date, end_date]

    Returns a list of messages.
    """
    all_messages = []
    last_sender_id = ""
    reached_start = False

    while not reached_start:
        try:
            response = api.get_messages(
                group_id=group_id,
                limit=100,
                before_id=last_sender_id
            )
        except GroupmeAPIError:
            return all_messages

        # check epoch dates and determine if you still want to run this loop
        messages = response['response']['messages'] 
        for message in messages:
            created_at = message['created_at']
            if created_at >= start_date and created_at <= end_date:
                # within the range
                all_messages.append(message)
            elif created_at < start_date:
                # don't look at any more messages after this one
                # messages come back from most --> least recent
                reached_start = True
                break
            last_sender_id = message['id']

    return all_messages
