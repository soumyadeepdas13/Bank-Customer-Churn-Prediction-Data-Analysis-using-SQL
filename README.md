

📊 Customer Churn Analytics – Banking

Mentor-Led Internship Project (UpGrad)

Understanding why customers leave is one of the most important challenges for retail banks. This project analyzes customer behavior, identifies the major drivers of churn, and builds a baseline predictive model to help banks proactively retain high-risk customers.

---

🚨 Problem Statement

Banks face increasing difficulty in retaining customers due to competition, digital alternatives, and diverse customer expectations.

Goal:
To perform churn analysis using customer demographics and account-related attributes, explore key patterns, and build a predictive model to classify high-risk customers so that targeted retention measures can be implemented.

---

📁 Dataset

The dataset used for this project is:
data/Bank_Churn_Dataset.csv

It contains the following columns:
	•	CreditScore
	•	Geography
	•	Gender
	•	Age
	•	Tenure
	•	Balance
	•	NumOfProducts
	•	HasCrCard
	•	IsActiveMember
	•	EstimatedSalary
	•	Exited (Target: 1 = churned, 0 = stayed)

These features help uncover behavioral and financial patterns linked to customer attrition.

---

🔍 Exploratory Data Analysis (EDA)

Below are the key visual insights generated during analysis:

📌 Churn Distribution

<img width="1400" height="1000" alt="churn_pie_polished" src="https://github.com/user-attachments/assets/aedefafb-a7e3-4a6c-aa4e-15d083779a44" />

---

🏆 Top 5 Customers (Based on Score, Tenure & Balance)


<img width="1600" height="800" alt="top5_customers" src="https://github.com/user-attachments/assets/09ef34c6-d2d5-4d06-b80e-360d85e1bfc2" />

---

👤 Age Distribution


<img width="1600" height="1000" alt="age_hist_polished" src="https://github.com/user-attachments/assets/23199090-2f2d-43c4-a62e-b7c836ccd563" />


---

🧩 Correlation Matrix


<img width="2000" height="1600" alt="corr_matrix_polished" src="https://github.com/user-attachments/assets/93c3717b-14f4-4942-ba97-ef3bfea21dfa" />


---

📈 ROC Curve (Model Performance)


<img width="1400" height="1000" alt="roc_curve_polished" src="https://github.com/user-attachments/assets/77bc5142-eb93-4cec-8fca-ad21afb6e6f5" />

---

📊 Mock Professional Dashboard


<img width="2400" height="1200" alt="mock_dashboard_polished" src="https://github.com/user-attachments/assets/b008ecfc-a1fc-4579-a477-f35aeb905928" />



---

🧠 Key Findings
	•	Churn rate is moderate, indicating immediate need for targeted retention strategies.
	•	Age and tenure play a major role — younger customers and low-tenure accounts show higher churn probability.
	•	Credit score, balance, and activity level influence churn and are strong candidates for feature engineering.
	•	The baseline Logistic Regression model achieves a solid AUC (see models/metrics.txt), but improvements are possible with:
	•	Hyperparameter tuning
	•	Ensemble models
	•	Better data balancing techniques

---

⚙️ How to Run This Project

1. Clone the repository

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Install dependencies

pip install -r requirements.txt

3. Run the analysis

To execute the full workflow:

python analysis.py

—or open—

analysis.ipynb

for a step-by-step notebook version.

4. Model results

Results (metrics, exported figures, predictions) are stored inside the:

/models
/plots


---



📝 Prepared For

UpGrad Mentor-Led Internship Program (Business Analytics & Data Science Track)
Project: Customer Churn Analytics – Banking

---

