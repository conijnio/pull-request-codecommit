import re
from typing import Optional
from enum import Enum


class Remote:
    """
    Understands remote CodeCommit URLs
    """

    class Protocol(Enum):
        SSH = 1
        HTTPS = 2

    def __init__(self, url: str):
        self.__url: str = url
        self.__region: Optional[str] = ""
        self.__profile: Optional[str] = ""
        self.__name: str = ""
        self.__protocol: Remote.Protocol = (
            Remote.Protocol.SSH if url.startswith("ssh://") else Remote.Protocol.HTTPS
        )

    def __regex(self, pattern: str, index: int = 1) -> Optional[str]:
        match = re.search(pattern, self.__url)
        return match.group(index) if match else None

    @property
    def supported(self) -> bool:
        return (
            self.__protocol == Remote.Protocol.HTTPS
            and self.__url.startswith("codecommit:")
            or self.__protocol == Remote.Protocol.SSH
            and self.__url.startswith("ssh://")
        ) and self.name != ""

    @property
    def url(self) -> str:
        return self.__url

    @property
    def region(self) -> Optional[str]:
        if not self.__region:
            if self.__protocol == Remote.Protocol.HTTPS:
                self.__region = self.__regex(r"^codecommit::(.*)://")
            elif self.__protocol == Remote.Protocol.SSH:
                self.__region = self.__regex(r"ssh://git-codecommit.(.*).amazonaws.com")

        return self.__region

    @property
    def profile(self) -> Optional[str]:
        if self.__profile == "":
            self.__profile = self.__regex(r"//(.*)@")

        return self.__profile

    @property
    def name(self) -> str:
        if not self.__name:
            if self.__protocol == Remote.Protocol.HTTPS:
                name = self.__regex(r"(\/\/|.*@)(.*)$", 2)
            elif self.__protocol == Remote.Protocol.SSH:
                name = self.__regex(r"/([^/]*)$", 1)

            if name:
                self.__name = name

        return self.__name

    @property
    def codecommit_url(self) -> str:
        return f"https://{self.region}.console.aws.amazon.com/codesuite/codecommit/repositories/{self.name}"

    def pull_request_url(self, pull_request_id: int) -> str:
        return (
            self.codecommit_url
            + f"/pull-requests/{pull_request_id}/details?region={self.region}"
        )
