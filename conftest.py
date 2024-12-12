# conftest.py
import time
import pytest
from pytest_metadata.plugin import metadata_key

"""
    Configure pytest and add custom metadata to the HTML report.

    This function sets up global metadata that will appear in the pytest-html report,
    including project details, execution date, and testing environment. It also
    records the start time for calculating the total execution time.

    Args:
    config (Config): Pytest configuration object.
"""
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "E-Commerce Chatbot Testing"
    config.stash[metadata_key]["Author"] = "Sumit Soman"
    config.stash[metadata_key]["Execution Date"] = time.strftime("%Y-%m-%d:%H:%M:%S")
    config.stash[metadata_key]["Environment"] = "Test"
    config.stash[metadata_key]["Framework"] = "LangChain"

    config.start_time = time.time()

"""
    Modify metadata in the HTML report by removing default entries.

    This function removes unnecessary default metadata such as Python version,
    platform details, plugins, and others to make the report more concise.

    Args:
    metadata (dict): Metadata dictionary to be included in the report.
"""
def pytest_metadata(metadata):
    """Remove default metadata from the report."""
    metadata.pop("Python", None)
    metadata.pop("Platform", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("JAVA_HOME", None)

def pytest_html_report_title(report):
   report.title = 'E-Commerce Chatbot Execution Report'

"""
    Calculate and add total execution time to the HTML report.

    This function calculates the total time taken for the test session and
    appends it to the metadata section of the HTML report.

    Args:
    session (Session): Pytest session object.
    exitstatus (int): Exit status of the test session.
"""
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Calculate and add execution time to the report."""
    end_time = time.time()
    total_time = end_time - session.config.start_time  # Total execution time in seconds

    # Add the execution time to the metadata
    session.config.stash[metadata_key]["Total Execution time"] = f"{total_time:.2f} seconds"
