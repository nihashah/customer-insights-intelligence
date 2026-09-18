from src.ai_service import (
    analyze_feedback,
    create_embedding,
    synthesize_problem,
)

from src.problem_discovery import cluster_feedback
from src.evidence import aggregate_evidence

def process_feedback(feedback_df, similarity_threshold):
    """
    Run the end-to-end customer intelligence pipeline.

    WARNING:
    This function makes OpenAI API calls.
    Do not execute until API testing is enabled.
    """

    processed_records = []
    print(f"Input records: {len(feedback_df)}")

    # STEP 1:
    # Interpret each customer signal and create its embedding.
    for _, row in feedback_df.iterrows():

        analysis = analyze_feedback(
            row["feedback_text"],
            row["product_area"],
        )

        semantic_text = (
            f"Product area: {row['product_area']}\n"
            f"Customer problem: {analysis.customer_problem}\n"
            f"Original evidence: {row['feedback_text']}"
        )

        embedding = create_embedding(
            semantic_text
        )

        processed_records.append({
            "feedback_id": row["feedback_id"],
            "date": row["date"],
            "source": row["source"],
            "customer_segment": row["customer_segment"],
            "product_area": row["product_area"],
            "feedback_text": row["feedback_text"],
            "theme": analysis.theme,
            "customer_problem": analysis.customer_problem,
            "sentiment": analysis.sentiment,
            "severity": analysis.severity,
            "embedding": embedding,
        })
        print(
    f"Processed {len(processed_records)}/{len(feedback_df)} "
    f"- {row['feedback_id']}")

        # STEP 2:
    # Discover groups of semantically related customer signals.
    clusters = cluster_feedback(
        processed_records,
        similarity_threshold,
    )

    print(f"Clusters discovered: {len(clusters)}")

    for i, cluster in enumerate(clusters, start=1):
        print(
            f"Cluster {i}: "
            f"{[record['feedback_id'] for record in cluster]}"
        )

    opportunities = []

    # STEP 3:
    # Convert each discovered cluster into product intelligence.
    for cluster in clusters:

        feedback_items = [
            record["feedback_text"]
            for record in cluster
        ]

        synthesis = synthesize_problem(
            feedback_items
        )

        evidence = aggregate_evidence(
            cluster
        )

        opportunities.append({
            "problem_title": synthesis.problem_title,
            "problem_statement": synthesis.problem_statement,
            "potential_opportunity": synthesis.potential_opportunity,
            "evidence": evidence,
        })

    print(
        f"Opportunities generated: {len(opportunities)}"
    )

    return opportunities, processed_records