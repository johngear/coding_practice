import pandas as pd

in_path = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/sorted_merged_claim_data.pkl"

out_path = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/ground_truths.pkl"
#where the classifier csv is
path_classifier = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/classifier_output.csv"

sorted_merged_data = pd.read_pickle(in_path)
# sliced_sorted_merged_data = sorted_merged_data[['claim_id', 'make', 'model', 'year', 'poi']]

classifier_data = pd.read_csv(path_classifier)

# his merged list is the ground truth for all of the repairs and replacements needed. 
# But i need to add in all of the urr_scores with the for the other parts
# merged_repair_replace = pd.merge(sorted_merged_data, classifier_data, on= ['claim_id', 'part'])

ground_truths = sorted_merged_data.merge(classifier_data, on=['claim_id', 'part'], how = 'right')

ground_truths.to_pickle(out_path) 

#this will keep the part, and URR_scrore from becoming the same thing 
# this is causing DUPLICATEs where there are more than 10 for the same claim number. hmmm
# test = pd.merge(sliced_sorted_merged_data, classifier_data, on=['claim_id'])

print('test')



##OK this is good.


def get_ground_truths(claim_id_number):
    index = claim_id_number*10
    # ground_truths._get_value(index)
    print(ground_truths[index:index+10])

get_ground_truths(0)
get_ground_truths(100)
get_ground_truths(989)


print('pass')