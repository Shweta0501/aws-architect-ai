from pathlib import Path

from app.services.architecture_loader import ArchitectureLoader
from app.services.diagram_service import DiagramService


def test_generate_aws_diagram(tmp_path):

    project_root = Path(__file__).resolve().parents[1]

    architecture_file = (
        project_root
        / "tests"
        / "fixtures"
        / "sample_architecture.json"
    )

    architecture = ArchitectureLoader.load_from_json(
        architecture_file
    )

    diagram_service = DiagramService()

    result = diagram_service.generate_diagram(
        architecture,
        output_directory=tmp_path,
    )

    assert result["png"].exists()