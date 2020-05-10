import pickle
a=input("accelerometer_X:")
b=input("accelerometer_Y:")
c=input("accelerometer_:")
x=[[a,b,c]]
logmodel=pickle.load(open('sedentary_model.sav','rb'))
prediction = logmodel.predict(x)
print(prediction)