from pathlib import Path
import mkdocs_gen_files
nav = mkdocs_gen_files.Nav()


for path in sorted(Path("ropython").glob("**/*.py")):
    module_path = path.with_suffix("")
    doc_path = path.with_suffix(".md")
    nav_path = str(doc_path).replace("ropython", "reference")

    nav[module_path.parts] = str(nav_path)
    print(nav_path)
    with mkdocs_gen_files.open(nav_path, "w") as f:
        ident = ".".join(module_path.parts)
        data = "::: " + ident
        print(data, file=f)