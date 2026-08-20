# Feature Engineering Documentation
**Global Superstore – Week 3**  
**Analyst:** Ozoeze Wilord Ugonna

---

## Purpose

New features were created using domain knowledge, exploratory findings, and statistical evidence so that the modelling dataset (Week 4) contains stronger signals of profitability and operational performance.

Minimum requirement: **at least three meaningful engineered features**.  
Four core features are documented below.

---

## Feature 1: Profit_Margin

**How it was created:**  
```python
df['Profit_Margin'] = df['Profit'] / df['Sales']
```
(Handle division by zero if any Sales = 0.)

**Why it was created:**  
Raw Profit is scale-dependent. A $50 profit on a $100 order is very different from a $50 profit on a $5,000 order. Profit Margin expresses profitability as a rate.

**Business meaning:**  
Shows the percentage of each sales dollar that remains as profit after costs (as captured in the dataset).

**Value for analysis / modelling:**  
- Allows fair comparison across products and categories  
- Strong candidate target or key predictor in regression / classification models  
- Easy for executives to interpret

---

## Feature 2: Is_Loss_Making

**How it was created:**  
```python
df['Is_Loss_Making'] = (df['Profit'] < 0).astype(int)
```

**Why it was created:**  
Approximately 24.5% of orders lose money. A clear binary flag makes loss patterns easier to analyse and model.

**Business meaning:**  
1 = order generated negative profit; 0 = order was profitable or break-even.

**Value for analysis / modelling:**  
- Useful as a classification target in Week 4  
- Enables rapid segmentation of risky orders  
- Supports calculation of loss rate by Category, Segment, Market, Discount band, etc.

---

## Feature 3: Discount_Impact

**How it was created:**  
```python
df['Discount_Impact'] = df['Sales'] * df['Discount']
```

**Why it was created:**  
The Discount percentage alone does not show how much revenue was given away. Multiplying by Sales estimates the absolute value of the discount.

**Business meaning:**  
Approximate revenue amount sacrificed through discounting on that order.

**Value for analysis / modelling:**  
- Quantifies the cost of discounting  
- Helps identify high-impact discount events  
- Complements the binary “has discount” view with a continuous magnitude

---

## Feature 4: Shipping_Efficiency

**How it was created:**  
```python
df['Shipping_Efficiency'] = df['Shipping Cost'] / df['Sales']
```

**Why it was created:**  
High shipping cost on a low-value order is more damaging than the same cost on a high-value order. This ratio measures shipping burden relative to order value.

**Business meaning:**  
Share of sales consumed by shipping cost. Higher values indicate less efficient shipping relative to revenue.

**Value for analysis / modelling:**  
- Highlights operational inefficiency  
- Useful for comparing Ship Modes and Markets  
- Can flag orders where shipping is eroding margin

---

## Additional Optional Features (if space allows)

| Feature | Formula / Logic | Purpose |
|---------|------------------|---------|
| Days_to_Ship | (Ship Date − Order Date).days | Operational speed |
| Sales_Band | Low / Medium / High based on quantiles | Segmentation |
| High_Discount_Flag | 1 if Discount ≥ 0.2 else 0 | Policy threshold |
| Profit_per_Unit | Profit / Quantity | Unit economics |

---

## Documentation Rule Used

For every engineered feature the following were recorded:
1. How the feature was created  
2. Why it was created  
3. Business meaning  
4. Potential value for future analysis or modelling  

---
