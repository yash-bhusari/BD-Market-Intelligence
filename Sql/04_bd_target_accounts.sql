-- =====================================================
-- BD Market Intelligence
-- 04 - BD Target Accounts
-- =====================================================

-- This view creates the final target-account list for
-- the Business Development team.
--
-- Priority tiers:
--   80+  = Tier 1 - High Priority
--   65+  = Tier 2 - Medium Priority
--   50+  = Tier 3 - Low Priority
--   <50  = Do Not Prioritize

CREATE OR REPLACE VIEW bd_target_accounts AS

SELECT
    company_id,
    company_name,
    industry,
    country,
    employees,
    annual_revenue,
    growth_rate,
    technology_spend,
    company_size,

    icp_fit_score,
    market_opportunity_score,
    target_account_score,

    CASE
        WHEN target_account_score >= 80
            THEN 'Tier 1 - High Priority'

        WHEN target_account_score >= 65
            THEN 'Tier 2 - Medium Priority'

        WHEN target_account_score >= 50
            THEN 'Tier 3 - Low Priority'

        ELSE 'Do Not Prioritize'
    END AS priority_tier

FROM target_account_scores

ORDER BY target_account_score DESC;