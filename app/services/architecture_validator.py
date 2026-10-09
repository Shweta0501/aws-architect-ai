from app.knowledge.aws_services import AWS_SERVICES
from app.models.architecture import Architecture


class ArchitectureValidator:
    def validate(self, architecture: Architecture) -> list[str]:
        errors = []

        known_services = set()

        for service in AWS_SERVICES.values():
            known_services.add(service["name"].lower())

            for alias in service.get("aliases", []):
                known_services.add(alias.lower())

        for component in architecture.components:
            if component.service.strip().lower() not in known_services:
                errors.append(
                    f"Unknown AWS service: {component.service}"
                )

        component_ids = {
            component.id for component in architecture.components
        }

        for connection in architecture.connections:
            if connection.source not in component_ids:
                errors.append(
                    f"Unknown source component: {connection.source}"
                )

            if connection.target not in component_ids:
                errors.append(
                    f"Unknown target component: {connection.target}"
                )

        return errors