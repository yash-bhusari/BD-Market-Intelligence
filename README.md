# BD Market Intelligence

An end-to-end Business Development analytics project designed to identify attractive expansion markets and prioritize target accounts using SQL and Python.

## Business Problem

A B2B SaaS company is planning to expand into new markets.

The Business Development team needs to answer two questions:

1. Which markets should be considered for expansion?
2. Which companies should the BD team approach first?

This project builds an account intelligence system that combines market opportunity, customer profiles, company characteristics, and account-level scoring to generate a prioritized target-account list.

## Project Objective

The objective is to transform raw company and market data into actionable Business Development recommendations.

The analysis covers:

- Market opportunity analysis
- Ideal Customer Profile (ICP) analysis
- Prospect identification
- Target account scoring
- Account segmentation
- Priority tiers
- BD outreach recommendations

## Tools & Technologies

- **SQL (MySQL)** — data analysis, joins, CTEs, window functions and scoring
- **Python** — data generation, analysis and account segmentation
- **Pandas** — data manipulation
- **NumPy** — synthetic data generation
- **Scikit-learn** — K-Means clustering
- **Matplotlib** — data visualization
- **GitHub** — project version control and portfolio

## Project Architecture

The project follows a simple analytics pipeline:

Raw Data
↓
SQL Data Analysis
↓
Market Opportunity Scoring
↓
ICP Profiling
↓
Prospect ICP Scoring
↓
Target Account Scoring
↓
Python Account Segmentation
↓
BD Recommendations

### Data Sources

The project uses fictional/synthetic company data created specifically for this portfolio project.

The datasets include:

- `companies.csv` — company characteristics and financial information
- `customers.csv` — existing customer and contract information
- `markets.csv` — market-level opportunity indicators
- `competitors.csv` — competitive landscape information

## SQL Analysis

SQL is used to transform the raw datasets into actionable Business Development insights.

### 1. Market Opportunity Scoring

Markets are evaluated using multiple factors:

- Market growth
- Digital adoption
- Target company pool
- Competition level
- Entry difficulty

Each factor is normalized to a 0–100 scale and combined into a weighted market opportunity score.

### 2. Ideal Customer Profile (ICP)

Existing customers are analyzed to identify common characteristics of valuable accounts.

The analysis considers:

- Industry
- Company size
- Employee count
- Annual revenue
- Growth rate
- Technology spending
- Contract value

### 3. Prospect ICP Scoring

Non-customer companies are compared with the high-value customer profile.

The ICP score uses:

- Employee similarity — 25%
- Revenue similarity — 25%
- Growth similarity — 20%
- Technology spend similarity — 30%

This creates a measurable estimate of how closely each prospect matches the company's ideal customer profile.

### 4. Target Account Scoring

The final account score combines:

**60% ICP Fit + 40% Market Opportunity**

This connects company-level fit with the attractiveness of the market in which the company operates.

### 5. BD Priority Tiers

Accounts are divided into actionable priority groups:

| Score | Priority |
|------:|----------|
| 80+ | Tier 1 - High Priority |
| 65–79.99 | Tier 2 - Medium Priority |
| 50–64.99 | Tier 3 - Low Priority |
| Below 50 | Do Not Prioritize |

The resulting account list can be used by a Business Development team to focus outreach resources on higher-priority prospects.

## Python Analysis

Python is used to extend the SQL analysis and turn account scores into practical Business Development insights.

### Account Segmentation

K-Means clustering is used to segment target accounts based on:

- Employee count
- Annual revenue
- Growth rate
- Technology spending
- Target account score

Four account segments are generated:

- Emerging Accounts
- High-Growth Accounts
- Enterprise Accounts
- Established Low-Growth Accounts

### BD Recommendation Engine

Each account receives a recommended BD action based on its:

- Priority tier
- Account segment
- ICP fit
- Market opportunity
- Growth characteristics

Examples of recommendations include:

- Personalized outreach
- Enterprise-focused multi-stakeholder outreach
- Growth and scalability-focused outreach
- Nurture campaigns
- Low-touch monitoring
- Do not actively target

### Outputs

Python generates:

- Account segment assignments
- Segment profiles
- Market opportunity visualization
- Final BD recommendations

Key output files include:

- `final_bd_recommendations.csv`
- `account_segment_profile.csv`
- `market_account_scores.png`

## Key Findings

The analysis generated several account-level and market-level insights from the synthetic dataset.

### Market-Level Findings

Average target-account scores varied across markets:

| Country | Average Target Account Score |
|---------|-----------------------------:|
| UAE | 62.46 |
| Singapore | 56.65 |
| New Zealand | 54.38 |
| Australia | 53.68 |
| India | 49.78 |
| Canada | 49.11 |
| United Kingdom | 48.12 |
| Germany | 43.18 |

The UAE had the highest average target-account score in the generated dataset, while Germany had the lowest.

### Account Priority Distribution

The 400 non-customer prospects were classified into four priority groups:

| Priority | Accounts |
|----------|---------:|
| Tier 1 - High Priority | 0 |
| Tier 2 - Medium Priority | 81 |
| Tier 3 - Low Priority | 156 |
| Do Not Prioritize | 163 |

No accounts reached the Tier 1 threshold of 80 in this dataset. The highest-scoring account achieved a target-account score of 78.39.

### Highest-Scoring Accounts

The highest-scoring accounts included companies from:

- Finance
- Telecommunications
- Healthcare
- Energy
- Logistics
- Manufacturing
- Professional Services

The highest individual target-account score was **78.39**.

### Industry Analysis

Average target-account scores by industry were:

| Industry | Average Score |
|----------|--------------:|
| Manufacturing | 56.06 |
| Telecommunications | 53.81 |
| Energy | 53.73 |
| Logistics | 53.62 |
| Finance | 53.07 |
| Retail | 51.74 |
| Healthcare | 51.30 |
| Professional Services | 50.93 |
| Education | 50.24 |
| SaaS | 46.62 |

### Account Segmentation

K-Means clustering produced four account segments:

| Segment | Accounts | Avg. Employees | Avg. Revenue | Avg. Growth |
|---------|---------:|---------------:|-------------:|------------:|
| Emerging Accounts | 129 | 816 | 12.43M | 14.78% |
| High-Growth Accounts | 101 | 2,829 | 42.36M | 25.59% |
| Enterprise Accounts | 76 | 4,121 | 79.21M | 15.57% |
| Established Low-Growth Accounts | 94 | 3,221 | 44.52M | 3.92% |

The segmentation provides an additional layer for tailoring Business Development strategies beyond a single account score.

## Project Outputs

The project produces the following reusable outputs:

- `final_bd_recommendations.csv` — final scored accounts and BD recommendations
- `account_segment_profile.csv` — account segment characteristics
- `market_account_scores.png` — market-level visualization
- SQL views for market, ICP, target-account and BD prioritization analysis

## Limitations

This project uses fictional/synthetic data created for portfolio and analytical demonstration purposes.

The market scores, company information, customer behavior and recommendations should therefore not be interpreted as real-world market intelligence.

The scoring framework is also model-driven and depends on the selected weights and assumptions. In a real Business Development environment, the model would be validated against historical conversion, customer acquisition cost, win rates, sales cycle length and actual market data.

## Project Structure

```text
BD-Market-Intelligence/
│
├── data/
│   ├── companies.csv
│   ├── customers.csv
│   ├── markets.csv
│   ├── competitors.csv
│   ├── target_accounts.csv
│   ├── final_bd_recommendations.csv
│   ├── account_segment_profile.csv
│   └── market_account_scores.png
│
├── python/
│   ├── generate_data.py
│   └── analyze_accounts.py
│
├── sql/
│   ├── 01_market_opportunity.sql
│   ├── 02_prospect_icp_scoring.sql
│   ├── 03_target_account_scoring.sql
│   └── 04_bd_target_accounts.sql
│
└── README.md