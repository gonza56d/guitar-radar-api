from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    HEALTHY = 'HEALTHY', 'Guitar Radar API is working at 100%.'
    OUTAGE = 'OUTAGE', 'Guitar Radar API is down.'
    DEGRADED = 'DEGRADED', 'Guitar Radar API is working but some dependencies are down.'


@dataclass(kw_only=True)
class SQLHealthStatus:

    connected: bool
    implementation: str


@dataclass(kw_only=True)
class DocumentHealthStatus:

    connected: bool
    implementation: str


class OverallStatus:

    status: str
    status_description: str

    def __init__(self, status_option: Status):
        self.status = status_option.value[0]
        self.status_description = status_option.value[1]


@dataclass(kw_only=True)
class HealthStatus:

    sql_db_status: SQLHealthStatus
    document_db_status: DocumentHealthStatus
    overall_status: OverallStatus
