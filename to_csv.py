import pandas as pd
df_operation = pd.read_csv('/Users/a10.12/operation_data.csv')
df_operation.dropna(axis=0,how='any',subset=['Identifier'],inplace=True)
df_operation.dropna(axis=0,how='any',thresh=3,inplace=True)
df_operation.fillna({'Date':9999},inplace=True)
df_gp = df_operation.groupby("Place")
df_date = df_operation.groupby(df_operation['Date'].map(lambda d:str(d)[0:2]+'00')).count()
def to_2(d):
    return str(d)[0:2]
# df_date['Title'].count()
df_date.to_csv('export_result.csv')