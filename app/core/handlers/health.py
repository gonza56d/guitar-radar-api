from app.core.commands import GetHealthCommand
from app.core.models.health import DependencyStatus, HealthStatus
from app.core.repositories.health import HealthRepository


class GetHealthHandler:

    health_repositories: list[HealthRepository]

    def __init__(self, *repositories):
        self.health_repositories = list(repositories)

    async def __call__(self, command: GetHealthCommand) -> HealthStatus:
        statuses = []
        for health in self.health_repositories:
            statuses.append(health.get_status())

        return HealthStatus(statuses=statuses)
