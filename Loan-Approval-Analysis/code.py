# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)
bank.head()
#Code starts here
categorical_var= bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var= bank.select_dtypes(include = 'number')
print(numerical_var)

#Step2
banks= bank.drop(['Loan_ID'], axis=1)
print(banks.isnull().sum())
bank_mode= banks.mode()
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

#Step3
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'], values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)

#Step4
Loan_Status=614
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count()
percentage_se = (loan_approved_se/Loan_Status)*100
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count()
percentage_nse = (loan_approved_nse/Loan_Status)*100
print(percentage_se)
print(percentage_nse)

#Step5
loan_term = banks['Loan_Amount_Term'].apply(lambda months : months/12 )
big_loan_term = loan_term[loan_term >= 25].size
print(big_loan_term)

#Step6
loan_groupby = banks.groupby('Loan_Status')
loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()



