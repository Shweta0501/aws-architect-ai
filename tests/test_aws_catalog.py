from app.knowledge.aws_service_catalog import AWS_SERVICE_CATALOG


def test_service_catalog_is_not_empty():

    assert AWS_SERVICE_CATALOG


def test_required_service_information_exists():

    required_fields = {
        "name",
        "category",
        "description",
        "icon",
    }

    for service_id, service in AWS_SERVICE_CATALOG.items():

        assert required_fields.issubset(
            service.keys()
        ), f"Missing fields for {service_id}"


def test_core_services_are_registered():

    expected_services = {
        "amazon_s3",
        "aws_lambda",
        "amazon_dynamodb",
        "amazon_api_gateway",
        "amazon_cloudfront",
        "amazon_sns",
    }

    assert expected_services.issubset(
        AWS_SERVICE_CATALOG.keys()
    )