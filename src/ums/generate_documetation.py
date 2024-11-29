import inspect
from fastapi import FastAPI
from typing import List
from ums.main import app
from ums.settings import settings


def generate_markdown_for_routes(app: FastAPI) -> List[str]:
    """
    Generates markdown documentation for FastAPI routes.
    """
    markdown_lines = ["# API Documentation\n"]
    markdown_lines.append("## Endpoints\n")

    for route in app.routes:
        if hasattr(route, "path") and hasattr(route, "methods"):
            endpoint_methods = ", ".join(route.methods - {"HEAD", "OPTIONS"})
            endpoint_summary = f"### `{endpoint_methods}` {route.path}\n"
            markdown_lines.append(endpoint_summary)

            # Add the handler function's docstring, if it exists
            if hasattr(route, "endpoint") and route.endpoint.__doc__:
                docstring = inspect.cleandoc(route.endpoint.__doc__)
                markdown_lines.append(f"{docstring}\n")

            # Add parameters if available
            if hasattr(route, "endpoint"):
                signature = inspect.signature(route.endpoint)
                if signature.parameters:
                    markdown_lines.append("#### Parameters:\n")
                    for param_name, param in signature.parameters.items():
                        param_info = f"- `{param_name}`: {param.annotation}"
                        markdown_lines.append(param_info)
                markdown_lines.append("\n")

    return markdown_lines


def write_markdown_to_file(markdown_lines: List[str], file_name: str):
    """
    Writes markdown documentation to a file.
    """
    with open(file_name, "w") as f:
        f.write("\n".join(markdown_lines))


if __name__ == "__main__":
    markdown_content = generate_markdown_for_routes(app)
    write_markdown_to_file(markdown_content, settings.file.endpoints_file)
