from .git import Commits
from .pull_request_codecommit import PullRequestCodeCommit

SPLITTER = """
#=
#= Existing pull request found: #{{PULL_REQUEST_ID}}
#=
#= Author: {{AUTHOR}}
#=
#= Above you will see the title and description of the existing pull request.
#= Below you will find the newly proposed description.
#=
"""


class PullRequestProposal:
    def __init__(self, pull_request: PullRequestCodeCommit, commits: Commits):
        self.__title = ""
        self.__description = ""
        self.__pull_request = pull_request
        self.__commits = commits

    @property
    def title(self) -> str:
        if self.__title:
            return self.__title

        if self.__pull_request.title:
            return self.__pull_request.title

        return self.__generate_title()

    def __generate_title(self) -> str:
        if not self.__commits.first:
            return ""

        title = self.__commits.first.message.subject

        if self.__commits.issues:
            title += f" ({', '.join(self.__commits.issues)})"

        return title

    @property
    def description(self) -> str:
        if self.__description:
            return self.__description

        if (
            len(self.__commits) == 1
            and self.__commits.first
            and not self.__pull_request.description
        ):
            return self.append_issues(self.__commits.first.message.body)

        return self.__merge_descriptions(
            existing_description=self.__pull_request.description,
            description=self.__generate_description(),
        )

    def append_issues(self, description: str) -> str:
        if not self.__commits.issues:
            return description

        splitter = "\n\n" if description else ""
        issues = "Issues: " + ", ".join(self.__commits.issues)

        return description + splitter + issues

    def __generate_description(self):
        return self.append_issues(
            "\n".join(list(map(lambda commit: commit.message.subject, self.__commits)))
        )

    def __merge_descriptions(self, existing_description: str, description: str) -> str:
        if not existing_description:
            return description

        splitter = SPLITTER.replace(
            "{{PULL_REQUEST_ID}}", str(self.__pull_request.pull_request_id)
        )
        splitter = splitter.replace("{{AUTHOR}}", self.__pull_request.author)
        return existing_description + splitter + description

    def update(self, title: str, description: str):
        self.__title = title
        self.__description = self.__remove_comments(description)

    @staticmethod
    def __remove_comments(description: str) -> str:
        return "\n".join(
            filter(lambda line: not line.startswith("#="), description.split("\n"))
        )
