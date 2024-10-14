import slp_to_csv


def test_load_slp(centered_pair_predictions_path):
    loaded = slp_to_csv.load_slp(centered_pair_predictions_path)
    assert len(loaded) == 1100
    assert len(loaded.tracks) == 2


def test_convert_to_df(centered_pair_predictions_path):
    loaded = slp_to_csv.load_slp(centered_pair_predictions_path)
    df = slp_to_csv.convert_to_df(loaded)
    assert len(df) == 2200
    assert len(df.columns) == 51
    assert "video" in df.columns
    assert "frame" in df.columns
    assert "track" in df.columns
    assert "thorax_x" in df.columns
    assert "thorax_y" in df.columns
