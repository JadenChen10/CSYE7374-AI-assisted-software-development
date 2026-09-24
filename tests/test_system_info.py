import pytest

from src.system_info import (
    build_environment_report,
    get_platform_name,
    get_python_version,
    normalize_name,
)


def test_get_python_version_returns_string():
    result = get_python_version()
    assert isinstance(result, str)
    assert result


def test_get_platform_name_returns_non_empty_string():
    result = get_platform_name()
    assert isinstance(result, str)
    assert result


def test_normalize_name_trims_whitespace_and_preserves_case():
    assert normalize_name("  alice  ") == "alice"
    assert normalize_name("  ALICE  ") == "ALICE"


def test_normalize_name_rejects_non_string_input():
    with pytest.raises((TypeError, ValueError)):
        normalize_name(123)


def test_normalize_name_rejects_empty_input_after_trim():
    with pytest.raises(ValueError):
        normalize_name("   ")


def test_build_environment_report_contains_expected_fields():
    report = build_environment_report("  Student User  ")

    assert set(report) == {"name", "python_version", "platform"}
    assert report["name"] == "Student User"
    assert report["python_version"] == get_python_version()
    assert report["platform"] == get_platform_name()


def test_build_environment_report_uses_normalized_name():
    report = build_environment_report("   Ada Lovelace   ")
    assert report["name"] == "Ada Lovelace"


def test_build_environment_report_rejects_invalid_input():
    with pytest.raises((TypeError, ValueError)):
        build_environment_report(123)
