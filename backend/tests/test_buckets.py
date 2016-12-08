import pytest

from ..bucket import bucket_by_person


def test_bucket_by_person_success():
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

    actual = bucket_by_person(message_list)

    assert actual == expected


def test_bucket_by_person_empty():
    message_list = []

    actual = bucket_by_person(message_list)

    assert actual == {}
