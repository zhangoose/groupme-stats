def validate_list_messages_args(args):
    """
    """
    BUCKET_BY_OPTIONS = [
        "user", None
    ]

    if not args.get('offset'):
        return False
    if args.get('bucket_by') not in BUCKET_BY_OPTIONS:
        return False
    return True
