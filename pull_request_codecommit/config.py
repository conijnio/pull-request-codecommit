from typing import Dict, Optional

import configparser
from pathlib import Path


class Config:
    """
    Understands the configuration of the pull-request-codecommit tool.
    """

    __cached_config: Dict[str, Dict[str, str]] = {}
    __config_file: Optional[configparser.ConfigParser] = None

    @classmethod
    def __default_config(cls) -> Dict[str, str]:
        return cls.__load_config("default")

    @classmethod
    def __get_config_value(cls, profile: str, key: str) -> str:
        if profile not in cls.__cached_config:
            cls.__cached_config[profile] = cls.__default_config()
            cls.__cached_config[profile].update(cls.__load_config(profile))

        return cls.__cached_config[profile].get(key, "")

    @classmethod
    def __user_config(cls) -> configparser.ConfigParser:
        if not cls.__config_file:
            cls.__config_file = configparser.ConfigParser()
            cls.__config_file.read(f"{Path.home()}/.aws/pull-request-codecommit")

        return cls.__config_file

    @classmethod
    def __load_config(cls, profile: str) -> Dict[str, str]:
        config = {}

        if profile != "default":
            profile = f"profile {profile}"

        if profile in cls.__user_config().sections():
            for key, value in list(cls.__user_config().items(profile)):
                config[key] = value

        return config

    @classmethod
    def destination_branch(cls, profile: str) -> str:
        return cls.__get_config_value(profile, "branch")
