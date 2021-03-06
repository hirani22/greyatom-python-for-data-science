# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
data_file='file.csv'
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.vstack([data,new_record])
print(data.shape)
print(census.shape)
age=census[0]
max_age= np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
citizens_ct = np.array([len_0,len_1,len_2,len_3,len_4])
print(citizens_ct)
minority_race = citizens_ct.min()
minority_race = 3
print(minority_race)

senior_citizens=census[census[:,0]>60]
working_hours_sum=np.array(census[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours=np.mean(working_hours_sum)
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])




