import base64
import os

from mlflow.tracking.request_auth.abstract_request_auth_provider import (
    RequestAuthProvider,
)


class ProxyAuthProvider(RequestAuthProvider):
    def __init__(self):
        self.username = os.getenv("MLFLOW_TRACKING_USERNAME")
        self.password = os.getenv("MLFLOW_TRACKING_PASSWORD")

    def get_name(self):
        return "proxy_auth_provider"

    def get_auth(self):
        # Add your Authelia Proxy-Authorization logic here
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
            "utf-8"
        )
        proxy_authorization_header = f"Basic {encoded_credentials}"

        # Return a dictionary containing the header for authentication
        return {"Proxy-Authorization": proxy_authorization_header}
