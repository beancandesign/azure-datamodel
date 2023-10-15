import json
import pytest


from oswdatamodel.model import Model


@pytest.mark.usefixtures("model", "modelpath")
class TestSerializeModel:
    def test_build_model_success(self, model):
        assert isinstance(model, Model)

    def test_serialize_success(self, model, modelpath):
        with open(modelpath, "w") as f:
            f.write(model.model_dump_json(indent=4))
        # Load from disk
        with open(modelpath, "r") as f:
            lines = f.read()
            loaded = Model.model_validate_json(lines)
        assert model
