from pathlib import Path

from graphviz import Digraph

from app.models.architecture import Architecture
from app.services.icon_service import IconService


class DiagramService:
    def __init__(self):
        self.icon_service = IconService()

    def generate_diagram(
        self,
        architecture: Architecture,
        output_directory: str | Path,
    ) -> dict[str, Path]:
        output_directory = Path(output_directory)
        output_directory.mkdir(parents=True, exist_ok=True)

        graph = Digraph(
            name=architecture.application_name.replace(" ", "_")
        )

        graph.attr(
            rankdir="TB",
            bgcolor="white",
            pad="0.2",
            nodesep="0.4",
            ranksep="0.5",
            splines="ortho",
            fontname="Arial",
            dpi="300",
        )

        graph.attr(
            "node",
            shape="none",
            margin="0",
        )

        graph.attr(
            "edge",
            color="#333333",
            arrowsize="0.7",
            penwidth="1.0",
            fontname="Arial Bold",
            fontsize="9",
            fontcolor="#222222"
        )

        for component in architecture.components:
            icon_path = self.icon_service.get_icon_path(
                component.service
            )

            graph.node(
                component.id,
                label=(
                    f'<<TABLE BORDER="0" CELLBORDER="0" '
                    f'CELLSPACING="0" CELLPADDING="2">'
                    f'<TR><TD WIDTH="42" HEIGHT="42">'
                    f'<IMG SRC="{icon_path}" SCALE="TRUE" '
                    f'WIDTH="38" HEIGHT="38"/>'
                    f'</TD></TR>'
                    f'<TR><TD><FONT FACE="Arial" POINT-SIZE="9">'
                    f'<B>{component.service}</B>'
                    f'</FONT></TD></TR>'
                    f'</TABLE>>'
                ),
                shape="plain",
            )

        for connection in architecture.connections:
            if connection.type == "supporting":
                graph.edge(
                    connection.source,
                    connection.target,
                    label=connection.label or "",
                    style="dashed",
                    color="#777777",
                    penwidth="1.0",
                    constraint="false",
                    arrowsize="0.5",
                )
            else:
                graph.edge(
                    connection.source,
                    connection.target,
                    label=connection.label or "",
                )

        output_path = output_directory / "aws_architecture"

        png_path = graph.render(
            str(output_path),
            format="png",
            cleanup=True,
        )

        return {
            "png": Path(png_path),
        }