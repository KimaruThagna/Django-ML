import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer
from sklearn.impute._iterative import IterativeImputer
# sample dataset Name and age of random college students
df = pd.DataFrame([
                    ["Ann", 20],
                    ["Mike",21],
                    ["Alice",np.nan ],
                    ["Jane",20],
                    ["liam",19],
                    ["Sue",20],
                    ["Jane",20],
                    ["Jimmy",np.nan],
                    ["Helena",24],
                    ], dtype='category')

# univariate imputation
imp = SimpleImputer(strategy="most_frequent") # could be most_frequent, least_frequent, constant_value, mean, median
print(imp.fit_transform(df))
# multivariate imputation
mi = IterativeImputer(max_iter=1000, random_state=0)
mi.fit([[1, 0.5], [3, 1.5], [4, 2], [np.nan, 100], [7, np.nan]])
X_test = [[np.nan, 100], [60, np.nan], [np.nan, 7]]
print(np.round(mi.transform(X_test)))