import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.legend import _get_legend_handles_labels
import pickle

from data_processing import get_data_ready
_ , ground_truth_data = get_data_ready(True) #load the data from the other file

# path = f"/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/ground_truths.pkl"
# ground_truth_data = pd.read_pickle(path)

replace_vals = [[], [], [], [], [], [], [], [], [], []]
repair_vals = [[], [], [], [], [], [], [], [], [], []] 
none_vals = [[], [], [], [], [], [], [], [], [], []] 

parts_order = ['fbumper', 'bbumper', 'bldoor', 'brdoor','frdoor', 'fldoor', 'frwing', 'flwing', 'brwing', 'blwing']

#TODO there is some duplicate code between here and the other classifier analysis file. if i had more time, would combine into a big plotting file
for i in range(10):
    for val in range(int(len(ground_truth_data)/10)):
        #every 
        idx = 10*val + i

        ##this is to check which part of the dataset is being used
        test = (ground_truth_data.at[idx, 'set'] == 2)
        current = ground_truth_data.at[idx, 'operation']
        current_score = ground_truth_data.at[idx, 'urr_score']

        if current == 'replace' and test:
            replace_vals[i].append(current_score)
        elif current == 'repair'and test:
            repair_vals[i].append(current_score)
        elif test:
            none_vals[i].append(current_score)

save_data = [replace_vals[0], repair_vals[0], none_vals[0]]
with open("fbumper_full_array", "wb") as fp:   #Pickling
    pickle.dump(save_data, fp)

#when i was looking at a different part of data for analysis
# save_data = [replace_vals[7], repair_vals[7], none_vals[7]]
# with open("flwing_full_array", "wb") as fp:   #Pickling
#     pickle.dump(save_data, fp)

#plot all of the results
sq_num_plots = 3
fig, axs = plt.subplots(sq_num_plots,sq_num_plots)
fig.suptitle('All of the Components')
for i in range(sq_num_plots):
    for j in range(sq_num_plots):
        l = 3*i + j
        axs[i,j].set_title(f"Part: {parts_order[l]}", fontsize=10,loc='right', pad=-14)
        axs[i,j].hist([none_vals[l],repair_vals[l], replace_vals[l]], bins=50, label=['Fine','Repair','Replace'])
plt.xlabel('urr_score')
plt.legend( ['Fine','Repair', 'Replace'])
# plt.savefig("/Users/johngearig/Desktop/INTERVIEW PREP/tractable_ds_excercise_data/my_data/AllPartsSeperate.png", dpi= 300)
plt.show()
