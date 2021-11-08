import ssl
from typing import Dict, Tuple, Union

import attr
import httpx


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API"""

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    auth: Union[str, Tuple[str, str]]

    def __attrs_post_init__(self):
        """Create new session after class initialization"""
        self.create_session()

    def get_auth(self):
        return self.auth

    def get_session(self):
        return self.session

    def create_session(self):
        """Create new session with the arguments obtained from client"""
        self.session = httpx.Client(
            base_url=self.base_url,
            auth=self.auth,
            headers=self.headers,
            cookies=self.cookies,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

    def close_session(self):
        self.session.close()

    def reload_session(self):
        self.close_session()
        self.create_session()
