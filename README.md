# LinkedIn a Predictor for City Unemployment Rate?

Welcome to my project! In this project I try and connect LinkedIn User Profile features (education count, experience count, number of followers, etc.) and use this data to try and try to see if there is some correlation to a given city's unemployment rate, and if so, how well we can predict such a thing. 

Datasets acquired: 

-crawled LinkedIn (crawler provided) through two-phase approach of crawling LinkedIn URLs on Google (implicit reliance on PageRank) and finally crawling LinkedIn profiles and parsing HTML data to capture several features.

-Used BLS (government) dataset for city unemployment rates.

Goal is essentially try and predict unemployment rates based on LinkedIn profiles

## Contributions

All three phases of this project were solely by Nikhil Gowda

## Findings
Ultimately, I used four different classification algorithms for Phase 3. A neural network, catboost (gradient boosting on decision trees), linear regression, and a regression tree. The main dependency is most likely catboost which requires something outside of sklearn


```bash
pip3 install --user catboost
```
Result details are found in associated Python Notebook but rewritten here:


### Hypotheses 1:

For this hypothesis, I have tried to classify two types of profiles, profiles that belong to Riverside/Los Angeles and profiles that belong to Irvine/San Francisco. In other words, the goal is to figure out if certain features are applicable to predicting whether this particular person is from a city with either a low or high unemployment rate.

Using a neural net first on small data, it seems that we get a barely better than chance outcome in prediction. This probably corresponds to lacking feature differentiation. People in both types of cities have similar experience, education, or follower count. And of course all of this interacts with Google's PageRank algorithm that gets the top hit sites based on valuable incoming links. This means the profiles we see are the best of each given city.

Using CatBoost, we come across a much better algorithm with about 65% accuracy despite the confounding variable of PageRank. This means there may actually be some differentiating factors between both city types.


### Hypotheses 2:

For this hypotheses, we use our confounding variable knowledge, page rank, and try to predict instead if we can simply predict unemployment rate as a regression problem. Using all 5 cities, we try to capture the error rates of each mis-labeled profile from a given city defined by the sum of difference of predicted and actual.

Our first algorithm is our classic linear regression which does better than our regression tree in terms of variance. This may be due to our decision tree finding the best prediction to be closes to the mean of all predictions.
