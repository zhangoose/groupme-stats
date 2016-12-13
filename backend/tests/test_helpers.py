import pytest
import mock

from ..helpers import filter_messages, validate_list_messages_args
from ..errors import GroupmeAPIError


def test_filter_messages_success():
    api = mock.Mock()
    api.get_messages.side_effect = [
        {
            "response": {
                "messages": [
                    {
                        "text": "this shouldn't be retruned",
                        "id": "0",
                        "created_at": 1481328000
                    },
                    {
                        "text": "beware of the beast",
                        "id": "789", 
                        "created_at": 1481241600 # end date
                    },
                    {
                        "text": "everyone has a torch to burn",
                        "id": "456",
                        "created_at": 1481172236 # in between
                    }
                ]
            }
        },
        {
            "response": {
                "messages": [
                    {
                        "text": "what are you doing here?",
                        "id": "123",
                        "created_at": 1481068800 # start date
                    },
                    {
                        "text": "this shouldn't be returned",
                        "id": "000",
                        "created_at": 1480982400
                    }
                ]
            }
        }
    ]
    expected = [
        {
            "text": "beware of the beast",
            "id": "789", 
            "created_at": 1481241600
        },
        {
            "text": "everyone has a torch to burn",
            "id": "456",
            "created_at": 1481172236
        },
        {
            "text": "what are you doing here?",
            "id": "123",
            "created_at": 1481068800
        }
    ]

    actual = filter_messages(api, "555", 1481068800, 1481241600)
    # 1481068800 = Wed, 07 Dec 2016 00:00:00 GMT
    # 1481241600 = Fri, 09 Dec 2016 00:00:00 GMT
    
    assert actual == expected


def test_filter_messages_error():
    api = mock.Mock()
    api.get_messages.side_effect = GroupmeAPIError

    actual = filter_messages(api, "555", 0, 0)

    assert actual == []


def test_validate_list_messages_args():
    args = {
        "bucket_by": "user",
        "start_date": "1481068800",
        "end_date": "1481241600"
    }

    actual = validate_list_messages_args(args)

    assert actual == True
