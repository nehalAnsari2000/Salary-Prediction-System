import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os            #for checking directory
from sklearn.model_selection import train_test_split  #Used to split data set in 2 parts 1 is test and 2nd is trainig
from sklearn.linear_model import LinearRegression   # Used to creat ML model i. e. Regression Line 
from sklearn.metrics import r2_score    # to calculate r^2 value to check performance of model
def welcom():
    print("\n\n                    **** WELCOME TO SALARY PREDICTION SYSTEM ****\n\n")
    print("Press ENTER key to proceed\n")
    input()

def checkcsv():
    csv_files=[]
    cur_dir=os.getcwd()   #This fn will give the current directory 
    content_list=os.listdir(cur_dir)  # this fn is used to fetch all files from the directory which is passed in arg
    for x in content_list:
        if x.split('.')[-1]=='csv':
            csv_files.append(x)
    if len(csv_files)==0:
        return 'No csv file in the directory'
    else:
        return csv_files

def display_and_select_csv(csv_files):
    i=0
    for file_name in csv_files:
        print(i,'----->',file_name)
        i+=1
    return csv_files[int(input("\nSelect file to create ML model : "))]

def graph(X_train,Y_train,regressionObject,X_test,Y_test,Y_pred):
    plt.scatter(X_train,Y_train,color='red',label='training data')
    plt.plot(X_train,regressionObject.predict(X_train),color='blue',label='Best Fit')
    plt.scatter(X_test,Y_test,color='green',label='Test data')
    plt.scatter(X_test,Y_pred,color='Black',label='Pred test data')
    plt.title("Salary Vs Experience")
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
    
def main():
    welcom()
    try:
        csv_files=checkcsv()  #csv_files will contain the list of file names present in directory after fn call
        if csv_files=='No csv file in the directory':
            raise FileNotFoundError('No csv filr in the directory')
        csv_file=display_and_select_csv(csv_files)
        print(csv_file,' is selected..\n')
        print("Reading csv file...\n")
        print("Creating data set... \n")
        dataset=pd.read_csv(csv_file)    #read() ffn read data of csv file 
        print("Data set is created\n")
        X=dataset.iloc[:,:-1].values     #fn to fetch data column wise or row wise
        Y=dataset.iloc[:,-1].values
        s=float(input("\nEnter test data size (Between 0 and 1) : "))     # i.e.  0.1 for 10%
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=s)  # It will return 4 values 
        print("\nModel creation in progress...\n")
        regressionObject=LinearRegression()
        regressionObject.fit(X_train,Y_train)
        print("Model is created\n")
        print("\nPress ENTER key to predict test data in trained model\n")
        input()
        Y_pred=regressionObject.predict(X_test)
        i=0
        print(X_test,  '---->',Y_test,'  ---->',Y_pred)
        while i<len(X_test):
            print(X_test[i],'---->',Y_test[i],'---->',Y_pred[i])
            i+=1
        input("\nPress ENTER key to see above result in graphical format \n")
        graph(X_train,Y_train,regressionObject,X_test,Y_test,Y_pred)
        r2=r2_score(Y_test,Y_pred)
        print("\n * Our model is %2.2f%% is acuurate...\n"%(r2*100))
        print("\n\n      **** NOW YOU CAN PREDICT SALARY OF AN EMPLOYEE USING OUR MODEL *****\n")
        input("Press ENTER key to proceed\n")
        print("\nEnter experience in years of the candidates, seprated by comma : ")
        exp=[float(e) for e in input().split(',')]
        ex=[]
        input("\nPress ENTER key to show prediction in graphical method \n")
        for x in exp:
            ex.append([x])
        experience=np.array(ex)
        salaries=regressionObject.predict(experience)
        plt.scatter(experience,salaries,color='black')
        plt.xlabel("Years of experience")
        plt.ylabel("Salaries")
        plt.show()

        d=pd.DataFrame({'Experience':exp,'Salaries':salaries})
        print(d)
        print()
        print("                     **THANK YOU **")
        
    except FileNotFoundError:
        print('No csv file in the directory')
        input("Press ENTER key to exit ")
        exit()
    
if __name__=="__main__":
    main()
    input()











    
