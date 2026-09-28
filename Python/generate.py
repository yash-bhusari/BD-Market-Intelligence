import pandas as pd
import numpy as np
import random

# Make results reproducible
np.random.seed(42)
random.seed(42)

# Business categories
industries = [
    "SaaS",
    "Finance",
    "Healthcare",
    "Retail",
    "Logistics",
    "Manufacturing",
    "Energy",
    "Education",
    "Telecommunications",
    "Professional Services"
]

countries = [
    "Australia",
    "India",
    "Singapore",
    "New Zealand",
    "UAE",
    "United Kingdom",
    "Canada",
    "Germany"
]

company_sizes = [
    "Startup",
    "Small",
    "Medium",
    "Large",
    "Enterprise"
]

companies = []

# Generate 500 companies
for i in range(1, 501):

    employees = random.randint(20, 5000)

    annual_revenue = round(
        employees * random.uniform(8000, 25000),
        2
    )

    growth_rate = round(
        random.uniform(-5, 35),
        2
    )

    technology_spend = round(
        annual_revenue * random.uniform(0.03, 0.15),
        2
    )

    companies.append({
        "company_id": i,
        "company_name": f"Company_{i:04d}",
        "industry": random.choice(industries),
        "country": random.choice(countries),
        "employees": employees,
        "annual_revenue": annual_revenue,
        "growth_rate": growth_rate,
        "technology_spend": technology_spend,
        "company_size": random.choice(company_sizes)
    })

# Convert to DataFrame
companies_df = pd.DataFrame(companies)

# Save CSV
companies_df.to_csv(
    "data/companies.csv",
    index=False
)

# Display results
print("Companies dataset created successfully!")
print("--------------------------------------")
print("Total companies:", len(companies_df))
print("\nFirst 5 companies:")
print(companies_df.head())
# Display results
print("Companies dataset created successfully!")
print("--------------------------------------")
print("Total companies:", len(companies_df))
print("\nFirst 5 companies:")
print(companies_df.head())

print("\nDataset information:")
print(companies_df.info())

print("\nBasic statistics:")
print(companies_df.describe())
# ----------------------------------------
# CREATE CUSTOMER DATASET
# ----------------------------------------

customer_records = []

# Select 100 existing customers
customer_company_ids = random.sample(
    list(companies_df["company_id"]),
    100
)

for customer_id, company_id in enumerate(customer_company_ids, start=1):

    company = companies_df[
        companies_df["company_id"] == company_id
    ].iloc[0]

    # Larger companies generally have larger contracts
    contract_value = round(
        company["annual_revenue"] *
        random.uniform(0.01, 0.05),
        2
    )

    # Keep contract values realistic
    contract_value = max(
        10000,
        min(contract_value, 500000)
    )

    customer_since = pd.Timestamp(
        "2022-01-01"
    ) + pd.Timedelta(
        days=random.randint(0, 1400)
    )

    products_purchased = random.randint(1, 5)

    satisfaction_score = round(
        random.uniform(6, 10),
        1
    )

    renewal_status = random.choice([
        "Renewed",
        "Renewed",
        "Renewed",
        "Pending",
        "At Risk"
    ])

    expansion_potential = random.choice([
        "High",
        "High",
        "Medium",
        "Low"
    ])

    customer_records.append({
        "customer_id": customer_id,
        "company_id": company_id,
        "contract_value": contract_value,
        "customer_since": customer_since.date(),
        "products_purchased": products_purchased,
        "satisfaction_score": satisfaction_score,
        "renewal_status": renewal_status,
        "expansion_potential": expansion_potential
    })

customers_df = pd.DataFrame(customer_records)

# Save customers
customers_df.to_csv(
    "data/customers.csv",
    index=False
)

print("\nCustomer dataset created successfully!")
print("--------------------------------------")
print("Total customers:", len(customers_df))
print("\nFirst 5 customers:")
print(customers_df.head())
# ----------------------------------------
# CREATE MARKET INTELLIGENCE DATASET
# ----------------------------------------

market_data = []

market_profiles = {
    "Australia": {
        "market_size": 4200,
        "market_growth": 12.5,
        "competition_level": 6,
        "digital_adoption": 88,
        "entry_difficulty": 4
    },
    "India": {
        "market_size": 6800,
        "market_growth": 18.2,
        "competition_level": 8,
        "digital_adoption": 72,
        "entry_difficulty": 6
    },
    "Singapore": {
        "market_size": 2100,
        "market_growth": 10.8,
        "competition_level": 5,
        "digital_adoption": 94,
        "entry_difficulty": 3
    },
    "New Zealand": {
        "market_size": 1200,
        "market_growth": 8.5,
        "competition_level": 4,
        "digital_adoption": 86,
        "entry_difficulty": 3
    },
    "UAE": {
        "market_size": 3500,
        "market_growth": 16.4,
        "competition_level": 6,
        "digital_adoption": 91,
        "entry_difficulty": 5
    },
    "United Kingdom": {
        "market_size": 7500,
        "market_growth": 9.2,
        "competition_level": 9,
        "digital_adoption": 89,
        "entry_difficulty": 7
    },
    "Canada": {
        "market_size": 5100,
        "market_growth": 11.1,
        "competition_level": 7,
        "digital_adoption": 87,
        "entry_difficulty": 5
    },
    "Germany": {
        "market_size": 6200,
        "market_growth": 7.8,
        "competition_level": 8,
        "digital_adoption": 84,
        "entry_difficulty": 7
    }
}

for country, profile in market_profiles.items():

    country_companies = companies_df[
        companies_df["country"] == country
    ]

    target_companies = len(country_companies)

    average_revenue = country_companies[
        "annual_revenue"
    ].mean()

    average_deal_size = round(
        average_revenue * 0.02,
        2
    )

    market_data.append({
        "country": country,
        "market_size_millions": profile["market_size"],
        "market_growth_percent": profile["market_growth"],
        "target_company_count": target_companies,
        "competition_level": profile["competition_level"],
        "digital_adoption_percent": profile["digital_adoption"],
        "entry_difficulty": profile["entry_difficulty"],
        "average_deal_size": average_deal_size
    })

markets_df = pd.DataFrame(market_data)

markets_df.to_csv(
    "data/markets.csv",
    index=False
)

print("\nMarket dataset created successfully!")
print("--------------------------------------")
print(markets_df)
# ----------------------------------------
# CREATE COMPETITOR DATASET
# ----------------------------------------

competitor_industries = [
    "SaaS",
    "Finance",
    "Healthcare",
    "Retail",
    "Logistics",
    "Manufacturing",
    "Energy",
    "Education",
    "Technology"
]

pricing_segments = [
    "Budget",
    "Mid-Market",
    "Premium",
    "Enterprise"
]

product_strengths = [
    "Low",
    "Medium",
    "High"
]

competitor_records = []

for i in range(1, 31):

    country = random.choice(countries)

    market_share = round(
        random.uniform(1, 18),
        2
    )

    customer_count = random.randint(
        50,
        3000
    )

    competitor_records.append({
        "competitor_id": i,
        "competitor_name": f"Competitor_{i:02d}",
        "country": country,
        "industry_focus": random.choice(
            competitor_industries
        ),
        "market_share_percent": market_share,
        "pricing_segment": random.choice(
            pricing_segments
        ),
        "product_strength": random.choice(
            product_strengths
        ),
        "customer_count": customer_count
    })

competitors_df = pd.DataFrame(
    competitor_records
)

competitors_df.to_csv(
    "data/competitors.csv",
    index=False
)

print("\nCompetitor dataset created successfully!")
print("--------------------------------------")
print("Total competitors:", len(competitors_df))
print("\nFirst 5 competitors:")
print(competitors_df.head())