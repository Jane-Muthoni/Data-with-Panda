import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

except Exception as e:
    print(f"Error loading dataset: {e}")
    exit(1)

print("First 5 rows:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
print("\nMissing values per column:")
print(df.isnull().sum())

df = df.dropna() 
print("\nBasic statistics:")
print(df.describe())

print("\nMean values by species:")
print(df.groupby('species').mean())

print("\nObservations:")
print("Setosa has smaller petal length and width compared to versicolor and virginica.")

sns.set(style="whitegrid")

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['sepal width (cm)'], label='Sepal Width')
plt.title('Sepal Length and Width over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Centimeters')
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, palette="viridis")
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['petal width (cm)'], bins=15, kde=True, color='purple')
plt.title('Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
