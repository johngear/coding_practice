import pandas as pd 

path_classifier = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/classifier_output.csv"
path_input = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/metadata/part-00002.csv.gz"


#these will both be in the dataframes
input_data = pd.read_csv(path_input, compression='gzip', error_bad_lines=False)

classifier_data = pd.read_csv(path_classifier, nrows = 10000)

merge_big = pd.merge(input_data, classifier_data, on= 'claim_id')
merged = pd.merge(input_data, classifier_data, on= ['claim_id','part'])

print(merged)

for index, row in merge_big.iterrows():
    if row['part_x'] != row['part_y']:

        merge_big.at[index, 'operation'] = None
        merge_big.at[index, 'part_price'] = 0
        merge_big.at[index, 'price'] = 0
        merge_big.at[index, 'labour_amt'] = 0
        merge_big.at[index, 'part_x'] = None
              
    elif row['part_x'] != row['part_y']:
        #idk why i just want to see if this passes at all
        pass


print(merge_big)