
import pandas as p  #importing pandas module

data1=p.read_csv('C:/Users/HP/Downloads/test.csv') #reading a kaggle test dataset using pandas modulle.
data2=p.read_csv('C:/Users/HP/Downloads/train.csv') #reading a kaggle train dataset using pandas modu
data3=p.read_csv('C:/Users/HP/Downloads/gender_submission.csv')  #reading a kaggle gender_submission dataset using pandas modu

print("DataSet1\n\n",data1) # Displaying the Entire datasset1
print("\n\nDataSet2\n\n",data2) # Displaying the Entire datasset2
print("\n\nDataSet3\n\n",data3) # Displaying the Entire datasset3

print("\n\nFirst Five rows in dataset1\n\n",data1.head()) #head func will display only the first five records in the csv file.
print("\n\nLast Five rows in dataset1\n\n",data1.tail()) #tail func will display only the last five records in the csv file.
print("\n\nFirst Five rows in dataset2\n\n",data2.head()) #head func will display only the first five records in the csv file.
print("\n\nLast Five rows in dataset2\n\n",data2.tail()) #tail func will display only the last five records in the csv file.
print("\n\nFirst Five rows in dataset3\n\n",data3.head()) #head func will display only the first five records in the csv file.
print("\n\nLast Five rows in dataset3\n\n",data3.tail()) #tail func will display only the last five records in the csv file.

#Our task is to find the mean, median, mode and other basic statistics.
print("\n\nDescription of dataset1\n\n",data1.describe()) # It displays the description of the dataset like count, mean value, standard deviation, min and max value. And various quatiles from 25% to 75%.
print("\n\nDescription of dataset2\n\n",data2.describe()) #It displays the description of the dataset like count, mean value, standard deviation, min and max value. And various quatiles from 25% to 75%
print("\n\nDescription of dataset3\n\n",data3.describe())#It displays the description of the dataset like count, mean value, standard deviation, min and max value. And various quatiles from 25% to 75%

print("\n\nColumns in DataSet1\n\n",data1.columns) # It returns all the columns name in the dataset1.
print("\n\nColumns in Dataset2\n\n",data2.columns) # It returns all the columns name in the dataset2.
print("\n\nColumns in Dataset3\n\n",data3.columns) # It returns all the columns name in the dataset3.

'''Let's find the mean, median, mode of column passangerId in all the datasets'''
print("\n\nMean of passangerId in Dataset1\n\n",data1['PassengerId'].mean()) #Finding mean value of passengerId column
print("\n\nMean of passangerId in Dataset2\n\n",data2['PassengerId'].mean()) #Finding mean value of passengerId column
print("\n\nMean of passangerId in Dataset3\n\n",data3['PassengerId'].mean()) #Finding mean value of passengerId column

print("\n\nMedian of passangerId in Dataset1\n\n",data1['PassengerId'].median()) #Finding median value of passengerId column
print("\n\nMedian of passangerId in Dataset2\n\n",data2['PassengerId'].median()) #Finding median value of passengerId column
print("\n\nMedian of passangerId in Dataset3\n\n",data3['PassengerId'].median()) #Finding median value of passengerId column

print("\n\nMode of passangerId in Dataset1\n\n",data1['PassengerId'].mode()) #Finding mode value of passengerId column
print("\n\nMode of passangerId in Dataset2\n\n",data2['PassengerId'].mode()) #Finding mode value of passengerId column
print("\n\nMode of passangerId in Dataset3\n\n",data3['PassengerId'].mode()) #Finding mode value of passengerId column

print("\n\nDisplay Mean Value of Each columns\n\n",data1.mean(numeric_only=True)) # It returns the mean value of each columns which are numeric datatype
print("\n\nDisplay Mean Value of Each columns\n\n",data2.mean(numeric_only=True)) # It returns the mean value of each columns which are numeric datatype
print("\n\nDisplay Mean Value of Each columns\n\n",data3.mean(numeric_only=True)) # It returns the mean value of each columns which are numeric datatype

print("\n\nDisplay Median Value of Each columns\n\n",data1.median(numeric_only=True)) # It returns the median value of each columns which are numeric datatype
print("\n\nDisplay Median Value of Each columns\n\n",data2.median(numeric_only=True)) # It returns the median value of each columns which are numeric datatype
print("\n\nDisplay Median Value of Each columns\n\n",data3.median(numeric_only=True)) # It returns the median value of each columns which are numeric datatype

print("\n\nDisplay Mode Value of Each columns\n\n",data1.mode(numeric_only=True)) # It returns the mode value of each columns which are numeric datatype
print("\n\nDisplay Mode Value of Each columns\n\n",data2.mode(numeric_only=True)) # It returns the mode value of each columns which are numeric datatype
print("\n\nDisplay Mode Value of Each columns\n\n",data3.mode(numeric_only=True)) # It returns the mode value of each columns which are numeric datatype

