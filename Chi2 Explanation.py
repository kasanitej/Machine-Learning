# chi-squared test with similar proportions
from scipy.stats import chi2_contingency,chi2
import pandas as pd
import numpy as np

#The variables are considered independent if the observed and expected frequencies are similar
#Null hypothesis(H0) means independent variable

df = pd.DataFrame([[31,14,45],[2,5,53],[53,45,2]],columns=['Asia','Africa','South-America'],
                    index=['Malaria-A','Malaria-B','Malaria-C'])

table= df.values

###########This segment is for understanding################################
dof_calc = (table.shape[0]-1)*(table.shape[1]-1)

def Expected_calc(table):
    total = np.sum(table)
    col_sum = np.sum(table, axis=0)
    col_sum = np.repeat(col_sum, table.size/col_sum.size).reshape(table.shape)
    col_sum = np.transpose(col_sum)
    row_sum = np.sum(table, axis=1)
    row_sum = np.repeat(row_sum, table.size/row_sum.size).reshape(table.shape)
    expected_cal = np.multiply(row_sum, col_sum)/total
    print(expected_cal)

def chi2_calculated(table, expected):
    rms = np.divide((table-expected)**2, expected)
    return np.sum(rms)
#####################*************End*************##########################

chi_2, prob, dof, expected = chi2_contingency(table)
critical_chi2 = chi2.ppf(0.95, dof)#Percent point function in lookup table you have to look at 0.05<---(1-0.95)

print('Criticial:',critical_chi2)
print('Actual   :',chi_2)

if critical_chi2<chi_2:
    print('------------>There is a relation between Malaria & Region<----------------------')
else:
    print('------------>There is no relation between Malaria & Region<---------------------')
# Expected_calc(table)
# print(dof_calc)
# print('actual:',dof)
