import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
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