# Customer Insights Intelligence — MVP PRD

## 1. Product Vision

Build an AI-powered Customer Insights Intelligence platform that transforms fragmented customer feedback into actionable insights and evidence-backed product opportunities.

The product is intended to help Product Managers understand recurring customer problems, investigate supporting evidence, and make better-informed product decisions.

---

## 2. Primary User

### Primary Persona

Product Managers working with moderate-to-large volumes of qualitative customer feedback across multiple channels.

### Responsibilities

The target Product Manager is responsible for:

- Understanding customer problems
- Conducting product discovery
- Identifying product opportunities
- Prioritizing problems and initiatives
- Defining experiments
- Contributing to roadmap decisions
- Measuring product outcomes

### Current Inputs

Customer insights may come from:

- Support tickets
- NPS / CSAT surveys
- Product reviews
- Sales conversations
- Customer Success feedback
- User research

---

## 3. Jobs to Be Done

### JTBD 1 — Discover Problems

When I receive large volumes of customer feedback across multiple channels,
I want to identify recurring customer problems,
so that I can determine which problems deserve deeper investigation.

### JTBD 2 — Understand Impact

When a recurring problem is identified,
I want to understand its frequency, severity, trend, and affected customer segments,
so that I can estimate its potential importance.

### JTBD 3 — Verify Evidence

When AI identifies a customer problem or opportunity,
I want to see the underlying customer evidence,
so that I can evaluate whether I trust the insight.

### JTBD 4 — Identify Opportunities

When customer evidence indicates a meaningful problem,
I want to convert that evidence into a clearly defined product opportunity,
so that I can decide whether to investigate, experiment, prioritize, or monitor it.

---

## 4. MVP User Journey

Customer Feedback
→ Feedback Ingestion
→ AI Analysis
→ Theme & Sentiment Identification
→ Customer Problem Detection
→ Evidence Linking
→ Product Opportunity
→ PM Review

A Product Manager should also be able to ask natural-language questions about the customer feedback and receive answers grounded in retrieved customer evidence.

---

## 5. MVP Functional Requirements

### FR1 — Feedback Ingestion

The system must accept a structured customer-feedback dataset.

For the MVP, feedback will be provided through CSV rather than production integrations.

### FR2 — AI Feedback Analysis

The system should analyze feedback and identify:

- Product area
- Customer problem/theme
- Sentiment
- Severity

### FR3 — Theme Aggregation

The system should group similar customer feedback into recurring themes or customer problems.

### FR4 — Evidence

Each identified customer problem should provide access to supporting customer-feedback records.

### FR5 — Product Opportunity

The system should transform significant customer problems into product-opportunity summaries containing:

- Problem
- Supporting evidence
- Affected customer segment
- Potential impact
- Potential hypothesis
- Recommended next investigation

### FR6 — Customer Insights Q&A

A Product Manager should be able to ask natural-language questions about the feedback dataset.

Example:

"What are enterprise customers saying about reporting?"

The system should retrieve relevant customer evidence and use that evidence to generate a grounded answer.

---

## 6. GenAI Requirements

The MVP will use a Large Language Model for qualitative feedback analysis and insight generation.

The system should demonstrate:

- Prompt design
- Structured LLM output
- Embeddings
- Semantic retrieval
- Retrieval-Augmented Generation (RAG)
- Evidence grounding
- Basic AI evaluation
- Human-in-the-loop decision making

AI-generated recommendations must be treated as decision support rather than autonomous product decisions.

---

## 7. MVP Scope

### Must Have

- Customer-feedback dataset
- Feedback analysis
- Theme identification
- Sentiment classification
- Severity classification
- Customer evidence
- Product-opportunity generation
- Basic PM dashboard
- Natural-language customer-insights Q&A
- Evidence-grounded answers

### Should Have

- Customer segment filtering
- Trend analysis
- Confidence indicators
- Opportunity scoring

### Future

- Zendesk integration
- Salesforce integration
- Jira / Linear integration
- Automated feedback ingestion
- Advanced opportunity scoring
- Roadmap recommendations
- Experiment recommendations
- Multi-user workspace

---

## 8. Non-Goals

The MVP will not:

- Respond directly to customer support tickets
- Replace customer-support agents
- Automatically modify a product roadmap
- Make autonomous prioritization decisions
- Integrate with production customer systems
- Process real customer PII
- Provide production-scale enterprise infrastructure

---

## 9. Success Metrics

### Product Metrics

- Time from feedback ingestion to actionable insight
- Number of evidence-backed opportunities reviewed
- Percentage of surfaced opportunities investigated by a PM

### AI Quality Metrics

- Theme classification accuracy
- Sentiment classification accuracy
- Retrieval relevance
- Evidence-grounding rate
- Unsupported-claim rate

### Technical Metrics

- LLM response latency
- Processing success rate
- Token usage
- Estimated cost per analysis

---

## 10. Product Principles

1. Customer problems before features.
2. Evidence before recommendations.
3. AI assists; Product Managers decide.
4. AI-generated insights should be traceable to customer evidence.
5. Uncertainty should be visible where appropriate.
6. Product opportunities should connect to measurable outcomes.

---

## 11. MVP Acceptance Criteria

The MVP will be considered successful when:

1. A customer-feedback CSV can be loaded into the application.
2. Feedback can be analyzed using an LLM.
3. Recurring customer themes can be surfaced.
4. A PM can inspect customer evidence supporting an insight.
5. The system can generate a product-opportunity summary.
6. A PM can ask a natural-language question about customer feedback.
7. The answer is grounded in retrieved customer evidence.
8. Basic AI-quality evaluation can be demonstrated.

---

## 12. Key Product Question

Can AI reduce the time required for Product Managers to move from fragmented customer feedback to evidence-backed product opportunities without removing human judgment from the product decision-making process?
