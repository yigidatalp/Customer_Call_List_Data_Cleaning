# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:50:21 2023

@author: Yigitalp
"""

import pandas as pd

df = pd.read_excel('Customer Call List.xlsx')

# Drop duplicates
df = df.drop_duplicates()


# Drop not useful columns
df = df.drop(columns='Not_Useful_Column')


# Clean Last_Name
"""
df['Last_Name'] = df['Last_Name'].str.lstrip('/') # /White
df['Last_Name'] = df['Last_Name'].str.lstrip() # Winger
df['Last_Name'] = df['Last_Name'].str.lstrip('...') # ...Potter
df['Last_Name'] = df['Last_Name'].str.rstrip('_') # Flenderson_
"""
df['Last_Name'] = df['Last_Name'].str.strip(
    '/ ._')  # space for white space in Winger


# Clean Phone_Number
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '')

# iterator functions (more practical than a for loop)
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(
    lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')


# Clean Address
df[['Street Address', 'State', 'Zip_Code']
   ] = df['Address'].str.split(',', 2, expand=True)
df = df.drop(columns='Address')


# Clean Paying Customer
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')


# Clean Do_Not_Contact
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].fillna('')
df['Do_Not_Contact'] = df['Do_Not_Contact'].replace('', 'N')


# Replace N/a with ''
df = df.replace('N/a', '')


# Replace NaN with ''
df = df.replace('NaN', '')


# Fill nan/None
df = df.fillna('')


# Detect callable customers
# df = df.dropna(subset = 'Phone_Number', inplace = True) also works as an alternative method.
df = df[df['Phone_Number'] != '']
df = df[df['Do_Not_Contact'] != 'Y']

# Reset index
df = df.reset_index(drop=True)
