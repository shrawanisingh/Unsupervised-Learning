# Unsupervised-Learning
## • DOMAIN: Automobile
• CONTEXT: The data concerns city-cycle fuel consumption in miles per gallon to be predicted in terms of 3 multivalued discrete and 5 
continuous attributes.
## • DATA DESCRIPTION: 
• PROJECT OBJECTIVE: To understand K-means Clustering by applying on the Car Dataset to segment the cars into various categories.

• STEPS:

1. Data Understanding & Exploration:
A. Read ‘Car name.csv’ as a DataFrame and assign it to a variable.
B. Read ‘Car-Attributes.json as a DataFrame and assign it to a variable. 
C. Merge both the DataFrames together to form a single DataFrame 
D. Print 5 point summary of the numerical features and share insights. 

2. Data Preparation & Analysis: 
A. Check and print feature-wise percentage of missing values present in the data and impute with the best suitable approach. 
B. Check for duplicate values in the data and impute with the best suitable approach. 
C. Plot a pairplot for all features.
D. Visualize a scatterplot for ‘wt’ and ‘disp’. Datapoints should be distinguishable by ‘cyl’.
E. Share insights for Q2.d. 
F. Visualize a scatterplot for ‘wt’ and ’mpg’. Datapoints should be distinguishable by ‘cyl’.
G. Share insights for Q2.f. 
H. Check for unexpected values in all the features and datapoints with such values. 

3. Clustering: 
A. Apply K-Means clustering for 2 to 10 clusters. 
B. Plot a visual and find elbow point.
C. On the above visual, highlight which are the possible Elbow points. 
D. Train a K-means clustering model once again on the optimal number of clusters. 
E. Add a new feature in the DataFrame which will have labels based upon cluster value. 
F. Plot a visual and color the datapoints based upon clusters. 
G. Pass a new DataPoint and predict which cluster it belongs to. 
