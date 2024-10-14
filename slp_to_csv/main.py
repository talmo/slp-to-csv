"""Main module for SLP to CSV conversion."""

import sleap_io as sio


def load_slp(slp_path: str) -> sio.Labels:
    """Load SLP file into SLEAP Labels object.
    Args:
        slp_path: Path to SLP file.
    Returns:
        SLEAP Labels object.
    """
    return sio.load_file(slp_path)
