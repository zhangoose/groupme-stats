import requests

from errors import GroupmeAPIError


BASE_API_URL = "https://api.groupme.com/v3/"

class GroupmeAPI(object):
    """
    Client to call endpoints on the GroupMe API
    """

    def __init__(self, access_token):
        self.access_token = access_token

    def _get(self, url):
        """
        Sends a GET request to the `url` appended to the base API URL with an
        authorization header.

        Returns the response.
        """
        response = requests.get(
            BASE_API_URL + url,
            headers={"x-access-token": self.access_token}
        )
        if response.status_code != 200:
            raise GroupmeAPIError()

        return response

    def get_groups(self):
        """
        Calls the `/groups` endpoint.

        Returns (<status_code>, <json_response>).
        """
        response = self._get("groups")

        return response.json()

    def get_messages(self, group_id, limit=100):
        """
        Calls the `/groups/{group_id}/messages` endpoint with a limit defaulted
        to 100.

        Returns (<status_code>, <json_response>).
        """
        url = "groups/{}/messages?limit={}".format(group_id, limit)
        response = self._get(url)

        return response.json()
