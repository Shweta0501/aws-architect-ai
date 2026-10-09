import pytest

from app.knowledge.aws_service_catalog import AWS_SERVICE_CATALOG
from app.services.icon_service import IconService


def test_all_catalog_icons_exist():
    service = IconService()

    for service_id, metadata in AWS_SERVICE_CATALOG.items():
        if not metadata["diagram_supported"]:
            continue

        icon_path = service.get_icon_path(metadata["name"])

        assert icon_path.exists(), (
            f"Icon missing for {service_id}: {metadata['name']}"
        )


def test_unknown_service():
    service = IconService()

    with pytest.raises(ValueError):
        service.get_icon_path("AWS Some Fake Service")


def test_service_aliases_are_supported():
    service = IconService()

    test_cases = {
        "S3": "Amazon S3",
        "Lambda": "AWS Lambda",
        "Cognito": "Amazon Cognito",
        "DynamoDB": "Amazon DynamoDB",
        "API Gateway": "Amazon API Gateway",
        "Bedrock": "Amazon Bedrock",
        "IAM": "AWS Identity and Access Management",
    }

    for alias, expected_service in test_cases.items():
        icon_path = service.get_icon_path(alias)

        assert icon_path.exists()
        assert icon_path.name == next(
            metadata["icon"]
            for metadata in AWS_SERVICE_CATALOG.values()
            if metadata["name"] == expected_service
        )