import numpy as np
import pandas as pd
from numpy import random
from openpyxl.utils import dataframe

file_mst = open('MathScoreTerm1_out.txt', 'w')
#
MathScore = np.loadtxt('input_files/MathScoreTerm1.csv', dtype=str, delimiter=',')
arr_MathScore = np.array(MathScore)
df_MathScore = pd.DataFrame(MathScore)
#df_MathScore_sorted=df_MathScore.sort_values('0')
#print('#1.\tRead Math df_MathScore_sorted:\n', df_MathScore.sort_values('0'))
#print('#1.\tRead Math Scores:\n', df_MathScore)

df_MathScore_filtered = df_MathScore[[1, 2, 4, 5, 6]]
#print('#2.\tMath Score\n', df_MathScore_filtered)

df_MathScore_filtered_Zero_score = df_MathScore_filtered.replace(r'^\s*$', 0, regex=True)
print('#3.\tMath Scores without blank scores\n', df_MathScore_filtered_Zero_score)
# ===========

PhysicsScore = np.loadtxt('input_files/PhysicsScoreTerm1.csv', dtype=str, delimiter=',')
arr_PhysicsScore = np.array(PhysicsScore)

df_PhysicsScore = pd.DataFrame(PhysicsScore)
#print('#1.\tRead Physics Scores:\n', df_PhysicsScore)

df_PhysicsScore_filtered = df_PhysicsScore[[1, 2, 4, 5, 6]]
#print('#2.\tPhysics Scores without Names & Ethnicity\n', df_PhysicsScore_filtered)

df_PhysicsScore_filtered_Zero_score = df_PhysicsScore_filtered.replace(r'^\s*$', 0, regex=True)
print('#3.\tPhysics Scores without blank scores\n', df_PhysicsScore_filtered_Zero_score)
# ===========

DSScore = np.loadtxt('input_files/DSScoreTerm1.csv', dtype=str, delimiter=',')
arr_DSScore = np.array(DSScore)

df_DSScore = pd.DataFrame(DSScore)
#print('#1.\tRead DS Scores:\n', df_DSScore)

df_DSScore_filtered = df_DSScore[[1, 2, 4, 5, 6]]
#print('#2.\tDS Scores without Names & Ethnicity\n', df_DSScore_filtered)

df_DSScore_filtered_Zero_score = df_DSScore_filtered.replace(r'^\s*$', 0, regex=True)
print('#3.\tDS Scores without blank scores\n', df_DSScore_filtered_Zero_score)




# print('DS Score Term 1\n-----------------------------\n\n', df_DSScoreTerm1)


# df = pd.DataFrame(data)
# df_PhysicsScoreTerm1 = df[["Age", "PhD"]]
# print('DATA - AGE & PhD\n', df2)


#
# middle_tn_schools = np.loadtxt('python_mod4/777_m4_datasets_v1.0/middle_tn_schools.csv', dtype=str, delimiter=',')
# arr_middle_tn_schools = np.array(middle_tn_schools)
# df_middle_tn_schools = pd.DataFrame(middle_tn_schools)
# print('Middle TN Schools\n'.upper(), df_middle_tn_schools)
#
# ScoreFinal = np.loadtxt('python_mod4/777_m4_datasets_v1.0/ScoreFinal.csv', dtype=str, delimiter=',')
# arr_ScoreFinal = np.array(ScoreFinal)
# df_ScoreFinal = pd.DataFrame(ScoreFinal)
# print('Score Final\n', df_ScoreFinal)
