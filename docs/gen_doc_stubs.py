#!/usr/bin/env python

from pathlib import Path
import mkdocs_gen_files
nav = mkdocs_gen_files.Nav()

for path in sorted(Path("ropython").glob("**/*.py")):
    if not path == "ropython/__init__.py"
        module_path = path.with_suffix("")
        doc_path = path.with_suffix(".md")
        nav_path = str(doc_path).replace("ropython", "reference")

        nav[module_path.parts] = str(nav_path)
        print(nav_path)
        with mkdocs_gen_files.open(nav_path, "w") as f:
            ident = ".".join(module_path.parts)
            data = "::: " + ident
            print(data, file=f)

# generated_nav = nav.build_literate_nav()

# nav_string = ""

# for nav_piece in generated_nav:
#     nav_piece = nav_piece.replace("[\\__init__]", "[\\_\\_init\\_\\_]")
#     nav_piece = nav_piece.replace("__init__.md", "/__init__.md")
#     nav_string += nav_piece


# with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
#     print(nav_string)
#     nav_file.write(nav_string)

# with mkdocs_gen_files.open("reference/SUMMARY.md", "r") as nav_file:
#     print(nav_file.read())
