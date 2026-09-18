from pathlib import Path

import pandas as pd


DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "customer_feedback.csv"
)


def load_feedback():
    """Load customer feedback from the MVP knowledge base."""
    return pd.read_csv(DATA_PATH)