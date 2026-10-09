import json
from pathlib import Path

from app.models.architecture import Architecture


class ArchitectureLoader:

    @staticmethod
    def load_from_json(file_path: str | Path) -> Architecture:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Architecture file not found: {path}"
            )

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return Architecture.model_validate(data)