import pandas as pd

#import the merged data from all of the zipped files
claim_data = pd.read_pickle('merged_data.pkl')

path_classifier = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/classifier_output.csv"
classifier_data = pd.read_csv(path_classifier)

#merge the data on the shared claim id
merged = pd.merge(claim_data, classifier_data, on= 'claim_id')

#this is to get rid of the duplicated information in the merge
#without this, there would be extra 
# for index, row in merged.iterrows():
#     if row['part_x'] != row['part_y']:

#         merged.at[index, 'operation'] = None
#         merged.at[index, 'part_price'] = 0
#         merged.at[index, 'price'] = 0
#         merged.at[index, 'labour_amt'] = 0
#         merged.at[index, 'part_x'] = None

print('test')
print('test')

merged.to_pickle('ground_truth.pkl') 
#merged = pd.read_pickle('ground_truth.pkl')