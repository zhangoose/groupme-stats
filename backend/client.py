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

        Returns the json_response.
        """
        response = self._get("groups")

        return response.json()

    def get_messages(self, group_id, limit=100, before_id=""):
        """
        Calls the `/groups/{group_id}/messages` endpoint with a limit defaulted
        to 100.

        Returns the json_response.
        """
        url = "groups/{}/messages?limit={}&before_id={}".format(
            group_id, limit, before_id)
        response = self._get(url)

        return response.json()
