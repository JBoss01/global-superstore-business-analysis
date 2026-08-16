# Global Superstore Business Intelligence Dashboard

<div align="center">

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Data Analytics](https://img.shields.io/badge/Data%20Analytics-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-FF6F00?style=for-the-badge)

</div>


**Week 2 Project | Data Analytics Internship – AnalystLab Africa Consulting**

---

## 📌 Project Overview

This project involves the end-to-end development of an interactive **Business Intelligence dashboard** using Microsoft Power BI. The dashboard was built to help senior management of a retail company monitor sales performance, profitability, customer behaviour, and regional results.

**Dataset:** Global Superstore (51,290 transactions | 147 countries | 2011–2014)
https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset

---

## 🎯 Business Problem

Management lacked a single, interactive view of business performance. Key questions that needed answering included:

- What is the overall sales performance of the company?
- Which regions and markets generate the highest sales and profit?
- Which customer segments contribute the most revenue?
- Which product categories and products are most profitable?
- What trends can be observed over time?
- What recommendations should management implement?

---

## 🛠️ Project Workflow

### 1. Data Preparation (Power Query)
- Converted Order Date and Ship Date from text to Date format
- Trimmed trailing spaces in Product Name
- Changed Postal Code data type to Text
- Created helper columns: Year, Month, Month Number
- Checked for missing values, duplicates, and data quality issues
- Validated logical consistency (e.g., Ship Date ≥ Order Date)

### 2. Dashboard Development (Power BI)
**KPI Cards**
- Total Sales
- Total Profit
- Total Orders
- Average Sales
- Profit Margin %

**Visualizations**
- Line Chart – Sales & Profit Trend over Time
- Donut Chart – Sales by Category
- Bar Charts – Sales by Region, Sales by Customer Segment
- Column Chart – Sales by Market
- Matrix – Category & Sub-Category Performance

**Interactivity**
- Slicers for Year, Market, Region, Segment, and Category

### 3. Business Insights & Recommendations
- 5 Key Business Insights
- 3 Business Risks
- 3 Business Opportunities
- 5 Actionable Recommendations

---

## 📊 Key Insights

| Insight | Finding |
|---------|---------|
| Top Category | Technology ($4.74M sales, 14% margin) |
| Top Segment | Consumer (over 50% of total revenue) |
| Top Region | Central Region |
| Top Market | APAC |
| Growth Trend | Consistent year-on-year growth (2011–2014) |
| Profit Challenge | Tables sub-category recorded losses |

---

## 🧰 Tools & Technologies

- **Microsoft Power BI Desktop**
- **Power Query** (Data cleaning & transformation)
- **DAX** (KPI measures)
- **Global Superstore Dataset**

---

## 📁 Project Structure
```text
├── Global_Superstore_Dashboard.pbix
├── BI_Overview_and_Executive_Summary_Report.docx
├── README.md
└── screenshots/
```
---

## 📄 Reports
- [Business Intelligence Overview Report](./BI_Overview_Report.md)
- [Executive Summary Report](./Executive_Summary_Report.md)

## 📸 Dashboard Screenshots

Executive Overview
<image-card alt="Executive Overview" src="./screenshots/executive-overview.png" ></image-card>

Regional & Market Performance
<image-card alt="Regional Performance" src="./screenshots/regional-performance.png" ></image-card>

Insights & Recommendations
<image-card alt="Insights" src="./screenshots/insights-recommendations.png" ></image-card>

## 🎓 Skills Demonstrated

- Data cleaning and transformation
- DAX measure development
- Interactive dashboard design
- Business analysis and insight generation
- Data storytelling
- Strategic recommendation writing
- Professional documentation

---

## 👤 Author

**Ozoeze Wilord Ugonna**  
Junior Business Intelligence Analyst  
Data Analytics Internship – AnalystLab Africa Consulting

---

## 📄 License

This project was completed as part of a professional internship assignment.
