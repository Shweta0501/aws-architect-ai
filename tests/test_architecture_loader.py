from pathlib import Path

from app.services.architecture_loader import ArchitectureLoader


def test_load_sample_architecture():
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

    assert architecture.application_name == "Secure Serverless Document Processing"
    assert len(architecture.components) == 9
    assert len(architecture.connections) == 8