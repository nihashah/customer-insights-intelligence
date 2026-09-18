from src.similarity import cosine_similarity


def cluster_feedback(records, similarity_threshold):
    """
    Group semantically similar customer feedback records.

    Each record is expected to contain:
    - feedback_id
    - embedding

    The threshold is supplied externally so it can be
    calibrated during evaluation rather than hard-coded.
    """

    clusters = []

    for record in records:
        best_cluster = None
        best_similarity = -1

        for cluster in clusters:
            representative = cluster[0]

            score = cosine_similarity(
                record["embedding"],
                representative["embedding"],
            )

            if score > best_similarity:
                best_similarity = score
                best_cluster = cluster

        if (
            best_cluster is not None
            and best_similarity >= similarity_threshold
        ):
            best_cluster.append(record)
        else:
            clusters.append([record])

    return clusters