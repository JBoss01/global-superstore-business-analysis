# Feature Evaluation and Selection Summary
**Global Superstore – Week 3**  
**Analyst:** Ozoeze Wilord Ugonna

---

## Objective

Evaluate original and engineered features to decide which variables should enter the final modelling dataset for Week 4. Decisions are based on statistical evidence, domain knowledge, redundancy, and potential data leakage — not on correlation alone.

---

## 1. Evaluation Approach

| Method | Purpose |
|--------|---------|
| Correlation analysis | Detect linear / monotonic relationships and redundancy |
| Distribution & missingness review | Identify low-information or problematic columns |
| Relationship with Profit / Is_Loss_Making | Assess predictive usefulness |
| Domain knowledge | Keep business-critical fields even if correlations are moderate |
| Leakage check | Ensure no future or target-derived information leaks incorrectly |

---

## 2. Original Features – Key Decisions

| Feature | Decision | Justification |
|---------|----------|---------------|
| Row ID | **Remove** | Identifier only; no analytical value |
| Order ID | **Remove** (or keep only for reference) | Identifier; high cardinality |
| Customer ID / Customer Name | **Remove** from modelling set | High cardinality; privacy; not generalisable |
| Product ID / Product Name | **Remove** from core model features | Extremely high cardinality |
| Postal Code | **Remove** | ~80% missing; mostly non-US |
| Sales | **Keep** | Core driver; moderate correlation with Profit |
| Quantity | **Keep** | Operational volume signal |
| Discount | **Keep** | Strong negative relationship with Profit |
| Profit | **Keep** as target (or use derived targets) | Primary business outcome |
| Shipping Cost | **Keep** | Operational cost driver |
| Category | **Keep** | Statistically significant profit differences |
| Sub-Category | **Keep** (or encode carefully) | Finer product signal |
| Segment | **Keep** | Strategic customer grouping |
| Ship Mode | **Keep** | Operational lever |
| Order Priority | **Keep** | Service level signal |
| Market / Region / Country | **Keep** (select best granularity) | Geographic performance |
| Order Date / Ship Date | **Transform** → Days_to_Ship, then can drop raw dates for modelling | Time signal captured in engineered feature |
| City / State | **Optional / Remove** for global model | Very high cardinality |

---

## 3. Engineered Features – Evaluation

| Feature | Decision | Evidence / Reason |
|---------|----------|-------------------|
| Profit_Margin | **Keep** | Normalises profit; high business interpretability |
| Is_Loss_Making | **Keep** | Clear binary target / risk flag (~24.5% positive class) |
| Discount_Impact | **Keep** | Captures absolute cost of discounting |
| Shipping_Efficiency | **Keep** | Relative shipping burden; operational insight |
| Days_to_Ship | **Keep** if data quality allows | Fulfilment speed |

**Note:** Profit_Margin and Is_Loss_Making are derived from Profit.  
- If the model **predicts Profit**, do **not** include Profit_Margin or Is_Loss_Making as inputs (leakage).  
- If the model **predicts Is_Loss_Making**, Profit and Profit_Margin must be excluded from inputs.

---

## 4. Redundancy & Multicollinearity Notes

- Sales and Shipping Cost are positively related (larger orders tend to cost more to ship). Both are retained because they answer different questions (revenue vs cost).
- Discount and Discount_Impact are related by construction. Both may be kept for interpretation, but for linear models one may be sufficient.
- Category and Sub-Category are nested. Prefer Category for stable models; use Sub-Category when finer detail is required.

No feature was removed solely because it was correlated with another feature. Every removal or retention is justified above.

---

## 5. Final Modelling Dataset Principles

The exported modelling dataset will contain:

1. Selected original features with clear business or predictive value  
2. All justified engineered features  
3. A clearly defined target column (Profit and/or Is_Loss_Making)  
4. No pure identifiers  
5. No features that would cause target leakage for the chosen prediction task  

All significant changes from the Week 2 dataset are documented in this summary and in the notebook.

---

*End of Feature Evaluation and Selection Summary*
