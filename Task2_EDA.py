import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Titanic data
data = {
    'Survived': [0,1,0,1,1,0,1,0],
    'Age': [22,38,26,35,28,2,45,27],
    'Sex': ['male','female','female','male','female','male','male','female'],
    'Pclass': [3,1,3,1,2,3,1,2]
}
df = pd.DataFrame(data)

print("--- Data Head ---")
print(df.head())

print("\n--- Info ---")
print(df.info())

print("\n--- Describe ---")
print(df.describe())

# Visualization
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()
