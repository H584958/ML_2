We chose the excercise TMDB Box Office Prediction. The task were to make and train a model, thats going to predict the revenue of the movie. This were the columns in the dataset: 

 0   id                     3000 non-null   int64  
 1   belongs_to_collection  604 non-null    object 
 2   budget                 3000 non-null   int64  
 3   genres                 2993 non-null   object 
 4   homepage               946 non-null    object 
 5   imdb_id                3000 non-null   object 
 6   original_language      3000 non-null   object 
 7   original_title         3000 non-null   object 
 8   overview               2992 non-null   object 
 9   popularity             3000 non-null   float64
 10  poster_path            2999 non-null   object 
 11  production_companies   2844 non-null   object 
 12  production_countries   2945 non-null   object 
 13  release_date           3000 non-null   object 
 14  runtime                2998 non-null   float64
 15  spoken_languages       2980 non-null   object 
 16  status                 3000 non-null   object 
 17  tagline                2403 non-null   object 
 18  title                  3000 non-null   object 
 19  Keywords               2724 non-null   object 
 20  cast                   2987 non-null   object 
 21  crew                   2984 non-null   object 
 22  revenue                3000 non-null   int64  

The sets had a lot of objects, so we needed to fix this in a good way. We checked ifobject is not null, if so give value true, else false. We did this to "belongs_to_collection", "homepage", "original_language" (english). We also took the number of people in cast and crew, and made it to an int.

We tried using PyCaret, but didnt get it to work, so we dropped it entirely. 

We tried using different diffent models, K-nearest neighbors, Stochastic gradient descent, logastic regression, and ended up with random forest regressor. 