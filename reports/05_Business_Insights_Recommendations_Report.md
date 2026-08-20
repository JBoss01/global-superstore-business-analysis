# Business Insights and Recommendations Report
**Global Superstore**  
**AnalystLab Africa – Data Science Internship | Week 3**  
**Analyst:** Ozoeze Wilord Ugonna

---

## 1. Executive Summary

Global Superstore generated approximately **$12.64 million** in sales and **$1.47 million** in profit across 51,290 orders (overall margin ≈ **11.6%**).

However, **nearly 1 in 4 orders (24.5%) loses money**. Discounting is a major driver of these losses: orders with any discount show an average profit of about **−$13.60**, while orders with no discount average about **+$61**.

Technology is the strongest category by average profit; Furniture carries the highest loss rate. These patterns were reinforced by formal statistical tests and by newly engineered features (Profit Margin, Loss Flag, Discount Impact, Shipping Efficiency).

This report summarises the key analytical findings, their business meaning, and prioritised recommendations. The refined dataset is ready for predictive modelling in Week 4.

---

## 2. Key Analytical Findings

### 2.1 Profitability Patterns
- Technology delivers the highest average profit per order (~$65).
- Furniture has the highest share of loss-making orders (~32%).
- Office Supplies has the lowest average profit but a large volume of orders.

### 2.2 Discounting Destroys Value
- ~43% of orders receive a discount.
- Discounted orders are, on average, unprofitable.
- Correlation between Discount and Profit is clearly negative (≈ −0.32).

### 2.3 Operational & Geographic Signals
- Shipping cost rises with order value, but efficiency (shipping cost as a share of sales) varies by Ship Mode and Market.
- Performance differs across Markets (APAC, LATAM, EU, US, EMEA, Africa, Canada); geographic strategy should be data-led.

### 2.4 Feature Insights
New features made the above patterns clearer:
- **Profit_Margin** – enables fair comparison across order sizes.
- **Is_Loss_Making** – turns the 24.5% loss rate into a trackable KPI and potential model target.
- **Discount_Impact** – quantifies revenue given away.
- **Shipping_Efficiency** – highlights costly fulfilment relative to revenue.

---

## 3. Business Implications

| Finding | Implication for Leadership |
|---------|----------------------------|
| High loss rate (24.5%) | Margin leakage is systemic, not isolated |
| Discounted orders often unprofitable | Discount policy is currently misaligned with profit goals |
| Furniture underperforms | Category needs tighter pricing, discount rules, or cost review |
| Technology outperforms | Growth investment here has stronger profit support |
| Shipping efficiency varies | Opportunity to optimise ship mode and carrier choices |

Without intervention, continued aggressive discounting and weak category controls will keep eroding overall margin.

---

## 4. Recommendations

### Priority 1 – Redesign Discount Policy (Immediate)
- Cap discounts on Furniture and on low-margin sub-categories.
- Require approval above a defined discount threshold (e.g. 20%).
- Monitor **Discount_Impact** as a weekly KPI.

### Priority 2 – Protect and Grow Technology
- Allocate marketing and inventory priority to Technology.
- Use Technology as the reference for healthy margin behaviour.

### Priority 3 – Furniture Turnaround
- Review cost structure and list prices.
- Reduce reliance on deep discounts to clear stock.
- Track Furniture loss rate monthly with a clear reduction target.

### Priority 4 – Operational Efficiency
- Analyse Ship Mode performance using **Shipping_Efficiency**.
- Prefer modes that balance speed and cost for each order-value band.

### Priority 5 – Prepare for Predictive Control (Week 4)
- Use the refined modelling dataset to predict **Is_Loss_Making** or **Profit**.
- Deploy a simple scoring approach so high-risk orders can be flagged before confirmation.

---

## 5. Dataset Limitations

- **Postal Code** is missing for most non-US rows → limited micro-geographic analysis.
- **Profit** in the dataset is given; full cost breakdown (COGS, overhead) is not available → margin interpretation is constrained to provided fields.
- High-cardinality fields (Customer, Product Name, City) limit stable modelling without aggregation or encoding strategies.
- Observational data only → statistical associations are not proof of causation.
- Time span and market mix may limit generalisation to future periods or new regions.

---

## 6. Next Steps (Week 4 – Machine Learning)

The refined modelling dataset produced in Week 3 will support:

1. **Classification models** predicting `Is_Loss_Making`
2. **Regression models** predicting `Profit` or `Profit_Margin`
3. Evaluation of model lift versus current rules-based discounting
4. Final business recommendations backed by both statistical evidence and predictive performance

Week 3 will move from descriptive insight to **validated, feature-rich, modelling-ready evidence**.

---

