# TMDB Box Office

We chose the excercise TMDB Box Office Prediction. The task were to make and train a model, thats going to predict the revenue of the movie. 


The sets had a lot of objects, so we needed to fix this in a good way. We checked ifobject is not null, if so give value true, else false. We did this to "belongs_to_collection", "homepage", "original_language" (english). We also took the number of people in cast and crew, and made it to an int.

We tried using PyCaret, but didnt get it to work, so we dropped it entirely. 

We tried using different diffent models, K-nearest neighbors, Stochastic gradient descent, logastic regression, and ended up with random forest regressor.

We used the joblib library to export our model, and then we deployed with Flask. 
