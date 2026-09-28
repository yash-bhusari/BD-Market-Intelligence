-- =====================================================
-- BD Market Intelligence
-- 02 - Prospect ICP Scoring
-- =====================================================

-- This view scores non-customer companies based on how
-- closely they match the profile of high-value customers.
--
-- ICP factors:
--   25% Employee similarity
--   25% Revenue similarity
--   20% Growth similarity
--   30% Technology spend similarity

CREATE OR REPLACE VIEW prospect_icp_scores AS

WITH high_value_profile AS (

    -- Calculate the average characteristics of
    -- existing high-value customers
    SELECT
        AVG(c.employees) AS avg_employees,
        AVG(c.annual_revenue) AS avg_revenue,
        AVG(c.growth_rate) AS avg_growth_rate,
        AVG(c.technology_spend) AS avg_technology_spend

    FROM companies c

    JOIN customers cu
        ON c.company_id = cu.company_id

    WHERE cu.contract_value >= (
        SELECT AVG(contract_value)
        FROM customers
    )
),

prospects AS (

    -- Select companies that are NOT existing customers
    SELECT
        c.company_id,
        c.company_name,
        c.industry,
        c.country,
        c.employees,
        c.annual_revenue,
        c.growth_rate,
        c.technology_spend,
        c.company_size

    FROM companies c

    LEFT JOIN customers cu
        ON c.company_id = cu.company_id

    WHERE cu.company_id IS NULL
)

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

    -- Employee similarity
    ROUND(
        GREATEST(
            0,
            100 - ABS(p.employees - h.avg_employees)
            / h.avg_employees * 100
        ),
        2
    ) AS employee_fit_score,

    -- Revenue similarity
    ROUND(
        GREATEST(
            0,
            100 - ABS(p.annual_revenue - h.avg_revenue)
            / h.avg_revenue * 100
        ),
        2
    ) AS revenue_fit_score,

    -- Growth similarity
    ROUND(
        GREATEST(
            0,
            100 - ABS(p.growth_rate - h.avg_growth_rate)
            / GREATEST(ABS(h.avg_growth_rate), 1) * 100
        ),
        2
    ) AS growth_fit_score,

    -- Technology spend similarity
    ROUND(
        GREATEST(
            0,
            100 - ABS(p.technology_spend - h.avg_technology_spend)
            / h.avg_technology_spend * 100
        ),
        2
    ) AS technology_fit_score,

    -- Final weighted ICP score
    ROUND(
        (
            GREATEST(
                0,
                100 - ABS(p.employees - h.avg_employees)
                / h.avg_employees * 100
            ) * 0.25
        )
        +
        (
            GREATEST(
                0,
                100 - ABS(p.annual_revenue - h.avg_revenue)
                / h.avg_revenue * 100
            ) * 0.25
        )
        +
        (
            GREATEST(
                0,
                100 - ABS(p.growth_rate - h.avg_growth_rate)
                / GREATEST(ABS(h.avg_growth_rate), 1) * 100
            ) * 0.20
        )
        +
        (
            GREATEST(
                0,
                100 - ABS(p.technology_spend - h.avg_technology_spend)
                / h.avg_technology_spend * 100
            ) * 0.30
        ),
        2
    ) AS icp_fit_score

FROM prospects p
CROSS JOIN high_value_profile h;