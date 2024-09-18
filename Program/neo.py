import pandas as pd

# File ID from Google Drive link
file_id = '1CBB0uYz3yOz5tpCw_uaywDVCobek_1Je'

# Construct the URL for downloading
url = f"https://drive.google.com/uc?id={file_id}&export=download"

# Load the CSV file directly from the Google Drive link
df = pd.read_csv(url)

# Display the first few rows of the DataFrame
# print(df.head())

# for col in df.columns:
#     print(f"Columna: {col}, \nTipo de dato: {df[col].dtype} \n")


df.count()


# Limpieza de columnas que no nos sirven
#neo_id
df = df.drop('neo_id', axis=1)
#name
df = df.drop('name', axis=1)
#orbiting_body
df = df.drop('orbiting_body', axis=1)