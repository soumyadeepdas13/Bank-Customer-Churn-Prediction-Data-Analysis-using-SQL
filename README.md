Customer Churn Analytics - Banking (UpGrad Mentor-led Internship)


Project: Customer Churn Analytics (Banking) — Mentor-led internship with UpGrad

---

Problem Statement
Customer churn is a critical concern for retail banks. The objective of this project is to analyze customer behavior, identify factors that drive attrition, and build a baseline predictive model to flag customers at risk of leaving so targeted retention strategies can be designed.

Dataset
The dataset `data/Bank_Churn_Dataset.csv` contains customer demographics and account information including: `CreditScore`, `Geography`, `Gender`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`, `EstimatedSalary` and the target variable `Exited` (1 = customer left, 0 = stayed).

Exploratory Data Analysis (EDA)
Below are key visualizations produced during analysis 

Churn distribution (Stayed vs Exited)
<img width="1400" height="1000" alt="churn_pie_polished" src="https://github.com/user-attachments/assets/aedefafb-a7e3-4a6c-aa4e-15d083779a44" />

Top 5 customers
<img width="1600" height="800" alt="top5_customers" src="https://github.com/user-attachments/assets/09ef34c6-d2d5-4d06-b80e-360d85e1bfc2" />


Age distribution
<img width="1600" height="1000" alt="age_hist_polished" src="https://github.com/user-attachments/assets/23199090-2f2d-43c4-a62e-b7c836ccd563" />


Correlation matrix (numeric features)
<img width="2000" height="1600" alt="corr_matrix_polished" src="https://github.com/user-attachments/assets/93c3717b-14f4-4942-ba97-ef3bfea21dfa" />


Model performance — ROC curve
<img width="1400" height="1000" alt="roc_curve_polished" src="https://github.com/user-attachments/assets/77bc5142-eb93-4cec-8fca-ad21afb6e6f5" />

Model performance — Confusion matrix
<img width="900" height="900" alt="confusion_matrix_polished" src="https://github.com/user-attachments/assets/38901bae-0d93-411e-b6c5-2e213296a04c" />


Mock professional dashboard (summary view)  
<img width="2400" height="1200" alt="mock_dashboard_polished" src="https://github.com/user-attachments/assets/b008ecfc-a1fc-4579-a477-f35aeb905928" />


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

---
*Prepared for UpGrad Mentor-led Internship submission.*
