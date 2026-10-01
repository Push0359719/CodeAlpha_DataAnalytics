import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Data
data = {'Month':['Jan','Feb','Mar','Apr','May','Jun'], 'Sales':[20000,25000,18000,30000,35000,40000]}
df = pd.DataFrame(data)

# Line Plot
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales - CodeAlpha Task 3')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# Bar Plot
plt.bar(df['Month'], df['Sales'], color='green')
plt.title('Sales Visualization')
plt.show()
