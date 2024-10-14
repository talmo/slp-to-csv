import slp_to_csv


def test_version():
    version = slp_to_csv.__version__
    assert len(version.split(".")) == 3
