import re
from typing import Optional


class Remote:
    """
    Understands remote CodeCommit URLs
    """

    def __init__(self, url: str):
        self.__url: str = url
        self.__region: Optional[str] = ""
        self.__profile: Optional[str] = ""
        self.__name: str = ""

    def __regex(self, pattern: str, index: int = 1) -> Optional[str]:
        match = re.search(pattern, self.__url)
        return match.group(index) if match else None

    @property
    def supported(self) -> bool:
        return self.__url.startswith("codecommit:") and self.name != ""

    @property
    def url(self) -> str:
        return self.__url

    @property
    def region(self) -> Optional[str]:
        if not self.__region:
            self.__region = self.__regex(r"^codecommit::(.*)://")

        return self.__region

    @property
    def profile(self) -> Optional[str]:
        if self.__profile == "":
            self.__profile = self.__regex(r"//(.*)@")

        return self.__profile

    @property
    def name(self) -> str:
        if not self.__name:
            name = self.__regex(r"(\/\/|.*@)(.*)$", 2)

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
