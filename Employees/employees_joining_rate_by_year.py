import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Employee.csv")
mn=df["JoiningYear"].min()
mx=df["JoiningYear"].max()
emp_count=[]
year=[]
for i in range(mn,mx+1):
    year.append(i)
    exp=df[df["JoiningYear"]==i]
    x=list(exp.shape)[0]
    emp_count.append(x)
   
plt.plot(year,emp_count,marker=".",markersize=30,
         markerfacecolor="#033F83",
         markeredgecolor="#000000",
         linestyle="solid",linewidth=3,color="#81B1FF")
plt.bar(year,emp_count)
plt.title("Employees Joining Rate by Year")
plt.xlabel("Joining Year")
plt.ylabel("Number of Employees")
plt.show()

