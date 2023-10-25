import numpy as np

import pandas as pd

a1 = pd.DataFrame({

    'Дата': pd.Timestamp('20231025'),
    'Товар': ['яблоко', 'апельсин', 'яблоко', 'апельсин'],
    'Количество': np.random.randint(7,35,4)
}
)

b1 = pd.DataFrame(a1.groupby('Товар')['Количество'].sum())


def count_sum(df):
    return b1

print(count_sum(a1))

