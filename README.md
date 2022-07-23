# Unsupervised-Learning
## • DOMAIN: Automobile
• CONTEXT: The data concerns city-cycle fuel consumption in miles per gallon to be predicted in terms of 3 multivalued discrete and 5 
continuous attributes.
## • DATA DESCRIPTION: 
• PROJECT OBJECTIVE: To understand K-means Clustering by applying on the Car Dataset to segment the cars into various categories.

• STEPS AND TASK [30 Marks]:

1. Data Understanding & Exploration: [5 Marks]
A. Read ‘Car name.csv’ as a DataFrame and assign it to a variable. [1 Mark]
B. Read ‘Car-Attributes.json as a DataFrame and assign it to a variable. [1 Mark]
C. Merge both the DataFrames together to form a single DataFrame [2 Mark]
D. Print 5 point summary of the numerical features and share insights. [1 Marks]
2. Data Preparation & Analysis: [10 Marks] 
A. Check and print feature-wise percentage of missing values present in the data and impute with the best suitable approach. [2 Mark]
B. Check for duplicate values in the data and impute with the best suitable approach. [1 Mark]
C. Plot a pairplot for all features. [1 Marks]
D. Visualize a scatterplot for ‘wt’ and ‘disp’. Datapoints should be distinguishable by ‘cyl’. [1 Marks]
E. Share insights for Q2.d. [1 Marks]
F. Visualize a scatterplot for ‘wt’ and ’mpg’. Datapoints should be distinguishable by ‘cyl’. [1 Marks]
G. Share insights for Q2.f. [1 Marks]
H. Check for unexpected values in all the features and datapoints with such values. [2 Marks]
[Hint: ‘?’ is present in ‘hp’]
3. Clustering: [15 Marks] 
A. Apply K-Means clustering for 2 to 10 clusters. [3 Marks]
B. Plot a visual and find elbow point. [2 Marks]
C. On the above visual, highlight which are the possible Elbow points. [1 Marks]
D. Train a K-means clustering model once again on the optimal number of clusters. [3 Marks]
E. Add a new feature in the DataFrame which will have labels based upon cluster value. [2 Marks]
F. Plot a visual and color the datapoints based upon clusters. [2 Marks]
G. Pass a new DataPoint and predict which cluster it belongs to. [2 Marks]
