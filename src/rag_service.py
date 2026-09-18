from src.ai_service import client, create_embedding
from src.similarity import cosine_similarity


def retrieve_relevant_feedback(
    question,
    processed_records,
    top_k=5,
):
    """
    Retrieve customer feedback that is most
    semantically relevant to the PM's question.
    """

    question_embedding = create_embedding(question)

    scored_records = []

    for record in processed_records:

        score = cosine_similarity(
            question_embedding,
            record["embedding"],
        )

        scored_records.append(
            (score, record)
        )

    scored_records.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        record
        for _, record in scored_records[:top_k]
    ]


def answer_question(
    question,
    relevant_records,
):
    """
    Generate an answer grounded only in
    retrieved customer evidence.
    """

    evidence = "\n\n".join(
        (
            f"Feedback ID: {record['feedback_id']}\n"
            f"Source: {record['source']}\n"
            f"Segment: {record['customer_segment']}\n"
            f"Product Area: {record['product_area']}\n"
            f"Feedback: {record['feedback_text']}"
        )
        for record in relevant_records
    )

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": """
You are a Customer Insights assistant for Product Managers.

Answer the Product Manager's question using ONLY the
customer evidence supplied to you.

Rules:
- Do not invent customer evidence.
- If the evidence is insufficient, say so.
- Summarize patterns rather than making unsupported claims.
- Reference relevant Feedback IDs in your answer.
- Clearly distinguish customer problems from potential solutions.
""",
            },
            {
                "role": "user",
                "content": f"""
Product Manager question:

{question}

Retrieved customer evidence:

{evidence}
""",
            },
        ],
    )

    return response.output_text