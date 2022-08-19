import pandas as pd 
import pickle
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import matplotlib.pyplot as plt

#TODO this could go into the data_processing file. could use a bit of reworking but this is fine
with open("fbumper_full_array", "rb") as fp:   # Unpickling
   data = pickle.load(fp)

# with open("flwing_full_array", "rb") as fp:   # Unpickling
#    data = pickle.load(fp)

#data[0] = replace; data[1] = repair; data[1] = none

#do some silly changing of data so that SKlearn likes it. this can likely be done in another way
X = data[0] + data[1] + data[2]
y = [0 for _ in range(len(data[0]))] + [1 for _ in range(len(data[1]))] + [2 for _ in range(len(data[2]))] 

Xnew = np.array(X)
ynew = np.array(y)

Xnew_er= Xnew[~np.isnan(Xnew)]
ynew_er = ynew[np.squeeze(~np.isnan(Xnew))]

Xnew_er = np.expand_dims(Xnew_er, axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(Xnew_er, ynew_er, stratify=ynew_er,random_state=1)

lda = LinearDiscriminantAnalysis().fit(X_train,y_train)
qda = QuadraticDiscriminantAnalysis().fit(X_train,y_train)

###ADD NEURAL NETWORK STUFF
from sklearn.neural_network import MLPClassifier
#i tried adding more layers and changing parameters here but there isn't much that changes
nn = MLPClassifier(hidden_layer_sizes=(100,), alpha=1, max_iter=5000).fit(X_train,y_train)

###NAIVE BAYES
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB().fit(X_train,y_train)

###SVM
from sklearn.svm import SVC
svm = SVC(kernel="linear", C=0.025).fit(X_train,y_train)

print("QDA score:   ", qda.score(X_test,y_test))
print("LDA score:   ", lda.score(X_test,y_test))
print("NN score:    ", nn.score(X_test,y_test))
print("NB score:    ", nb.score(X_test,y_test))
print("SVM score:   ", svm.score(X_test,y_test))


######TEST ACCURACY WITH A HIGHER THRESHOLD

#this is super ugly im tired lol. not sure if sklearn has something do this

#only give a class if the output is above the threshold (to reduce the number of misclassifieds)
threshold = 0.75

test_data = X_test
correct = y_test
correct_num, incorrect_num = 0,0
# print("len", len(test_data))
for (test_data_point, ground_truth) in zip(test_data, correct):
    classification = -1
    [outs] = qda.predict_proba([test_data_point])

    anything = np.argwhere(outs>threshold)
    if anything.size > 0:
        [[classification]]= np.argwhere(outs>threshold)

    if classification == -1:
        #nothing happens here it never reached the threshold
        pass
    elif classification == ground_truth:
        #correctly identified
        correct_num +=1 
    elif classification != ground_truth:
        #this is wrong
        incorrect_num +=1
    else:
        print('idk if this should b in here LOL')

print(f"\n\n{correct_num+incorrect_num} classified out of {len(test_data)}")
print(f"\n\nAccuracy with threshold {threshold}:        ", correct_num/(correct_num+incorrect_num), "\n\n")

#if you want to recreate the plot that I had on here previously...
plot = True
if plot == True:
    #OK Now I will create a plot of the behavior of the QDA

    probs = [] # [Preplace, Prepair, Pnone]
    x_axis = [x/1000 for x in range(1000)]

    for i in x_axis:
        probs.append((qda.predict_proba([[i]])[0] ))


    probs_np = np.array(probs)
    plt.plot(x_axis, probs_np[:,2], label = 'fine')
    plt.plot(x_axis, probs_np[:,1], label = 'repair')
    plt.plot(x_axis, probs_np[:,0], label = 'replace')
    plt.xlabel('URR_Score')
    plt.ylabel('Probability of Category')
    plt.title('Front Left Bumper')
    plt.legend()
    plt.show()