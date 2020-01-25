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
                    ["Jimmy",20],
                    ["Jane",20],
                    ["Jimmy",np.nan],
                    ["Helena",24],
                    ], dtype='category')