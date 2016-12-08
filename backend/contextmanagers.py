from contextlib import contextmanager

from client import GroupmeAPI


@contextmanager
def call_api(accessToken):
    api = GroupmeAPI(accessToken)
    yield api


