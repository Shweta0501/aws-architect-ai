from app.models.architecture import (
    Architecture,
    ArchitectureComponent,
    ArchitectureConnection,
)
from app.services.architecture_service import ArchitectureService


def test_generate_architecture_without_api_call(monkeypatch):

    mock_architecture = Architecture(
        application_name="Mock Serverless Application",
        description="Mock architecture for testing.",
        components=[
            ArchitectureComponent(
                id="lambda",
                service="AWS Lambda",
                purpose="Run backend logic.",
            ),
            ArchitectureComponent(
                id="dynamodb",
                service="Amazon DynamoDB",
                purpose="Store application data.",
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

    def mock_generate_architecture(self, requirement):
        return mock_architecture

    monkeypatch.setattr(
        "app.services.ai_service.AIService.generate_architecture",
        mock_generate_architecture,
    )

    service = ArchitectureService()

    architecture = service.generate(
        "Build a serverless application."
    )

    assert architecture.application_name == (
        "Mock Serverless Application"
    )

    assert len(architecture.components) == 2
    assert len(architecture.connections) == 1