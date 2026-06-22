import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Employee.csv")
city1=df[df["City"]=="Pune"]
city2=df[df["City"]=="Bangalore"]
city3=df[df["City"]=="New Delhi"]


total_employees=list(df.shape)[0]
num1=list(city1.shape)[0]
num2=list(city2.shape)[0]
num3=list(city3.shape)[0]

city1_per=(int(num1)/int(total_employees))*100
city2_per=(int(num2)/int(total_employees))*100
city3_per=(int(num3)/int(total_employees))*100

City_names=["Pune","Bangalore","New Delhi"]
num_of_emp=[city1_per,city2_per,city3_per]


colours=["#e62cff","#FF8F18","#0d9aff"]
plt.pie(num_of_emp,
        labels=City_names,autopct="%1.1f%%",
        colors=colours,shadow=True,)
plt.title("Employment percentage by City")
plt.show()
