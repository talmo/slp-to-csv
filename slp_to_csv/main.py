"""Main module for SLP to CSV conversion."""

import sleap_io as sio
import pandas as pd


def load_slp(slp_path: str) -> sio.Labels:
    """Load SLP file into SLEAP Labels object.

    Args:
        slp_path: Path to SLP file.

    Returns:
        SLEAP Labels object.
    """
    return sio.load_file(slp_path)


def convert_to_df(labels: sio.Labels) -> pd.DataFrame:
    """Convert SLEAP Labels object to pandas DataFrame.

    Args:
        labels: SLEAP Labels object.

    Returns:
        Pandas DataFrame containing the equivalent of the SLEAP labels object.
    """
    df = []
    for lf in labels:
        video_ind = labels.videos.index(lf.video)

        for inst in lf:
            row = {
                "video": video_ind,
                "frame": lf.frame_idx,
                "track": inst.track.name if inst.track is not None else None,
            }
            for node, pt in inst.points.items():
                row[f"{node.name}_x"] = pt.x
                row[f"{node.name}_y"] = pt.y
            df.append(row)
    df = pd.DataFrame(df)
    return df
