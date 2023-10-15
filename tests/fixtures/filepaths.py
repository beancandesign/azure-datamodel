from pathlib import Path
import pytest


@pytest.fixture
def modelpath(tmp_path: Path):
    yield tmp_path / "model.json"
