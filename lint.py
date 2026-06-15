import tempfile
import subprocess
import os

def run_pyflakes(code):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".py",
        mode="w",
        encoding="utf-8"
    ) as f:

        f.write(code)
        filename = f.name

    result = subprocess.run(
        ["pyflakes", filename],
        capture_output=True,
        text=True
    )

    os.unlink(filename)

    if result.stdout.strip():
        return result.stdout

    return "No issues found"