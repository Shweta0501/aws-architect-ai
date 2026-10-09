from pathlib import Path

from app.knowledge.aws_service_catalog import AWS_SERVICE_CATALOG


PROJECT_ROOT = Path(__file__).resolve().parents[2]

ICON_DIRECTORY = (
    PROJECT_ROOT
    / "assets"
    / "aws-icons"
)


AWS_SERVICES = AWS_SERVICE_CATALOG