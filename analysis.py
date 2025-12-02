# analysis.py
# Reproducible script for Customer Churn Analytics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/Bank_Churn_Dataset.csv')
print('Dataset shape:', df.shape)
print(df.head())

# summary stats
print(df.describe())

# churn distribution
churn_counts = df['Exited'].value_counts().sort_index()
print('Churn counts:\n', churn_counts)

# simple plots (will overwrite images in images/)
plt.figure(figsize=(6,4))
plt.hist(df['Age'].dropna(), bins=20)
plt.title('Age distribution')
plt.xlabel('Age'); plt.ylabel('Count'); plt.tight_layout()
plt.savefig('images/age_hist.png'); plt.close()

plt.figure(figsize=(5,5))
labels = ['Stayed','Exited']
plt.pie(churn_counts.values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Churn (Exited vs Stayed)')
plt.savefig('images/churn_pie.png'); plt.close()

# correlation heatmap (numeric columns)
num = df.select_dtypes(include=[np.number]).drop(columns=['RowNumber','CustomerId'], errors='ignore')
corr = num.corr()
plt.figure(figsize=(8,6))
im = plt.imshow(corr, interpolation='nearest', aspect='auto')
plt.colorbar(im, fraction=0.046, pad=0.04)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.index)), corr.index)
for i in range(len(corr.index)):
    for j in range(len(corr.columns)):
        plt.text(j, i, '{:.2f}'.format(corr.iloc[i, j]), ha='center', va='center', fontsize=8)
plt.title('Correlation matrix (numeric features)'); plt.tight_layout()
plt.savefig('images/corr_matrix.png'); plt.close()

# Top 5 customers example
top5 = df.sort_values(by=['CreditScore','Balance','EstimatedSalary','Tenure'], ascending=False).head(5)
top5.to_csv('top5_customers.csv', index=False)
print('Top 5 customers saved to top5_customers.csv')
