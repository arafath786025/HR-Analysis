#import pandas
import pandas as pd

#import file

df=pd.read_csv("E:\Project\HR Analysis\Dataset\HR Analysis.csv")
print(df)
print("\n")

#create new column

df['Attrition_Flag'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
print("Attrition_Flag:",df['Attrition_Flag'])
print("\n")

#total employees

total_employees=len(df)
print("total_employees:",total_employees)
print("\n")

#total attritions

total_attritions=df['Attrition_Flag'].sum()
print("total_attritions:",total_attritions)
print("\n")

#attrition rate

attrition_rate=round((total_attritions / total_employees) * 100,2)
print("attrition_rate:",attrition_rate)
print("\n")

#basic matrics

basic_matrics=pd.DataFrame({'Matrics': ['Total_Employees','Total_Attrition','Attrition_Rate (%)'], 'Values': [total_employees,total_attritions,attrition_rate] })
print("basic_matrics:",basic_matrics)
print("\n")

#attrition by department

dept_attrition = df.groupby('Department')['Attrition_Flag'].sum().reset_index()
print("dept_attrition:",dept_attrition)
print("\n")

#attrition by job role

jobrole_attrition = df.groupby('JobRole')['Attrition_Flag'].sum().reset_index()
print("jobrole_attrition:",jobrole_attrition)
print("\n")


#attrition by gender

gender_attrition = df.groupby('Gender')['Attrition_Flag'].sum().reset_index()
print("gender_attrition:",gender_attrition)
print("\n")

#attrition by job satisfaction

jobsat_attrition = df.groupby('JobSatisfaction')['Attrition_Flag'].sum().reset_index()
print("job_satisfaction_attrition:",jobsat_attrition)
print("\n")

#age group analysis

bins = [18, 25, 35, 45, 60]
labels = ['18-25', '26-35', '36-45', '46-60']

df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
print("Age_Group:",df['Age_Group'])
print("\n")

#attrition by age

age_attrition = df.groupby('Age_Group')['Attrition_Flag'].sum().reset_index()
print("age_attrition:",age_attrition)
print("\n")

#save all the outputs in excel format

with pd.ExcelWriter("HR_Analysis_Outputs.xlsx",engine='openpyxl') as writer:
    basic_matrics.to_excel(writer, sheet_name='Basic_Matrics', index= False)
    dept_attrition.to_excel(writer, sheet_name='Attrition_by_Department', index=False)
    jobrole_attrition.to_excel(writer, sheet_name='Attrition_by_Job_Role', index=False)
    gender_attrition.to_excel(writer, sheet_name='Attrition_by_Gender', index=False)
    jobsat_attrition.to_excel(writer, sheet_name='Attrition_by_Job_Satisfaction', index=False)
    age_attrition.to_excel(writer, sheet_name='Attrition_by_Age', index=False)
    
