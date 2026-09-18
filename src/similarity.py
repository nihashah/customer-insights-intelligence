import numpy as np


def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two embedding vectors.

    Higher values indicate greater semantic similarity.
    """

    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )