# Updated Data Dictionary
**Global Superstore Modelling Dataset — Week 3**  
**AnalystLab Africa Data Science Internship**  
**Analyst:** Ozoeze Wilord Ugonna

---

## 1. Dataset Overview

| Item | Details |
|------|---------|
| **File name** | `global_superstore_modelling_dataset.csv` |
| **Rows** | 51,290 orders |
| **Columns** | 21 fields (original + engineered) |
| **Primary outcomes** | `Profit` (continuous), `Is_Loss_Making` (binary) |
| **Source** | Global Superstore dataset (cleaned in Week 2; refined in Week 3) |

---

## 2. Field Dictionary

### Original fields

| Field Name | Type | Description |
|------------|------|-------------|
| Order Date | datetime | Date the order was placed |
| Segment | categorical | Customer segment: Consumer, Corporate, or Home Office |
| City | categorical | City where the order was delivered |
| State | categorical | State or province of the delivery location |
| Country | categorical | Country of the order |
| Market | categorical | High-level market (APAC, EU, US, LATAM, EMEA, Africa, Canada) |
| Region | categorical | Sub-region within the market |
| Category | categorical | Product category: Furniture, Office Supplies, or Technology |
| Sub-Category | categorical | Finer product grouping within Category |
| Sales | numeric | Sales revenue for the order line |
| Quantity | integer | Number of units ordered |
| Discount | numeric | Discount rate (0–1 scale, e.g. 0.2 = 20%) |
| Profit | numeric | Profit or loss for the order line (primary continuous target) |
| Shipping Cost | numeric | Cost of shipping the order |
| Ship Mode | categorical | Standard Class, Second Class, First Class, or Same Day |
| Order Priority | categorical | Low, Medium, High, or Critical |

### Engineered fields (Week 3)

| Field Name | Type | Description |
|------------|------|-------------|
| Profit_Margin | numeric | Profit ÷ Sales — profitability rate across order sizes |
| Is_Loss_Making | binary (0/1) | 1 if Profit < 0, else 0 — loss flag / classification target (~24.5%) |
| Discount_Impact | numeric | Sales × Discount — estimated revenue given away |
| Shipping_Efficiency | numeric | Shipping Cost ÷ Sales — relative shipping burden |
| Days_to_Ship | integer | Ship Date − Order Date (days) — fulfilment speed |

---

## 3. Target Variables and Leakage Rules

- **Profit** — continuous target for regression  
- **Is_Loss_Making** — binary target for classification  

**Leakage rules:**
- If predicting `Is_Loss_Making` → do **not** use `Profit` or `Profit_Margin` as inputs  
- If predicting `Profit` → do **not** use `Profit_Margin` or `Is_Loss_Making` as inputs  

---

## 4. Fields Excluded from the Modelling Dataset

| Excluded field | Reason |
|----------------|--------|
| Row ID, Order ID | Identifiers only; no predictive value |
| Customer ID, Customer Name | High cardinality; not generalisable |
| Product ID, Product Name | Very high cardinality |
| Postal Code | Missing for ~80% of rows (mostly non-US) |
| Ship Date (raw) | Represented via `Days_to_Ship` |

---

## 5. Version Notes

- **Version:** Week 3 final modelling dataset  
- **Upstream:** Week 2 cleaned Global Superstore extract (full re-cleaning not repeated)  
- **Intended use:** Statistical follow-up and Week 4 supervised learning  
- **Known limitation:** Limited micro-geographic detail outside the US due to missing Postal Code  

---
