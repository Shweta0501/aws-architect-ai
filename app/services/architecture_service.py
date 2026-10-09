from app.models.architecture import Architecture
from app.services.ai_service import AIService
from app.services.architecture_validator import ArchitectureValidator


class ArchitectureService:

    def __init__(self):

        self.ai_service = AIService()
        self.validator = ArchitectureValidator()

    def generate(
        self,
        requirement: str
    ) -> Architecture:

        if not requirement.strip():

            raise ValueError(
                "Application requirement cannot be empty."
            )

        architecture = (
            self.ai_service.generate_architecture(
                requirement
            )
        )

        errors = self.validator.validate(
            architecture
        )

        if errors:

            raise ValueError(
                "Architecture validation failed:\n"
                + "\n".join(errors)
            )

        return architecture