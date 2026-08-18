import logging
import pytest

def test_uploaded_files_tab(check_uploaded_files):

    upload, file_types = check_uploaded_files
    if file_types is None:
        logging.info("🔹 Skipping assertions as the test was already started and file search was skipped.")
        pytest.skip("Skipping assertions as the test was already started and file search was skipped.")

    assert upload.search_input.is_visible(), "Search input should be visible on the uploaded files page"
    assert upload.uploaded_files_table.is_visible(), "Uploaded files table should be visible"
    assert upload.rows.count() > 0, "Expected at least one row in the uploaded files results"
    assert file_types, "Expected at least one uploaded file type from search results"
    assert "azm" in file_types, f"Expected 'azm' file type in search results; got {file_types}"
    assert "csv" in file_types, f"Expected 'csv' file type in search results; got {file_types}"
    assert "sig1" in file_types, f"Expected 'sig1' file type in search results; got {file_types}"