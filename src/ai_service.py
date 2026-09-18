import os
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class FeedbackAnalysis(BaseModel):
    theme: str
    customer_problem: str
    sentiment: Literal["Positive", "Neutral", "Negative"]
    severity: Literal["Low", "Medium", "High"]


def analyze_feedback(
    feedback_text: str,
    product_area: str
) -> FeedbackAnalysis:
    """
    Interpret one customer signal without forcing it
    into a predefined problem taxonomy.
    """

    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": """
You analyze qualitative customer feedback for Product Managers.

Your job is to identify what the customer is actually experiencing.

Rules:
- Identify the underlying customer problem.
- Do not propose a feature or solution.
- Do not force the feedback into a predefined taxonomy.
- Keep the theme concise.
- Base the analysis only on the supplied evidence.
- Do not invent customer impact that is not stated or reasonably supported.
""",
            },
            {
                "role": "user",
                "content": f"""
Product area: {product_area}

Customer feedback:
{feedback_text}
""",
            },
        ],
        text_format=FeedbackAnalysis,
    )

    return response.output_parsed

def create_embedding(text: str) -> list[float]:
    """
    Convert text into a numerical embedding
    for semantic similarity comparison.
    """

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding

class ProblemSynthesis(BaseModel):
    problem_title: str
    problem_statement: str
    potential_opportunity: str


def synthesize_problem(feedback_items: list[str]) -> ProblemSynthesis:
    """
    Synthesize a group of related customer signals
    into an evidence-backed customer problem.
    """

    evidence = "\n".join(
        f"- {item}" for item in feedback_items
    )

    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": """
You synthesize related customer feedback for Product Managers.

Based only on the supplied customer evidence:

1. Create a concise customer problem title.
2. Describe the underlying customer problem.
3. Identify a potential product opportunity.

Rules:
- Do not invent evidence.
- Separate the customer problem from the proposed opportunity.
- The problem statement must describe the customer need or friction.
- The opportunity should describe a direction worth investigating,
  not prescribe a detailed feature.
""",
            },
            {
                "role": "user",
                "content": f"""
Customer evidence:

{evidence}
""",
            },
        ],
        text_format=ProblemSynthesis,
    )

    return response.output_parsed