df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# make a new column with zeros at zeros and nans elsewhere
df = df.assign(idx_from_0=df.loc[df.X==0])

nul = df['idx_from_0'].isnull()
df.assign(idx_from_0=nul.groupby((nul.diff() == 1).cumsum()).cumsum())
