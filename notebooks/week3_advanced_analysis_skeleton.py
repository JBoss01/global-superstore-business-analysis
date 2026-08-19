"""
Global Superstore – Week 3
Advanced Data Analysis, Statistical Validation & Feature Engineering
Analyst: Ozoeze Wilord Ugonna
AnalystLab Africa Data Science Internship

This file is a complete code skeleton. Copy sections into a Jupyter notebook
and run cell by cell. Replace the data path with your Week 2 cleaned file
if different.
"""

# ============================================================
# 0. SETUP
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 5)

# ============================================================
# 1. LOAD WEEK 2 CLEANED DATA
# ============================================================
# Update path if your cleaned file lives elsewhere
DATA_PATH = "../data/Global_Superstore2.xlsx"  # or your week2 cleaned csv

df = pd.read_excel(DATA_PATH)  # or pd.read_csv(...)
print("Shape:", df.shape)
print(df.columns.tolist())
df.head()

# Parse dates (if not already done in Week 2)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

# ============================================================
# 2. PROJECT CONTINUITY (short recap in markdown cells)
# ============================================================
# In the notebook, write a markdown section covering:
# - Business problem
# - Target variable (Profit / profitability)
# - Week 1 key findings
# - Week 2 cleaning summary
# - Questions still open for Week 3

# ============================================================
# 3. ADVANCED EDA – NUMERICAL
# ============================================================
num_cols = ["Sales", "Quantity", "Discount", "Profit", "Shipping Cost"]

# Distributions, skewness, variability
display(df[num_cols].describe())
print("Skewness:\n", df[num_cols].skew())

# Histograms / KDE
for col in num_cols:
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    ax.set_title(f"Distribution of {col}")
    plt.show()

# Boxplots for outlier view
fig, ax = plt.subplots()
sns.boxplot(data=df[num_cols], orient="h", ax=ax)
ax.set_title("Boxplots – Numerical Features")
plt.show()

# ============================================================
# 4. ADVANCED EDA – CATEGORICAL
# ============================================================
cat_cols = ["Category", "Segment", "Ship Mode", "Order Priority", "Market"]

for col in cat_cols:
    print(f"\n=== {col} ===")
    print(df[col].value_counts(normalize=True).round(3))

# Example: Category vs Profit
fig, ax = plt.subplots()
sns.barplot(data=df, x="Category", y="Profit", estimator=np.mean, ci=95, ax=ax)
ax.set_title("Average Profit by Category")
plt.show()

# Loss rate by Category
loss_rate = df.assign(loss=df["Profit"] < 0).groupby("Category")["loss"].mean()
print("Loss rate by Category:\n", (loss_rate * 100).round(1))

# ============================================================
# 5. BIVARIATE & MULTIVARIATE
# ============================================================
# Correlation heatmap
corr = df[num_cols].corr(method="spearman")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, ax=ax)
ax.set_title("Spearman Correlation – Numerical Features")
plt.show()

# Scatter: Sales vs Profit coloured by Category
fig, ax = plt.subplots()
sns.scatterplot(data=df.sample(3000, random_state=42), x="Sales", y="Profit",
                hue="Category", alpha=0.5, ax=ax)
ax.set_title("Sales vs Profit by Category (sample)")
plt.show()

# Discount vs Profit
fig, ax = plt.subplots()
sns.boxplot(data=df, x=pd.cut(df["Discount"], bins=[-0.01, 0, 0.2, 0.5, 1]),
            y="Profit", ax=ax)
ax.set_title("Profit by Discount Band")
plt.show()

# ============================================================
# 6. STATISTICAL HYPOTHESIS TESTING (minimum 4)
# ============================================================

# --- Test 1: Kruskal-Wallis – Profit across Categories ---
groups = [g["Profit"].dropna().values for _, g in df.groupby("Category")]
stat, p = stats.kruskal(*groups)
print("Test 1 – Kruskal-Wallis (Profit ~ Category)")
print(f"  H statistic = {stat:.4f}, p-value = {p:.4e}")
print("  Decision:", "Reject H0" if p < 0.05 else "Fail to reject H0")

# --- Test 2: Mann-Whitney – Discounted vs Non-discounted Profit ---
no_disc = df.loc[df["Discount"] == 0, "Profit"].dropna()
with_disc = df.loc[df["Discount"] > 0, "Profit"].dropna()
stat, p = stats.mannwhitneyu(no_disc, with_disc, alternative="two-sided")
print("\nTest 2 – Mann-Whitney (Profit: No Discount vs Discount)")
print(f"  U statistic = {stat:.4f}, p-value = {p:.4e}")
print("  Mean No Discount =", no_disc.mean())
print("  Mean With Discount =", with_disc.mean())
print("  Decision:", "Reject H0" if p < 0.05 else "Fail to reject H0")

# --- Test 3: Chi-Square – Segment vs Order Priority ---
ct = pd.crosstab(df["Segment"], df["Order Priority"])
chi2, p, dof, exp = stats.chi2_contingency(ct)
print("\nTest 3 – Chi-Square (Segment vs Order Priority)")
print(f"  Chi2 = {chi2:.4f}, dof = {dof}, p-value = {p:.4e}")
print("  Decision:", "Reject H0" if p < 0.05 else "Fail to reject H0")

# --- Test 4: Spearman correlations ---
print("\nTest 4 – Spearman Correlations with Profit")
for col in ["Sales", "Discount", "Shipping Cost", "Quantity"]:
    r, p = stats.spearmanr(df[col], df["Profit"], nan_policy="omit")
    print(f"  {col}: rho = {r:.4f}, p = {p:.4e}")

# In the notebook: for EACH test write H0, H1, justification, interpretation, business implication.

# ============================================================
# 7. FEATURE ENGINEERING (minimum 3)
# ============================================================
# 1. Profit Margin
df["Profit_Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], np.nan)

# 2. Is Loss Making
df["Is_Loss_Making"] = (df["Profit"] < 0).astype(int)

# 3. Discount Impact (approx. revenue given away)
df["Discount_Impact"] = df["Sales"] * df["Discount"]

# 4. Shipping Efficiency
df["Shipping_Efficiency"] = np.where(df["Sales"] != 0,
                                     df["Shipping Cost"] / df["Sales"], np.nan)

# 5. Days to Ship
df["Days_to_Ship"] = (df["Ship Date"] - df["Order Date"]).dt.days

print(df[["Profit_Margin", "Is_Loss_Making", "Discount_Impact",
          "Shipping_Efficiency", "Days_to_Ship"]].describe())

# Document each feature in markdown: how, why, business meaning, modelling value.

# ============================================================
# 8. FEATURE EVALUATION & SELECTION
# ============================================================
# Correlation including new features
eval_cols = ["Sales", "Quantity", "Discount", "Profit", "Shipping Cost",
             "Profit_Margin", "Discount_Impact", "Shipping_Efficiency", "Days_to_Ship"]
corr2 = df[eval_cols].corr(method="spearman")
fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(corr2, annot=True, fmt=".2f", cmap="RdBu_r", center=0, ax=ax)
ax.set_title("Correlation – Original + Engineered Features")
plt.show()

# Simple association of engineered features with loss flag
print("Mean feature values by Is_Loss_Making:")
print(df.groupby("Is_Loss_Making")[["Discount", "Discount_Impact",
                                    "Shipping_Efficiency", "Profit_Margin"]].mean())

# Decisions (write in markdown):
# - Drop pure IDs: Row ID, Order ID, Customer Name, Product Name, Postal Code
# - Watch leakage: if predicting Is_Loss_Making, do not use Profit or Profit_Margin as inputs
# - Keep: Category, Segment, Market, Ship Mode, Discount, Sales, Quantity, Shipping Cost + engineered features

# ============================================================
# 9. DATASET REFINEMENT & EXPORT
# ============================================================
modelling_cols = [
    # identifiers kept only if needed for traceability (optional)
    # "Order ID",
    "Order Date", "Segment", "City", "State", "Country", "Market", "Region",
    "Category", "Sub-Category", "Sales", "Quantity", "Discount", "Profit",
    "Shipping Cost", "Ship Mode", "Order Priority",
    # engineered
    "Profit_Margin", "Is_Loss_Making", "Discount_Impact",
    "Shipping_Efficiency", "Days_to_Ship",
]

df_model = df[modelling_cols].copy()
out_path = "../data/global_superstore_modelling_dataset.csv"
df_model.to_csv(out_path, index=False)
print("Saved modelling dataset:", out_path, "Shape:", df_model.shape)

# ============================================================
# 10. BUSINESS INSIGHTS (markdown in notebook + separate report)
# ============================================================
# Summarise:
# - Key patterns confirmed by statistics
# - Role of engineered features
# - Recommendations (discount policy, category focus, operations)
# - Limitations
# - Next steps for Week 4 modelling

print("Week 3 skeleton complete.")
