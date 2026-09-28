-- =====================================================
-- BD Market Intelligence
-- 01 - Market Opportunity Scoring
-- =====================================================

-- This view calculates a normalized market opportunity
-- score for each country using:
--   30% Market Growth
--   20% Digital Adoption
--   20% Company Pool
--   15% Competition
--   15% Entry Ease

CREATE OR REPLACE VIEW market_opportunity_scores AS

SELECT
    country,

    -- Higher market growth = higher score
    ROUND(
        (
            (market_growth_percent - MIN(market_growth_percent) OVER ())
            /
            (MAX(market_growth_percent) OVER () -
             MIN(market_growth_percent) OVER ())
        ) * 100,
        2
    ) AS growth_score,

    -- Higher digital adoption = higher score
    ROUND(
        (
            (digital_adoption_percent - MIN(digital_adoption_percent) OVER ())
            /
            (MAX(digital_adoption_percent) OVER () -
             MIN(digital_adoption_percent) OVER ())
        ) * 100,
        2
    ) AS digital_adoption_score,

    -- Larger target company pool = higher score
    ROUND(
        (
            (target_company_count - MIN(target_company_count) OVER ())
            /
            (MAX(target_company_count) OVER () -
             MIN(target_company_count) OVER ())
        ) * 100,
        2
    ) AS company_pool_score,

    -- Lower competition = higher score
    ROUND(
        (
            (MAX(competition_level) OVER () - competition_level)
            /
            (MAX(competition_level) OVER () -
             MIN(competition_level) OVER ())
        ) * 100,
        2
    ) AS competition_score,

    -- Lower entry difficulty = higher score
    ROUND(
        (
            (MAX(entry_difficulty) OVER () - entry_difficulty)
            /
            (MAX(entry_difficulty) OVER () -
             MIN(entry_difficulty) OVER ())
        ) * 100,
        2
    ) AS entry_ease_score,

    -- Weighted market opportunity score
    ROUND(
        (
            (
                (market_growth_percent - MIN(market_growth_percent) OVER ())
                /
                (MAX(market_growth_percent) OVER () -
                 MIN(market_growth_percent) OVER ())
            ) * 100 * 0.30
        )
        +
        (
            (
                (digital_adoption_percent - MIN(digital_adoption_percent) OVER ())
                /
                (MAX(digital_adoption_percent) OVER () -
                 MIN(digital_adoption_percent) OVER ())
            ) * 100 * 0.20
        )
        +
        (
            (
                (target_company_count - MIN(target_company_count) OVER ())
                /
                (MAX(target_company_count) OVER () -
                 MIN(target_company_count) OVER ())
            ) * 100 * 0.20
        )
        +
        (
            (
                (MAX(competition_level) OVER () - competition_level)
                /
                (MAX(competition_level) OVER () -
                 MIN(competition_level) OVER ())
            ) * 100 * 0.15
        )
        +
        (
            (
                (MAX(entry_difficulty) OVER () - entry_difficulty)
                /
                (MAX(entry_difficulty) OVER () -
                 MIN(entry_difficulty) OVER ())
            ) * 100 * 0.15
        ),
        2
    ) AS market_opportunity_score

FROM markets;-- =====================================================
-- BD Market Intelligence
-- 01 - Market Opportunity Scoring
-- =====================================================

-- This view calculates a normalized market opportunity
-- score for each country using:
--   30% Market Growth
--   20% Digital Adoption
--   20% Company Pool
--   15% Competition
--   15% Entry Ease

CREATE OR REPLACE VIEW market_opportunity_scores AS

SELECT
    country,

    -- Higher market growth = higher score
    ROUND(
        (
            (market_growth_percent - MIN(market_growth_percent) OVER ())
            /
            (MAX(market_growth_percent) OVER () -
             MIN(market_growth_percent) OVER ())
        ) * 100,
        2
    ) AS growth_score,

    -- Higher digital adoption = higher score
    ROUND(
        (
            (digital_adoption_percent - MIN(digital_adoption_percent) OVER ())
            /
            (MAX(digital_adoption_percent) OVER () -
             MIN(digital_adoption_percent) OVER ())
        ) * 100,
        2
    ) AS digital_adoption_score,

    -- Larger target company pool = higher score
    ROUND(
        (
            (target_company_count - MIN(target_company_count) OVER ())
            /
            (MAX(target_company_count) OVER () -
             MIN(target_company_count) OVER ())
        ) * 100,
        2
    ) AS company_pool_score,

    -- Lower competition = higher score
    ROUND(
        (
            (MAX(competition_level) OVER () - competition_level)
            /
            (MAX(competition_level) OVER () -
             MIN(competition_level) OVER ())
        ) * 100,
        2
    ) AS competition_score,

    -- Lower entry difficulty = higher score
    ROUND(
        (
            (MAX(entry_difficulty) OVER () - entry_difficulty)
            /
            (MAX(entry_difficulty) OVER () -
             MIN(entry_difficulty) OVER ())
        ) * 100,
        2
    ) AS entry_ease_score,

    -- Weighted market opportunity score
    ROUND(
        (
            (
                (market_growth_percent - MIN(market_growth_percent) OVER ())
                /
                (MAX(market_growth_percent) OVER () -
                 MIN(market_growth_percent) OVER ())
            ) * 100 * 0.30
        )
        +
        (
            (
                (digital_adoption_percent - MIN(digital_adoption_percent) OVER ())
                /
                (MAX(digital_adoption_percent) OVER () -
                 MIN(digital_adoption_percent) OVER ())
            ) * 100 * 0.20
        )
        +
        (
            (
                (target_company_count - MIN(target_company_count) OVER ())
                /
                (MAX(target_company_count) OVER () -
                 MIN(target_company_count) OVER ())
            ) * 100 * 0.20
        )
        +
        (
            (
                (MAX(competition_level) OVER () - competition_level)
                /
                (MAX(competition_level) OVER () -
                 MIN(competition_level) OVER ())
            ) * 100 * 0.15
        )
        +
        (
            (
                (MAX(entry_difficulty) OVER () - entry_difficulty)
                /
                (MAX(entry_difficulty) OVER () -
                 MIN(entry_difficulty) OVER ())
            ) * 100 * 0.15
        ),
        2
    ) AS market_opportunity_score

FROM markets;