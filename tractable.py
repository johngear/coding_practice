import pandas as pd
import numpy as np
import csv
import gzip


#where i want to save the .pkl file so I don't have to rerun this every time
path_to_claims_pickle = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/sorted_merged_claim_data.pkl"


#this is what the labels ought to be
ideal_labels = ['claim_id', 'make', 'model', 'year', 'poi', 'line_num', 'part', 'operation', 'part_price', 'labour_amt']
# dtypes = [int, str, str, int, str, int, str, str, int, int]

#This is to handle all of the 40 different files that I need to unzip and read
claim_path = []
len_input_data = 40 #this is the number of different folders that need to be unzipped
for i in range(len_input_data):
    #make this a nice number with a leading zero so I can easily access any of these files
    i_str = str(i).zfill(2)
    claim_path.append(f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/metadata/part-000{i_str}.csv.gz")

#saving this into a big array and then saving it is supposed to be better practice than saving into a dataframe and appending... 
full_claim_data = []
for path_singular in claim_path:
    with gzip.open(path_singular, mode = 'rt') as csvfile:
        data = list(csv.reader(csvfile))
        current_labels = data[0] #this should be the first row of the file with the names of the data

        #this there is a divergence in file naming 
        if current_labels != ideal_labels:
            print(f"There is an issue with the naming of the first line. It is labeled as {current_labels}")
        full_claim_data += data[1:] #append all of the information except for the top line

#Now, we want this in Pandas for their merge functionality and whatnot
df_full_claim_data = pd.DataFrame(full_claim_data, columns=ideal_labels)
df_full_claim_data = df_full_claim_data.astype({'claim_id': int})
df_full_claim_data = df_full_claim_data.sort_values(by=['claim_id', 'line_num']) #first sorts by the claim ID, then the line number

#save to a file so I don't have to do this every time
df_full_claim_data.to_pickle(path_to_claims_pickle)

# df_full_claim_data = pd.read_pickle(path_to_claims_pickle)
print(f"\n\nSaved sorted merged claim data to: {path_to_claims_pickle}\n\n")






# #helper function to understand the format of the data
# def print_sample_data(path_input):
#     #taken from stack overflow article on how to preview a .gz file
#     data = pd.read_csv(path_input, nrows=100, compression='gzip', error_bad_lines=False)
#     return data
