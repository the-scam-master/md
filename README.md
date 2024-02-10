# Adjusted R-squared - Exercise Solution

Using the code from the lecture, create a function which will calculate the adjusted R-squared for you, given the independent variable(s) (x) and the dependent variable (y).

Check if you function is working properly.

Solution at the bottom.

## Import the relevant libraries


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
```

## Load the data


```python
data = pd.read_csv('1.02. Multiple linear regression.csv')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SAT</th>
      <th>Rand 1,2,3</th>
      <th>GPA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1714</td>
      <td>1</td>
      <td>2.40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1664</td>
      <td>3</td>
      <td>2.52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1760</td>
      <td>3</td>
      <td>2.54</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1685</td>
      <td>3</td>
      <td>2.74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1693</td>
      <td>2</td>
      <td>2.83</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SAT</th>
      <th>Rand 1,2,3</th>
      <th>GPA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>84.000000</td>
      <td>84.000000</td>
      <td>84.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1845.273810</td>
      <td>2.059524</td>
      <td>3.330238</td>
    </tr>
    <tr>
      <th>std</th>
      <td>104.530661</td>
      <td>0.855192</td>
      <td>0.271617</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1634.000000</td>
      <td>1.000000</td>
      <td>2.400000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1772.000000</td>
      <td>1.000000</td>
      <td>3.190000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1846.000000</td>
      <td>2.000000</td>
      <td>3.380000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1934.000000</td>
      <td>3.000000</td>
      <td>3.502500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2050.000000</td>
      <td>3.000000</td>
      <td>3.810000</td>
    </tr>
  </tbody>
</table>
</div>



## Create the multiple linear regression

### Declare the dependent and independent variables


```python
x = data[['SAT','Rand 1,2,3']]
y = data['GPA']
```

### Regression itself


```python
reg = LinearRegression()
reg.fit(x,y)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)




```python
reg.coef_
```




    array([ 0.00165354, -0.00826982])




```python
reg.intercept_
```




    0.29603261264909486



### Calculating the R-squared


```python
reg.score(x,y)
```




    0.4066811952814285



### Formula for Adjusted R^2

$R^2_{adj.} = 1 - (1-R^2)*\frac{n-1}{n-p-1}$


```python
x.shapeFormula for Adjusted R^2

𝑅2𝑎𝑑𝑗.=1−(1−𝑅2)∗𝑛−1𝑛−𝑝−1
```




    (84, 2)




```python
r2 = reg.score(x,y)
n = x.shape[0]
p = x.shape[1]

adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
adjusted_r2
```




    0.39203134825134023



### Adjusted R^2 function


```python
# There are different ways to solve this problem
# To make it as easy and interpretable as possible, we have preserved the original code
def adj_r2(x,y):
    r2 = reg.score(x,y)
    n = x.shape[0]
    p = x.shape[1]
    adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
    return adjusted_r2
```


```python
# Here's the result
adj_r2(x,y)
```




    0.39203134825134023


