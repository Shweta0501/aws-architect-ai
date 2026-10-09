from typing import List, Optional

from pydantic import BaseModel, Field


class ArchitectureComponent(BaseModel):
    id: str = Field(description="Unique identifier for the component")
    service: str = Field(description="Official AWS service name")
    purpose: str = Field(description="Purpose of this AWS service")
    layer: str = Field(
        default="application",
        description=(
            "Logical architecture layer for diagram placement. "
            "Use one of: edge, application, processing, storage, "
            "messaging, security, monitoring."
        ),
    )

class ArchitectureConnection(BaseModel):
    source: str = Field(description="ID of the source component")
    target: str = Field(description="ID of the target component")
    label: Optional[str] = Field(
        default=None,
        description="Short 2-4 word description of the connection",
    )
    type: str = Field(
        default="primary",
        description=(
            "Connection type. Use 'primary' for the main application "
            "data/request flow and 'supporting' for security, monitoring, "
            "permissions, encryption, auditing, or other secondary relationships."
        ),
    )


class Architecture(BaseModel):
    application_name: str = Field(
        description="Name of the application"
    )

    description: str = Field(
        description="Short description of the proposed architecture"
    )

    components: List[ArchitectureComponent] = Field(
        default_factory=list
    )

    connections: List[ArchitectureConnection] = Field(
        default_factory=list
    )