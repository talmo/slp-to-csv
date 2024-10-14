import slp_to_csv


def test_load_slp(centered_pair_predictions_path):
    loaded = slp_to_csv.load_slp(centered_pair_predictions_path)
    assert len(loaded) == 1100
    assert len(loaded.tracks) == 2
