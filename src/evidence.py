from collections import Counter


def aggregate_evidence(cluster):
    """
    Calculate factual evidence for a discovered
    customer-problem cluster.
    """

    signal_count = len(cluster)

    feedback_ids = [
        record["feedback_id"]
        for record in cluster
    ]

    sources = sorted({
        record["source"]
        for record in cluster
    })

    segments = sorted({
        record["customer_segment"]
        for record in cluster
    })

    product_areas = sorted({
        record["product_area"]
        for record in cluster
    })

    severity_counts = Counter(
        record["severity"]
        for record in cluster
        if record.get("severity")
    )

    return {
        "signal_count": signal_count,
        "feedback_ids": feedback_ids,
        "sources": sources,
        "segments": segments,
        "product_areas": product_areas,
        "severity_counts": dict(severity_counts),
    }