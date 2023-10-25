import numpy as np

import pandas as pd

a1 = pd.DataFrame({

    'Дата': pd.Timestamp('20231025'),
    'Товар': ['apple', 'orange', 'apple', 'orange'],
    'Количество': np.random.randint(7,35,4)
}
)

b1 = pd.DataFrame(a1.groupby('Товар')['Количество'].sum())


def count_sum(df):
    return b1


print(count_sum(a1))

# print(a1)
# print(b1)
