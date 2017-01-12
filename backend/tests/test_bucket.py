import pytest

from ..bucket import bucket_by_user, bucket_by_user_day, bucket_by_day


def test_bucket_by_user_success():
    message_list = [
        {
            "sender_id": "1234",
            "text": "we should ask him for help!"
        },
        {
            "sender_id": "5678",
            "text": "no, we should not ask him for help"
        },
        {
            "sender_id": "1234",
            "text": "but--!"
        }
    ]
    expected = {
        "1234": [
            message_list[0], message_list[2]
        ],
        "5678": [
            message_list[1]
        ]
    }

    actual = bucket_by_user(message_list)

    assert actual == expected


def test_bucket_by_user_empty():
    message_list = []

    actual = bucket_by_user(message_list)

    assert actual == {}


def test_bucket_by_user_day():
    message_list = [
        {
            "sender_id": "1234",
            "created_at": 1481364000,
            "text": "we should ask him for help!"
        },
        {
            "sender_id": "5678",
            "created_at": 1481364000,
            "text": "no, we should not ask him for help"
        },
        {
            "sender_id": "1234",
            "created_at": 1481492749,
            "text": "but--!"
        }
    ]
    expected = {
        "1234": {
            "2016-12-10": [
                message_list[0]
            ],
            "2016-12-11": [
                message_list[2]
            ]
        },
        "5678": {
            "2016-12-10": [
                message_list[1]
            ]
        }
    }

    actual = bucket_by_user_day(message_list)

    assert actual == expected


def test_bucket_by_day():
    message_list = [
        {
            "sender_id": "1234",
            "created_at": 1481364000,
            "text": "we should ask him for help!"
        },
        {
            "sender_id": "5678",
            "created_at": 1481364000,
            "text": "no, we should not ask him for help"
        },
        {
            "sender_id": "1234",
            "created_at": 1481492749,
            "text": "but--!"
        }
    ]
    expected = {
        "2016-12-10": [
            message_list[0],
            message_list[1]
        ],
        "2016-12-11": [
            message_list[2]
        ]
    }

    actual = bucket_by_day(message_list)

    assert actual == expected


