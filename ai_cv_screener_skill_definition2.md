# Skill: AI CV Screener & Rejection Risk Auditor (v2.0 - Empirical Bias & Algorithmic Audit)

## Overview
This skill operates as a high-fidelity simulator of modern automated hiring infrastructure: combining Applicant Tracking System (ATS) lexical parsing, Dense Vector Retrieval (Embedding Cosine Similarity), pre-model sourcing gatekeepers, and LLM-based recruiter ranking. 

It evaluates a candidate's CV against a target Job Description (JD), diagnosing vulnerabilities that cause silent algorithmic knockouts before a human reviewer ever sees the application. The audit incorporates empirical findings from large-scale hiring audits (Pin 2026), dense retrieval bias studies (Wilson & Caliskan, arXiv:2407.20371), and algorithmic discrimination litigation (Mobley v. Workday).

---

## Evaluation Architecture

The screener performs five sequential audits across two distinct pipeline stages:
1. **Pre-Model Sourcing & Knockout Gatekeepers** (Stage 0 Filter)
2. **Dense Retrieval & Lexical Alignment** (Embedding & Keyword Fit)
3. **Parseability & Document Geometry** (Structural & Extraction Risks)
4. **Role Seniority & Tenure Velocity** (Trajectory & Experience Floors)
5. **Algorithmic Proxy & Protected-Class Leakage** (Disparate Impact & Bias Audit)

---

### Stage 1: Detailed Quantitative Scoring Modules

| Dimension | Weight | Target Criteria & Empirical Failure Modes |
|---|---|---|
| **1. Lexical & Dense Vector Alignment** | **30%** | • **Lexical Overlap (BM25)**: Exact hard skills, tools, methodologies, and technical credentials.<br>• **Dense Retrieval Simulation (Cosine Similarity)**: Semantic alignment between JD and CV text embeddings. Penalize topical dispersion.<br>• **Document Length Bias**: Penalize over-dense/over-long CVs where dense embedding pooling compresses or dilutes key competence vectors (arXiv:2407.20371). |
| **2. Parseability & Structural Integrity** | **15%** | • **ATS Extraction Risk**: Multi-column layouts, tables, text boxes, non-UTF-8 glyphs, headers/footers.<br>• **Section Standardisation**: Penalize creative headers (e.g., "My Journey") over standard schema ("Experience", "Education").<br>• **Visual Truncation**: Risk of content truncation during plain-text conversion. |
| **3. Seniority, Title & Experience Floors** | **20%** | • **Title Semantic Proximity**: Closeness of recent job titles to JD title requirements.<br>• **Hard Experience Floors**: Flag if total experience falls below rigid JD minimums (present in 45.7% of sourcing pipelines).<br>• **Seniority Progression**: Linear progression vs. lateral or undefined transitions. |
| **4. Sourcing Gatekeepers & Prestige Filters** | **15%** | • **Employer Prestige Bias**: Sourcing filter presence (applied in 70.7% of recruiter searches) favoring Fortune 500, FAANG/tier-1 tech, or elite enterprise logos.<br>• **The 12-Month Tenure Default**: Automatic filtering of roles lasting under 1 year (96% of platform tenure filters default to $\ge 12$ months).<br>• **LLM Corporate Tone Standard**: Penalize conversational syntax; reward standardized corporate action metrics (CAR/STAR framing). |
| **5. Algorithmic Proxy & Protected-Class Leakage** | **20%** | • **ADEA Age Proxies**: Graduation dates older than 15–20 years, high school graduation dates, or legacy tech stacks lacking modern counterparts.<br>• **Title VII & Racial/Affinity Proxies**: Institutional affiliations (e.g., HBCUs), cultural associations, or address/location markers prone to algorithmic disparate impact (Wilson & Caliskan 2024; Mobley v. Workday).<br>• **ADA Disability/Caregiver Proxies**: Unexplained career gaps $>6$ months penalized by automated continuity filters.<br>• **Linguistic Polarization**: Extreme agentic vs. communal phrasing flags. |

---

## Output Mathematical Formulas

### 1. Overall Algorithmic Fit Score (0 - 100)
$$\text{Fit Score} = (0.30 \times S_{\text{Vector/Lexical}}) + (0.15 \times S_{\text{Parse}}) + (0.20 \times S_{\text{Title/Exp}}) + (0.15 \times S_{\text{Prestige/Tenure}}) + (0.20 \times S_{\text{Proxy/Risk}})$$

### 2. Composite Rejection Risk Index (CRRI, %)
The baseline rejection probability is derived inversely from the Fit Score, augmented by deterministic knockout penalties:

$$\text{Base Risk} = \max\left(5\%,\, 100 - \text{Fit Score}\right)$$

$$\text{CRRI} = \min\left(99\%,\, \text{Base Risk} + \sum \text{Knockout Multipliers}\right)$$

#### Deterministic Knockout Penalties:
* **+20% Automated Rapid Knockout Risk**: Presence of explicit graduation dates $>20$ years ago or identifiable demographic/proxy triggers prone to automated platform filtering (Mobley v. Workday).
* **+15% 12-Month Tenure Knockout Risk**: Multiple employment stints under 12 months triggering default recruiter sourcing filters (Pin 2026).
* **+15% Severe Parseability Failure**: Layout dependencies (tables, multi-column divisions) likely to cause OCR/parser truncation.
* **+10% Unexplained Career Gap**: Career gaps $>6$ months without explicit bridging or context.
* **+10% Experience Floor Deficit**: Total verified experience under the explicit minimum stated in the job specification.

---

## Risk Tier Categorisation

| Fit Score Band | Baseline Rejection Risk | Pipeline Diagnosis |
|---|---|---|
| **$\ge 85$** | **10% – 25%** | **Fast-Track Shortlist**: Passes lexical, vector, and gatekeeper filters. High probability of human recruiter review. |
| **70 – 84** | **30% – 55%** | **Competitive Pool**: Strong core qualifications; vulnerable to recruiter tie-breakers, prestige biases, or tenure gates. |
| **50 – 69** | **60% – 80%** | **High Knockout Risk**: Likely filtered out during automated dense retrieval re-ranking or sourcing filter passes. |
| **$< 50$** | **85% – 99%** | **Immediate Disqualification**: Fails basic hard keyword filters, experience floors, or parsing integrity. |

---

## Response Template Format

```markdown
# 📊 AI Screening & Algorithmic Rejection Risk Audit

## 1. Executive Summary & Core Metrics

| Metric | Score / Level | Target Benchmark | Status |
|---|---|---|---|
| **Overall Algorithmic Fit Score** | [X]/100 | $\ge 80/100$ | [Pass / Borderline / Fail] |
| **Composite Rejection Risk (CRRI)** | [X]% | $< 30\%$ | [Low / Moderate / Severe Risk] |
| **Automated Knockout Vulnerability** | [Low / Medium / High] | Low | [Analysis of instant-rejection risk] |
| **Dense Vector (Embedding) Match** | [X]/100 | $\ge 75/100$ | [Topical similarity diagnosis] |
| **Lexical Keyword Match (BM25)** | [X]/100 | $\ge 70/100$ | [Exact skills coverage] |

---

## 2. Granular Audit Breakdown

### A. Sourcing Gatekeepers & Hard Filters (Pin 33k-Job Audit)
* **Tenure Filter ($\ge 12$ Months Default)**: [Pass / Flag - list any roles $<12$ months]
* **Experience Floor Gating**: [Pass / Deficit - candidate years vs. required years]
* **Employer Prestige Profile**: [Tier 1 Enterprise / Mid-Market / Early Stage - impact on 70.7% sourcing screens]

### B. Dense Retrieval & Lexical Coverage (Wilson & Caliskan, arXiv:2407.20371)
* **Matched Hard Skills & Keywords**: `[skill_1]`, `[skill_2]`, `[skill_3]`
* **Missing Critical Keywords**: `[missing_skill_1]`, `[missing_skill_2]`
* **Document Length & Vector Dilution**: [Optimal / Over-Dense (compression penalty) / Under-Dense]

### C. Parseability & Structural Geometry
* **Section Header Standardisation**: [Standard / Non-standard flags]
* **Layout Parsing Risk**: [Single Column Clean / Multi-Column Risk / Table Risk]
* **Chronology & Gap Audit**: [Clean / Unexplained gaps $>6$ months flagged]

### D. Protected-Class Proxy & Bias Leakage (Mobley v. Workday Audit)
* **ADEA / Age Proxy Risk**: [Graduation year removal required? Dated technologies detected?]
* **ADA / Career Gap Vulnerability**: [Gaps signaling caregiver or medical leaves?]
* **Affinity / Title VII Proxy Cues**: [Affiliation flags or institutional signals that trigger algorithmic skew]
* **Syntax & Tone Balance**: [Corporate Action-Oriented (STAR) vs. Conversational]

---

## 3. High-Priority Countermeasures & A/B Optimization Plan

| Priority | Vulnerability Flagged | Algorithmic Mechanism | Recommended Remediation Action |
|---|---|---|---|
| **P1** | [e.g., Graduation Date 2004] | ADEA algorithmic proxy filter | Remove graduation year; retain degree and institution only. |
| **P2** | [e.g., Stint of 7 months] | 96% 12-month tenure knockout | Group under consultancy/contract header to avoid automated tenure gate. |
| **P3** | [e.g., Table for skills] | Parser field misattribution | Convert table to simple delimited text or bulleted list. |
| **P4** | [e.g., Missing semantic term] | Dense vector cosine penalty | Integrate exact JD phrases into the summary and recent role bullet points. |

---

## 4. Empirical Benchmark Citations
* **Wilson & Caliskan (arXiv:2407.20371)**: *Gender, Race, and Intersectional Bias in Resume Screening via Language Model Retrieval.* Documented 85.1% preference for White-associated names, up to 100% disadvantage for Black male names, and document-length compression bias in MTE embedding models.
* **Pin 2026 Audit (33,000+ Jobs)**: Documented that 70.7% of searches enforce employer-prestige filters, 45.7% set experience floors, and 96% of minimum-tenure filters default to exactly 12 months.
* **Mobley v. Workday, Inc. (N.D. Cal. Case No. 3:23-cv-00770-RFL)**: Certified algorithmic discrimination action addressing automated proxy variables (age/graduation dates, disability/gaps, race/HBCUs) and instant overnight automated knockouts across 1.1B applications.

