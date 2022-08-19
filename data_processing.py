import pandas as pd
import numpy as np
import csv
import gzip

############# RUNTIME INFORMATION ############# 
# The numpy version:           1.19.2.
# The pandas version:          1.1.3.
# The scikit-learn version:    1.1.2.
# The python version:          3.8.5 (default, Sep  4 2020, 02:22:02) 
# [Clang 10.0.0 ].
###############################################


#where i want to save the .pkl file so I don't have to rerun this every time
path_to_claims_pickle = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/sorted_merged_claim_data.pkl"
path_to_ground_truth_pickle = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/ground_truths.pkl"

#where the classifier csv is
path_to_classifier_csv = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/classifier_output.csv"

#path to all of the claims are located in the function #TODO figure out an easy way around this lol


def get_data_ready(load_from_pkl):
    #this function will return the claim data, and the merged classifier data in a pandas dataframe
    #when calling if you have the choice to load the data from CSVs as it was given, or load from pickle files after processing

    #enter this function if you are loading the information for the first time. 
    if load_from_pkl == False:
        print('pulling data from the files')


        #This is to handle all of the 40 different files that I need to unzip and read
        claim_path = []
        len_input_data = 40 #this is the number of different folders that need to be unzipped
        for i in range(len_input_data):
            #make this a nice number with a leading zero so I can easily access any of these files
            i_str = str(i).zfill(2)
            claim_path.append(f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/metadata/part-000{i_str}.csv.gz")


        #this is what the labels ought to be
        ideal_labels = ['claim_id', 'make', 'model', 'year', 'poi', 'line_num', 'part', 'operation', 'part_price', 'labour_amt']
        # dtypes = [int, str, str, int, str, int, str, str, int, int]

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

        print(f"\n\nSaved sorted merged claim data to: {path_to_claims_pickle}\n\n")

        ########################################################
        # Now we want to deal with the classifier information
        ########################################################

        classifier_data = pd.read_csv(path_to_classifier_csv)

        #merge these with the correct Claim ID and Part number
        df_ground_truths = df_full_claim_data.merge(classifier_data, on=['claim_id', 'part'], how = 'right')

        #again, save this, so we only have to run it once. 
        df_ground_truths.to_pickle(path_to_ground_truth_pickle) 
        print(f"\n\nSaved ground truth data to: {path_to_ground_truth_pickle}\n\n")

        return df_full_claim_data, df_ground_truths

    #enter this function is you already have ran it once, and just want to load it from a pkl file
    elif load_from_pkl == True:
        # print('entered load from pkl')
        df_full_claim_data = pd.read_pickle(path_to_claims_pickle)
        df_ground_truths = pd.read_pickle(path_to_ground_truth_pickle)

        return df_full_claim_data, df_ground_truths

#returns all of the information about one specific claim number
def get_ground_truths(truths_df, claim_id_number):
    index = claim_id_number*10
    # ground_truths._get_value(index)
    return truths_df[index:index+10]

#change this function if you want to run it for the first time
_ , ground_truths = get_data_ready(True)
print('\nloaded data from data_processing.py\n')