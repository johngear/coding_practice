import pandas as pd
import matplotlib.pyplot as plt
import random

############# RUNTIME INFORMATION ############# 
# The numpy version:           1.19.2.
# The pandas version:          1.1.3.
# The scikit-learn version:    0.24.1.
# The python version:          3.8.5 (default, Sep  4 2020, 02:22:02) 
# [Clang 10.0.0 ].
###############################################

from data_processing import get_data_ready
_ , ground_truth_data = get_data_ready(True) #load the data from the other file

# path = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/ground_truths.pkl"
# ground_truth_data = pd.read_pickle(path)


specific_part = False #change this to loop over the entire range of parts or just one part

##loop through every value
replace_vals = []
repair_vals = []
none_vals = []

#this is if you just want to look at Front Bumper for example
if specific_part:
    for val in range(int(len(ground_truth_data)/10)):
        #every 
        
        current = ground_truth_data.at[10*val, 'operation']
        current_score = ground_truth_data.at[10*val, 'urr_score']
        if current == 'replace':
            replace_vals.append(current_score)
        elif current == 'repair':
            repair_vals.append(current_score)
        else:
            none_vals.append(current_score)

#and this will combine all of the Urr_Scores
else:
    for val in range(len(ground_truth_data)):
        #every 

        #this is to see if it's in the test data set
        test = (ground_truth_data.at[val, 'set'] == 2)

        current = ground_truth_data.at[val, 'operation']
        current_score = ground_truth_data.at[val, 'urr_score']
        if current == 'replace' and test:
            replace_vals.append(current_score)
        elif current == 'repair' and test:
            repair_vals.append(current_score)
        elif test:
            none_vals.append(current_score)

fig, ax = plt.subplots()
ax.hist([none_vals, repair_vals, replace_vals], bins=50, alpha=1, label = ['Fine', 'Repair', 'Replace'])


plt.legend(loc='upper right')
plt.ylabel("# of Instances")
plt.xlabel("URR_Score from Classifier")
plt.title("All Parts, Test portion of Dataset")
plt.show()
# plt.savefig("/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/AllParts.png", dpi= 300)