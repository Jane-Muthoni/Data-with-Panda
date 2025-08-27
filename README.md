Iris Dataset Analysis & Visualization
This Python program explores the Iris dataset using `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`. It provides statistical summaries and data visualizations to help you understand the dataset better.
Features
- Load Iris dataset safely with error handling
- Display:
  - First five rows
  - Data types
  - Missing values
  - Basic statistics
  - Mean values grouped by species
- Key insight: Setosa has a smaller petal length and width than Versicolor and Virginica.
Visualizations
- Line Plot: Sepal Length & Width over samples
- Bar Chart: Average petal length per species
- Histogram: Petal width distribution
- Scatter Plot: Sepal length vs Petal length by species
Requirements
Install required libraries:
``"ash
pip install pandas matplotlib seaborn scikit-learn
 Run the Program
bash
python iris_analysis.py
Example Output
First five rows:
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
0                5.1               3.5                1.4               0.2  setosa
1                4.9               3.0                1.4               0.2  setosa
