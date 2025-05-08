from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

#C Load the diabetes dataset
iris_X , iris_y = datasets.load_iris(return_X_y=True)
# Split train : test = 8:2
X_train , X_test , y_train , y_test = train_test_split (
iris_X , iris_y ,
test_size =0.2 ,
random_state =42)

#B Define model
dt_classifier = DecisionTreeClassifier ()

#A Train
dt_classifier . fit ( X_train , y_train )

#D Preidct and evaluate
y_pred = dt_classifier . predict ( X_test )
accuracy_score ( y_test , y_pred )