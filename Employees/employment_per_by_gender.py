import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Employee.csv")
ladies=df[df["Gender"]=="Female"]
gents=df[df["Gender"]=="Male"]


total_employees=list(df.shape)[0]
total_ladies=list(ladies.shape)[0]
total_gents=list(gents.shape)[0]

ladies_per=(int(total_ladies)/int(total_employees))*100
gents_per=(int(total_gents)/int(total_employees))*100

colours=["#30f000","#0A35F4"]
plt.pie([ladies_per,gents_per],
        labels=["Female Employees","Male Employees"],autopct="%1.1f%%",
        colors=colours,shadow=True,)
plt.title("Employment percentage by gender")
plt.show()