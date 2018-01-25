import pandas as pd

s = pd.Series([7, 2, 0, 3, 4, 2, 5, 0, 3, 4])

(s.groupby(s.eq(0).cumsum().mask(s.eq(0))).cumcount() + 1).mask(s.eq(0), 0).tolist()
