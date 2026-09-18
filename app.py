import streamlit as st

from src.rag_service import (
    retrieve_relevant_feedback,
    answer_question,
)

from src.data_loader import load_feedback

from src.pipeline import process_feedback

st.set_page_config(
    page_title="Customer Insights Intelligence",
    page_icon="💡",
    layout="wide",
)

# Load customer feedback
feedback = load_feedback()

# Header
st.title("Customer Insights Intelligence")

st.caption(
    "Transform fragmented customer feedback into "
    "evidence-backed product opportunities."
)

st.divider()

# Evidence base
st.subheader("Customer Evidence Base")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Customer Signals", len(feedback))

with col2:
    st.metric("Feedback Sources", feedback["source"].nunique())

with col3:
    st.metric("Customer Segments", feedback["customer_segment"].nunique())

st.caption(
    "Signals consolidated across Support, NPS, Product Reviews, "
    "Sales, Customer Success, and User Research."
)

st.divider()

# Product intelligence
st.subheader("Product Opportunities")

st.caption(
    "Discover recurring customer problems across fragmented "
    "feedback and connect them to supporting evidence."
)

if "opportunities" not in st.session_state:
    st.session_state.opportunities = None


if st.button("Analyze Customer Feedback"):

    with st.spinner(
        "Analyzing customer signals and discovering product opportunities..."
    ):

        try:
            opportunities, processed_records = process_feedback(
                feedback,
                similarity_threshold=0.80,
            )

            st.session_state.opportunities = opportunities
            st.session_state.processed_records = processed_records

        except Exception as error:
            st.error(
                f"Analysis could not be completed: {error}"
            )


if st.session_state.opportunities:

    for opportunity in st.session_state.opportunities:

        with st.container(border=True):

            st.markdown(
                f"### {opportunity['problem_title']}"
            )

            st.write(
                opportunity["problem_statement"]
            )

            evidence = opportunity["evidence"]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Supporting Signals",
                    evidence["signal_count"],
                )

            with col2:
                st.metric(
                    "Feedback Sources",
                    len(evidence["sources"]),
                )

            with col3:
                st.metric(
                    "Customer Segments",
                    len(evidence["segments"]),
                )

            st.markdown(
                "**Potential Product Opportunity**"
            )

            st.write(
                opportunity["potential_opportunity"]
            )

            with st.expander(
                "View Supporting Evidence"
            ):

                st.write(
                    "**Evidence IDs:**",
                    ", ".join(
                        evidence["feedback_ids"]
                    ),
                )

                st.write(
                    "**Sources:**",
                    ", ".join(
                        evidence["sources"]
                    ),
                )

                st.write(
                    "**Segments:**",
                    ", ".join(
                        evidence["segments"]
                    ),
                )

                st.write(
                    "**Severity:**",
                    evidence["severity_counts"],
                )

else:

    st.info(
        "Run the AI analysis to discover recurring "
        "customer problems and product opportunities."
    )

st.divider()

# Investigation
st.subheader("Ask Customer Insights")

question = st.text_input(
    "Ask a question about your customer feedback",
    placeholder=(
        "Example: What problems are Enterprise customers "
        "experiencing with reporting?"
    ),
)

if st.button("Ask"):

    if not st.session_state.get("processed_records"):

        st.warning(
            "Run 'Analyze Customer Feedback' first "
            "so the customer evidence can be indexed."
        )

    elif not question:

        st.warning(
            "Enter a question first."
        )

    else:

        with st.spinner(
            "Searching customer evidence..."
        ):

            try:

                relevant_records = retrieve_relevant_feedback(
                    question,
                    st.session_state.processed_records,
                    top_k=5,
                )

                answer = answer_question(
                    question,
                    relevant_records,
                )

                st.markdown("### Answer")

                st.write(answer)

                with st.expander(
                    "View Retrieved Evidence"
                ):

                    for record in relevant_records:

                        st.markdown(
                            f"**{record['feedback_id']} — "
                            f"{record['source']}**"
                        )

                        st.write(
                            record["feedback_text"]
                        )

            except Exception as error:

                st.error(
                    f"Question could not be answered: {error}"
                )

st.divider()

# Raw evidence
with st.expander("View Raw Customer Evidence"):
    st.dataframe(
        feedback,
        use_container_width=True,
        hide_index=True,
    )