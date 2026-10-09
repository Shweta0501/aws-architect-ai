from pathlib import Path

from app.knowledge.aws_services import AWS_SERVICES, ICON_DIRECTORY


class IconService:
    def get_icon_path(self, service_name: str) -> Path:
        requested_name = service_name.strip().lower()

        for service in AWS_SERVICES.values():
            registered_name = service["name"].lower()

            if requested_name == registered_name:
                return self._get_icon_path(service)

            for alias in service.get("aliases", []):
                if requested_name == alias.lower():
                    return self._get_icon_path(service)

        raise ValueError(f"AWS service is not registered: {service_name}")

    @staticmethod
    def _get_icon_path(service: dict) -> Path:
        icon_path = ICON_DIRECTORY / service["icon"]

        if not icon_path.exists():
            raise FileNotFoundError(
                f"Icon file not found for {service['name']}: {icon_path}"
            )

        return icon_path