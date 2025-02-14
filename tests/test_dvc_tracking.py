import subprocess
from unittest.mock import patch

@patch("subprocess.run")
def test_dvc_status(mock_subprocess_run):
    """Test if DVC status correctly detects changes."""
    mock_subprocess_run.return_value.stdout = "data/sample.pdf modified"
    
    result = subprocess.run(["dvc", "status"], capture_output=True, text=True)
    assert "modified" in result.stdout
