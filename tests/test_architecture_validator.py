import pytest

from app.models.architecture import (
    Architecture,
    ArchitectureComponent,
    ArchitectureConnection,
)
from app.services.architecture_validator import ArchitectureValidator
from app.models.architecture import Architecture, ArchitectureComponent

def test_valid_architecture():

    architecture = Architecture(
        application_name="Test Application",
        description="Test architecture",
        components=[
            ArchitectureComponent(
                id="lambda",
                service="AWS Lambda",
                purpose="Run backend logic",
            ),
            ArchitectureComponent(
                id="dynamodb",
                service="Amazon DynamoDB",
                purpose="Store data",
            ),
        ],
        connections=[
            ArchitectureConnection(
                source="lambda",
                target="dynamodb",
                label="Read / Write",
            )
        ],
    )

    validator = ArchitectureValidator()

    errors = validator.validate(architecture)

    assert errors == []


def test_unknown_service():

    architecture = Architecture(
        application_name="Test Application",
        description="Test architecture",
        components=[
            ArchitectureComponent(
                id="unknown",
                service="AWS Fake Service",
                purpose="Test",
            )
        ],
        connections=[],
    )

    validator = ArchitectureValidator()

    errors = validator.validate(architecture)

    assert "Unknown AWS service: AWS Fake Service" in errors


def test_invalid_connection():

    architecture = Architecture(
        application_name="Test Application",
        description="Test architecture",
        components=[
            ArchitectureComponent(
                id="lambda",
                service="AWS Lambda",
                purpose="Run backend logic",
            )
        ],
        connections=[
            ArchitectureConnection(
                source="lambda",
                target="does_not_exist",
                label="Test",
            )
        ],
    )

    validator = ArchitectureValidator()

    errors = validator.validate(architecture)

    assert (
        "Unknown target component: does_not_exist"
        in errors
    )

def test_validator_accepts_service_alias():
    architecture = Architecture(
        application_name="Alias Test",
        description="Test architecture using an AWS service alias.",
        components=[
            ArchitectureComponent(
                id="storage",
                service="S3",
                purpose="Store application files.",
            )
        ],
        connections=[],
    )

    validator = ArchitectureValidator()

    errors = validator.validate(architecture)

    assert errors == []