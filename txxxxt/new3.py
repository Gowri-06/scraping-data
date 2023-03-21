import json
import pandas as pd

import pandas as pd

# Read in both Excel files
df_5 = pd.read_excel('./txxxxt/ProducthuntProduct.xlsx')
df_6 = pd.read_excel('Producthuntwebsitelink.xlsx')

# Merge the two dataframes based on the 'id' column
merged_df = pd.merge(df_5, df_6[['Id', 'Website']], on='Id', how='left')

# Save the merged dataframe to a new Excel file
merged_df.to_excel('merged_file.xlsx', index=False)
