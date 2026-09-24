"""Student-facing system information module for Lab 01.

Students should complete the missing implementations below.
"""

from __future__ import annotations

import platform
import sys


def main() -> None:
    """Run a small demonstration of the environment report workflow."""
    try:
        report = build_environment_report("Student User")
    except NotImplementedError:
        print("Complete the TODO implementations in src/system_info.py before running this demo.")
        return

    print("Environment report:")
    for key in ("name", "python_version", "platform"):
        print(f"- {key}: {report[key]}")


def get_python_version() -> str:
    """Return the running Python version."""
    # TODO: implement this function.
    # Read from the running interpreter, e.g. "3.11.9" — never hard-coded.
    return platform.python_version()


def get_platform_name() -> str:
    """Return the operating-system/platform name."""
    # TODO: implement this function.
    # platform.system() gives "Linux" / "Darwin" / "Windows"; it may return ""
    # when the value cannot be determined, so fall back to sys.platform.
    return platform.system() or sys.platform


def normalize_name(name: str) -> str:
    """Return a normalized name suitable for display."""
    # TODO: implement this function.
    if not isinstance(name, str):
        raise TypeError(f"name must be a string, got {type(name).__name__}")

    # Trim both ends and collapse internal runs of whitespace to a single
    # space; case is preserved as the user typed it.
    normalized = " ".join(name.split())
    if not normalized:
        raise ValueError("name must not be empty")
    return normalized


def build_environment_report(name: str) -> dict:
    """
    Return a dictionary describing the execution environment.
    """
    # TODO: implement this function.
    return {
        "name": normalize_name(name),
        "python_version": get_python_version(),
        "platform": get_platform_name(),
    }


if __name__ == "__main__":
    main()
