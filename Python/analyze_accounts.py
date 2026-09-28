import pandas as pd

# Load SQL-generated target account data
file_path = "data/target_accounts.csv"
df = pd.read_csv(file_path)

print("=" * 50)
print("BD MARKET INTELLIGENCE ANALYSIS")
print("=" * 50)

# --------------------------------------------------
# 1. Priority distribution
# --------------------------------------------------

print("\n1. ACCOUNT PRIORITY DISTRIBUTION")
print("-" * 40)

priority_counts = df["account_priority"].value_counts()

print(priority_counts)


# --------------------------------------------------
# 2. High-priority accounts by country
# --------------------------------------------------

print("\n2. HIGH-PRIORITY ACCOUNTS BY COUNTRY")
print("-" * 40)

high_priority = df[
    df["account_priority"] == "Tier 1 - High Priority"
]

country_analysis = (
    high_priority
    .groupby("country")
    .size()
    .sort_values(ascending=False)
)

print(country_analysis)


# --------------------------------------------------
# 3. High-priority accounts by industry
# --------------------------------------------------

print("\n3. HIGH-PRIORITY ACCOUNTS BY INDUSTRY")
print("-" * 40)

industry_analysis = (
    high_priority
    .groupby("industry")
    .size()
    .sort_values(ascending=False)
)

print(industry_analysis)


# --------------------------------------------------
# 4. Average account score by country
# --------------------------------------------------

print("\n4. AVERAGE TARGET ACCOUNT SCORE BY COUNTRY")
print("-" * 40)

average_country_score = (
    df
    .groupby("country")["target_account_score"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print(average_country_score)


# --------------------------------------------------
# 5. Top 10 accounts
# --------------------------------------------------

print("\n5. TOP 10 TARGET ACCOUNTS")
print("-" * 40)

top_accounts = df.nlargest(
    10,
    "target_account_score"
)

print(
    top_accounts[
        [
            "company_name",
            "industry",
            "country",
            "icp_fit_score",
            "market_opportunity_score",
            "target_account_score",
            "account_priority"
        ]
    ].to_string(index=False)
)
import matplotlib.pyplot as plt

# --------------------------------------------------
# 6. Market opportunity visualization
# --------------------------------------------------

plt.figure(figsize=(10, 6))

average_country_score.sort_values().plot(
    kind="barh"
)

plt.title("Average Target Account Score by Country")
plt.xlabel("Average Target Account Score")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    "data/market_account_scores.png",
    dpi=300
)

# plt.show()
# --------------------------------------------------
# 7. Industry opportunity analysis
# --------------------------------------------------

industry_summary = (
    df.groupby("industry")
    .agg(
        average_score=("target_account_score", "mean"),
        tier_1_accounts=(
            "account_priority",
            lambda x: (x == "Tier 1 - High Priority").sum()
        ),
        total_accounts=("company_id", "count")
    )
    .sort_values(
        by="average_score",
        ascending=False
    )
)

industry_summary["average_score"] = (
    industry_summary["average_score"].round(2)
)

print("\n6. INDUSTRY OPPORTUNITY ANALYSIS")
print("-" * 40)

print(industry_summary)
# --------------------------------------------------
# 8. Automatic BD recommendations
# --------------------------------------------------

def generate_recommendation(row):

    reasons = []

    if row["icp_fit_score"] >= 80:
        reasons.append("strong ICP fit")
    elif row["icp_fit_score"] >= 65:
        reasons.append("moderate ICP fit")

    if row["market_opportunity_score"] >= 80:
        reasons.append("attractive market")
    elif row["market_opportunity_score"] >= 65:
        reasons.append("promising market")

    if row["growth_rate"] >= 20:
        reasons.append("high company growth")

    if row["technology_spend"] >= df["technology_spend"].median():
        reasons.append("healthy technology spending")

    if not reasons:
        return "Limited current targeting signals"

    return "Target because of " + ", ".join(reasons)


df["bd_recommendation"] = df.apply(
    generate_recommendation,
    axis=1
)

print("\n7. SAMPLE BD RECOMMENDATIONS")
print("-" * 40)

print(
    df[
        [
            "company_name",
            "country",
            "industry",
            "target_account_score",
            "account_priority",
            "bd_recommendation"
        ]
    ]
    .head(15)
    .to_string(index=False)
)
# --------------------------------------------------
# 9. Export final BD recommendations
# --------------------------------------------------

output_file = "data/final_bd_recommendations.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nFinal BD recommendation file created:")
print(output_file)
# --------------------------------------------------
# 10. Account segmentation using K-Means
# --------------------------------------------------

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Features used for segmentation
features = [
    "employees",
    "annual_revenue",
    "growth_rate",
    "technology_spend"
]

X = df[features].copy()

# Standardize the features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Create 4 account segments
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["account_segment"] = kmeans.fit_predict(X_scaled)

print("\n8. ACCOUNT SEGMENT DISTRIBUTION")
print("-" * 40)

print(
    df["account_segment"]
    .value_counts()
    .sort_index()
)
# --------------------------------------------------
# 11. Profile each account segment
# --------------------------------------------------

segment_profile = (
    df.groupby("account_segment")
    .agg(
        account_count=("company_id", "count"),
        avg_employees=("employees", "mean"),
        avg_revenue=("annual_revenue", "mean"),
        avg_growth_rate=("growth_rate", "mean"),
        avg_technology_spend=("technology_spend", "mean"),
        avg_target_score=("target_account_score", "mean")
    )
    .round(2)
)

print("\n9. ACCOUNT SEGMENT PROFILE")
print("-" * 40)

print(segment_profile)
# --------------------------------------------------
# 12. Export segment analysis
# --------------------------------------------------

segment_profile.to_csv(
    "data/account_segment_profile.csv"
)

# Save the enriched account dataset
df.to_csv(
    "data/final_bd_recommendations.csv",
    index=False
)

print("\nSegment profile saved:")
print("data/account_segment_profile.csv")

print("\nFinal enriched dataset updated:")
print("data/final_bd_recommendations.csv")
# --------------------------------------------------
# 13. Convert cluster IDs into business segments
# --------------------------------------------------

segment_names = {
    0: "Emerging Accounts",
    1: "High-Growth Accounts",
    2: "Enterprise Accounts",
    3: "Established Low-Growth Accounts"
}

df["account_segment_name"] = (
    df["account_segment"]
    .map(segment_names)
)

print("\n10. BUSINESS SEGMENT DISTRIBUTION")
print("-" * 40)

print(
    df["account_segment_name"]
    .value_counts()
)

# Save updated dataset
df.to_csv(
    "data/final_bd_recommendations.csv",
    index=False
)

print("\nUpdated final dataset saved.")
# --------------------------------------------------
# 14. Generate BD action recommendations
# --------------------------------------------------

def generate_action(row):

    if row["account_priority"] == "Tier 1 - High Priority":

        if row["account_segment_name"] == "High-Growth Accounts":
            return "Prioritize personalized outreach and book a discovery call"

        elif row["account_segment_name"] == "Enterprise Accounts":
            return "Use an enterprise-focused approach with multiple stakeholders"

        elif row["account_segment_name"] == "Emerging Accounts":
            return "Use targeted outreach focused on growth and scalability"

        else:
            return "Use targeted account-based outreach"

    elif row["account_priority"] == "Tier 2 - Medium Priority":

        return "Add to nurture campaign and monitor engagement"

    elif row["account_priority"] == "Tier 3 - Low Priority":

        return "Use low-touch outreach and monitor for changes"

    else:

        return "Do not actively target at this stage"


df["bd_action"] = df.apply(
    generate_action,
    axis=1
)

print("\n11. SAMPLE BD ACTIONS")
print("-" * 40)

print(
    df[
        [
            "company_name",
            "country",
            "industry",
            "account_segment_name",
            "account_priority",
            "target_account_score",
            "bd_action"
        ]
    ]
    .head(15)
    .to_string(index=False)
)

# Save final dataset
df.to_csv(
    "data/final_bd_recommendations.csv",
    index=False
)

print("\nFinal BD intelligence dataset saved:")
print("data/final_bd_recommendations.csv")
