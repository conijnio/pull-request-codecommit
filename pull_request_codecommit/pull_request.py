from typing import Optional

from .pull_request_codecommit import PullRequestCodeCommit
from .pull_request_proposal import PullRequestProposal
from .repository import Repository
from .git import Commits


class PullRequest:
    """
    Understands pull requests
    """

    def __init__(self, repo: Repository) -> None:
        self.__repo: Repository = repo
        self.__proposal: Optional[PullRequestProposal] = None
        self.__commits: Commits = self.__repo.commits()
        self.__pull_request: PullRequestCodeCommit = PullRequestCodeCommit(
            repository=repo
        )

    @property
    def proposal(self) -> PullRequestProposal:
        if not self.__proposal:
            self.__proposal = PullRequestProposal(self.__pull_request, self.__commits)

        return self.__proposal

    @property
    def title(self) -> str:
        return self.proposal.title

    @property
    def description(self) -> str:
        return self.proposal.description

    @property
    def link(self) -> str:
        return self.__pull_request.link

    @property
    def has_changes(self) -> bool:
        return True if self.__commits.first else False

    def save(self) -> None:
        self.__repo.push()
        self.__pull_request.save(self.title, self.description)

    def update(self, title: str, description: str) -> None:
        self.proposal.update(title=title, description=description)

    def merge(self) -> str:
        return self.__pull_request.merge()
