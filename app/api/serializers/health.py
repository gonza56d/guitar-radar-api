from pydantic import BaseModel

from app.api.serializers.base import ResponseModel
from app.core.models.health import OverallStatus


class DependencyStatusModel(BaseModel):

    connected: bool
    implementation: str


class OverallStatusModel(BaseModel):

    status: str | None = None
    status_description: str | None = None


class HealthStatusResponse(ResponseModel):

    sql_db_status: DependencyStatusModel
    document_db_status: DependencyStatusModel
    overall_status: OverallStatus | None = None
