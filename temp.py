txt = "61e1, 81or"
txt2 = "602e"
x = txt.split(",")
x2 = txt2.split(",")
print(x[0])
print(x2[0])


print("divider")
x = txt.split(",")[0]
x2 = txt2.split(",")[0]
print(x)
print(x2)


txt = "61e1, 81or, 123k, 19ca"
x = txt.split(",", 1)
print(x)
print(x[0])

import pandas as pd

# Example dataframe
df = pd.DataFrame({
    'col': ['a,b,c', 'd,e,f', 'g,h,i']
})

# Split each string by the first comma and get the first element
df['col'] = df['col'].str.split(',', n=1, expand=False).str[0]

print(df)





# Example dataframe
df = pd.DataFrame({
    'col': ['a,b,c', 'd,e,f', 'g,h,i']
})

# Split the column into multiple columns
df_split = df['col'].str.split(',', expand=True)

print(df_split)

new_df = df_split[[0, 2]]
print(new_df)


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

filepath = os.path.join('files', 'one.txt')
request_path = os.path.join(BASE_DIR, filepath)
print(request_path, filepath, BASE_DIR)


CURR_DIR = os.getcwd()
print(CURR_DIR)
complete_path = os.path.join(CURR_DIR, "Oogabooga")
print(complete_path)