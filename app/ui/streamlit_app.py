from pathlib import Path

import streamlit as st

from app.services.architecture_service import ArchitectureService
from app.services.diagram_service import DiagramService


st.set_page_config(
    page_title="AI AWS Architect",
    page_icon="☁️",
    layout="wide",
)


st.title("☁️ AI AWS Architect")

st.write(
    "Describe your application requirement and generate "
    "an AWS architecture."
)


requirement = st.text_area(
    "Describe your application",
    placeholder=(
        "Example: Build a serverless application where users "
        "upload documents and receive notifications when "
        "processing is complete."
    ),
    height=180,
)


if st.button("Generate Architecture", type="primary"):

    if not requirement.strip():

        st.warning(
            "Please describe your application first."
        )

    else:

        try:

            architecture_service = ArchitectureService()

            with st.spinner(
                "Designing your AWS architecture..."
            ):

                architecture = (
                    architecture_service.generate(
                        requirement
                    )
                )

            st.success(
                "Architecture generated successfully!"
            )

            st.subheader(
                architecture.application_name
            )

            st.write(
                architecture.description
            )

            project_root = (
                Path(__file__).resolve().parents[2]
            )

            output_directory = (
                project_root / "output"
            )

            diagram_service = DiagramService()

            result = diagram_service.generate_diagram(
                architecture,
                output_directory=output_directory,
            )

            st.subheader(
                "AWS Architecture Diagram"
            )

            st.image(
                str(result["png"]),
                caption="AWS Architecture",
                use_container_width=True,
            )

        except Exception as error:

            st.error(
                f"Unable to generate architecture: {error}"
            )