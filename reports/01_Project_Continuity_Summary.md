# Project Continuity Summary
**AnalystLab Africa – Data Science Internship Programme**  
**Week 3: Advanced Data Analysis, Statistical Validation & Feature Engineering**

**Analyst:** Ozoeze Wilord Ugonna  
**Project:** Global Superstore Business Intelligence & Analytics  
**Dataset:** Global Superstore (51,290 orders)

---

## 1. Business Problem

Global Superstore operates across multiple international markets (APAC, LATAM, EU, US, EMEA, Africa, Canada) selling Furniture, Office Supplies, and Technology products.

The core business problem is:

> **How can Global Superstore improve profitability by understanding which products, customer segments, regions, shipping choices, and discount practices drive or destroy profit?**

---

## 2. Main Project Objective

To analyse sales and profit performance, identify loss-making patterns, validate key business assumptions with statistics, engineer useful features, and produce a modelling-ready dataset that will support predictive models in Week 4.

**Target variable of interest:** `Profit` (and derived profitability indicators such as Profit Margin and Is_Loss_Making).

---

## 3. Key Findings from Week 1

- Total Sales ≈ **$12.64 million**; Total Profit ≈ **$1.47 million**
- Overall profit margin ≈ **11.6%**
- **Technology** is the most profitable category (avg profit ≈ $65.5)
- **Furniture** has the highest loss rate (~31.6% of orders are loss-making)
- **Consumer** is the largest segment by order volume
- High discounts are strongly associated with negative profit
- Shipping cost and discount levels vary significantly by market and ship mode

---

## 4. Major Data-Quality Issues Identified in Week 1

| Issue | Status after Week 2 |
|-------|---------------------|
| `Postal Code` missing for ~80% of rows (mostly non-US) | Documented; not critical for global analysis |
| Inconsistent date formats | Parsed and standardised |
| Extreme outliers in Sales / Profit / Shipping Cost | Investigated; retained with flags where useful |
| Mixed market / region naming | Cleaned and standardised |

---

## 5. Major Cleaning & Preprocessing Completed in Week 2

- Date columns converted to datetime
- Missing Postal Code handled (left as missing for non-US rows)
- Data types corrected
- Duplicate checks performed (no critical duplicates found)
- Basic derived fields prepared where needed
- Cleaned dataset saved for advanced analysis

**Week 3 rule:** The complete Week 2 cleaning process is **not** repeated. Only justified refinements are applied based on new analytical evidence.

---

## 6. Remaining Questions Requiring Deeper Investigation (Week 3 Focus)

1. Are the differences in average Profit across Categories statistically significant?
2. Do discounted orders produce significantly lower profit than non-discounted orders?
3. Is there a statistically significant association between customer Segment and Order Priority?
4. How strong are the relationships between Sales, Discount, Shipping Cost, and Profit?
5. Which engineered features (Profit Margin, Discount Impact, Shipping Efficiency, etc.) add the most value for future modelling?
6. Which original features are redundant or low-value and should be excluded from the modelling dataset?

---

## 7. How Week 3 Builds on Previous Work

| Week | Focus | Output |
|------|--------|--------|
| Week 1 | Business understanding & initial EDA | Patterns, risks, first insights |
| Week 2 | Data cleaning & preparation | Clean, structured dataset | Visualization
| **Week 3** | **Advanced EDA, hypothesis testing, feature engineering & evaluation** | **Statistically validated insights + modelling-ready dataset** |
| Week 4 | Machine learning models | Predictive models & business recommendations |

Week 3 does **not** restart the project. It deepens the analysis, validates assumptions, creates new features, and prepares the final dataset for predictive modelling.

---
