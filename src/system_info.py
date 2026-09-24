"""Student-facing system information module for Lab 01.

Students should complete the missing implementations below.
"""

from __future__ import annotations


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
    raise NotImplementedError("Implement get_python_version().")


def get_platform_name() -> str:
    """Return the operating-system/platform name."""
    # TODO: implement this function.
    raise NotImplementedError("Implement get_platform_name().")


def normalize_name(name: str) -> str:
    """Return a normalized name suitable for display."""
    # TODO: implement this function.
    raise NotImplementedError("Implement normalize_name().")


def build_environment_report(name: str) -> dict:
    """
    Return a dictionary describing the execution environment.
    """
    # TODO: implement this function.
    raise NotImplementedError("Implement build_environment_report().")


if __name__ == "__main__":
    main()
