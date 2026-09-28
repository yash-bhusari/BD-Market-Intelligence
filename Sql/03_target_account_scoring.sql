-- =====================================================
-- BD Market Intelligence
-- 03 - Target Account Scoring
-- =====================================================

-- This view combines:
--   60% ICP Fit
--   40% Market Opportunity
--
-- The result identifies which prospect accounts are
-- strongest targets for Business Development.

CREATE OR REPLACE VIEW target_account_scores AS

SELECT
    p.company_id,
    p.company_name,
    p.industry,
    p.country,
    p.employees,
    p.annual_revenue,
    p.growth_rate,
    p.technology_spend,
    p.company_size,

    p.icp_fit_score,
    m.market_opportunity_score,

    -- Final target account score
    ROUND(
        (p.icp_fit_score * 0.60)
        +
        (m.market_opportunity_score * 0.40),
        2
    ) AS target_account_score

FROM prospect_icp_scores p

JOIN market_opportunity_scores m
    ON p.country = m.country;