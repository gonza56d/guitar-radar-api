from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    HEALTHY = 'HEALTHY', 'Guitar Radar API is working at 100%.'
    OUTAGE = 'OUTAGE', 'Guitar Radar API is down.'
    DEGRADED = 'DEGRADED', 'Guitar Radar API is working but some dependencies are down.'


@dataclass
class DependencyStatus:

    connected: bool
    implementation: str


@dataclass
class OverallStatus:

    status: str | None = None
    status_description: str | None = None

    def __init__(self, status_option: Status):
        self.status = status_option.value[0]
        self.status_description = status_option.value[1]


@dataclass(kw_only=True)
class HealthStatus:

    statuses: list[DependencyStatus]
    overall_status: OverallStatus | None = None

    def __post_init__(self):
        statuses = [status.connected for status in self.statuses]
        status = Status.OUTAGE
        if any(statuses):
            status = Status.DEGRADED
        if all(statuses):
            status = Status.HEALTHY
        self.overall_status = OverallStatus(status)
