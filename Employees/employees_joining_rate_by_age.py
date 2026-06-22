import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Employee.csv")
mn=df["Age"].min()
mx=df["Age"].max()
emp_count=[]
age=[]
for i in range(mn,mx+1):
    age.append(i)
    exp=df[df["Age"]==i]
    x=list(exp.shape)[0]
    emp_count.append(x)
   

plt.plot(age,emp_count,marker=".",markersize=10,
         markerfacecolor="#033F83",
         markeredgecolor="#000000",
         linestyle="solid",linewidth=2,color="#81B1FF")
plt.bar(age,emp_count)

plt.title("Employees Joining Rate by Age")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.show()

