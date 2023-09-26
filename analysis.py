import pandas as pd
file_name = 'cfpb.xlsx'
cfpb_data = pd.read_excel(file_name, header = 8)

# Rename columns using the first row
cfpb_data.columns = cfpb_data.iloc[0]

# Drop the first row since it's now the header
cfpb_data = cfpb_data.drop(cfpb_data.index[0])

# Reset the index
cfpb_data.reset_index(drop=True, inplace=True)

# Display the first few rows with the new column names
print(cfpb_data.head())

#drop the row/entry with all missing values
cfpb_data.dropna(how='all', inplace=True)

# Check for duplicate rows
duplicate_rows = cfpb_data.duplicated().sum()

# Check for missing values in the dataset
missing_values = cfpb_data.isnull().sum()
cfpb_data_head = cfpb_data.head()
print(cfpb_data_head, duplicate_rows, missing_values.head(10))
