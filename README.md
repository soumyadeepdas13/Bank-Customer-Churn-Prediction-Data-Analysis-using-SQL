# Customer Churn Analytics - Banking (UpGrad Mentor-led Internship)

**Author:** Soumyadeep Das  
**Project:** Customer Churn Analytics (Banking) — Mentor-led internship with UpGrad

---

## Problem Statement
Customer churn is a critical concern for retail banks. The objective of this project is to analyze customer behavior, identify factors that drive attrition, and build a baseline predictive model to flag customers at risk of leaving so targeted retention strategies can be designed.

## Dataset
The dataset `data/Bank_Churn_Dataset.csv` contains customer demographics and account information including: `CreditScore`, `Geography`, `Gender`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`, `EstimatedSalary` and the target variable `Exited` (1 = customer left, 0 = stayed).

## Exploratory Data Analysis (EDA)
Below are key visualizations produced during analysis (polished for corporate presentation). Each figure is located in the `images/` folder.

**Churn distribution (Stayed vs Exited)**  
![Churn distribution](images/churn_pie_polished.png)

**Age distribution**  
![Age distribution](images/age_hist_polished.png)

**Correlation matrix (numeric features)**  
![Correlation matrix](images/corr_matrix_polished.png)

**Model performance — ROC curve**  
![ROC curve](images/roc_curve_polished.png)

**Model performance — Confusion matrix**  
![Confusion matrix](images/confusion_matrix_polished.png)

**Mock professional dashboard (summary view)**  
![Mock dashboard](images/mock_dashboard_polished.png)

## Key Findings
- The overall churn rate is visible in the churn distribution image; use this to prioritize interventions.  
- Age and tenure show important variation — younger customers and those with low tenure may have different churn propensity.  
- Correlations indicate relationships between `CreditScore`, `Balance`, `Tenure` and `Exited` that can be used for feature selection.  
- Baseline Logistic Regression yields a respectable AUC (reported in `models/metrics.txt`); further model tuning is recommended.

## Recommendations
1. **Targeted retention campaigns**: Use model scores to target customers with high predicted churn probability with tailored offers.  
2. **High-value customer protection**: Identify high-balance or high-salary customers who are at risk and offer personalized incentives (fee waivers, preferential rates).  
3. **Onboarding & engagement**: Strengthen onboarding processes for low-tenure customers and offer cross-sell opportunities for customers with fewer products.  
4. **A/B test retention offers**: Run experiments to evaluate which incentives reduce churn cost-effectively.

## How to Run
1. Create and activate a virtual environment (recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. To reproduce the analysis and images:  
   - Open `analysis.ipynb` in Jupyter Notebook / JupyterLab and run cells, or run the script:  
     ```bash
     python analysis.py
     ```
4. Model artifacts are saved in the `models/` folder (`logistic_regression_baseline.pkl`, `metrics.txt`, `test_predictions.csv`).

## Licensing
This project and its contents are released under the MIT License — feel free to reuse, adapt, and extend for learning or portfolio purposes. See `LICENSE` for details.

---
*Prepared for UpGrad Mentor-led Internship submission.*
