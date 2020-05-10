---------------------------------------------------DATA SET--------------------------------------------------------------

The Data_Set is a collection of Real time accelerometer values taken a mobile.
The accelerometer readings of various activites are noted and used as a dataset.
The dataset is passed through a  Machine Learning Algorithm to train a module
The module is then used for predictions of future values.

---------------------------------------------------Firebase_key------------------------------------------------------------
This is the authentication key used to access the values from Firebase.


----------------------------------------------Sedentary_final_model------------------------------------------------------

This is the final model used to create the application.
This uses Relative motion to detect movements.

-------------------------------------------------Sedentary_model.sav------------------------------------------------------

This contains the trained model which predicts the activity based on the input parameters given.


---------------------------------------------------------Test.py----------------------------------------------------------------

This script gets the data from the firebased and passes it to the trained model to get predictions.

---------------------------------------------------------Train.py----------------------------------------------------------------

This Script Uses dataset to train a Machine Learning model that uses DecisionTreeClassifier for classification.





 