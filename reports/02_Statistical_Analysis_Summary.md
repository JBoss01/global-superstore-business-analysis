# Statistical Analysis Summary
**Global Superstore – Week 3**  
**Analyst:** Ozoeze Wilord Ugonna

---

## Overview

Four statistical tests were selected based on business questions, variable types, and data distribution characteristics. Each test follows a consistent structure: business question → hypotheses → method → results → decision → business implication.

---

## Test 1: Difference in Mean Profit Across Product Categories

**Business Question:**  
Is average profit significantly different across Furniture, Office Supplies, and Technology?

**Objective:**  
Determine whether category is a meaningful driver of profitability.

**Hypotheses:**  
- H₀: Mean Profit is the same across all three categories.  
- H₁: At least one category has a different mean Profit.

**Method:**  
Kruskal-Wallis H-test (non-parametric alternative to one-way ANOVA). Chosen because profit distributions are skewed and contain outliers.

**Key Descriptive Results:**  
| Category          | Mean Profit | Loss Rate |
|-------------------|-------------|-----------|
| Technology        | ~$65.45     | ~23.9%    |
| Furniture         | ~$28.88     | ~31.6%    |
| Office Supplies   | ~$16.58     | ~22.4%    |

**Expected Decision:**  
Reject H₀ (profit differs significantly by category).

**Business Implication:**  
Category is a core profitability driver. Technology should be prioritised for growth; Furniture requires margin protection and discount control.

---

## Test 2: Profit – Discounted vs Non-Discounted Orders

**Business Question:**  
Do orders that receive a discount generate significantly lower profit than orders with no discount?

**Objective:**  
Quantify the impact of discounting on profitability.

**Hypotheses:**  
- H₀: Mean Profit of discounted orders = Mean Profit of non-discounted orders.  
- H₁: Mean Profit of discounted orders ≠ Mean Profit of non-discounted orders.

**Method:**  
Mann-Whitney U test (independent samples, non-normal distributions).

**Key Descriptive Results:**  
| Group            | Mean Profit | Share of Orders |
|------------------|-------------|-----------------|
| No Discount      | ~$61.04     | ~56.6%          |
| With Discount    | ~−$13.61    | ~43.4%          |

**Expected Decision:**  
Reject H₀. Discounted orders are significantly less profitable (and often loss-making).

**Business Implication:**  
Current discount practices are destroying value. Discount rules should be tightened, especially on Furniture and high shipping-cost orders.

---

## Test 3: Association Between Segment and Order Priority

**Business Question:**  
Is there a relationship between customer Segment (Consumer, Corporate, Home Office) and Order Priority?

**Objective:**  
Understand whether different customer types systematically receive different service priority levels.

**Hypotheses:**  
- H₀: Segment and Order Priority are independent.  
- H₁: Segment and Order Priority are associated.

**Method:**  
Chi-Square Test of Independence.

**Business Implication:**  
If association exists, the company may be prioritising certain segments inconsistently. Service level policies can be aligned with segment value and strategic importance.

---

## Test 4: Correlation Between Sales, Discount, Shipping Cost and Profit

**Business Question:**  
How strongly are Sales, Discount, and Shipping Cost related to Profit?

**Objective:**  
Identify the strength and direction of key numerical relationships that will inform feature engineering and modelling.

**Method:**  
Spearman rank correlation (robust to skewness and outliers).

**Observed Correlations (approximate):**  
| Pair                    | Correlation | Interpretation              |
|-------------------------|-------------|-----------------------------|
| Sales ↔ Profit          | ~0.48       | Moderate positive           |
| Discount ↔ Profit       | ~−0.32      | Moderate negative           |
| Shipping Cost ↔ Profit  | ~0.35       | Moderate positive           |

**Business Implication:**  
- Higher sales tend to bring higher profit, but not always (discount and cost matter).  
- Discount is a clear negative driver of profit.  
- Shipping Cost is positively related to profit partly because higher-value orders incur higher shipping — efficiency metrics are still needed.

---

## Summary of Statistical Decisions

| Test | Result Direction | Action for Business |
|------|------------------|---------------------|
| Profit by Category | Significant difference | Prioritise Technology; protect Furniture margins |
| Discount vs No Discount | Discounted orders far less profitable | Redesign discount policy |
| Segment × Order Priority | Test for association | Align service levels with strategy |
| Correlations | Discount hurts profit; Sales supports it | Use these signals in feature engineering & models |

All interpretations focus on **business meaning**, not only p-values.

---
