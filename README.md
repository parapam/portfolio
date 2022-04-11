<p>
  <a href="https://www.linkedin.com/in/brigita-pli%C5%A1ka-044a64158/">
    <img src="https://i.stack.imgur.com/gVE0j.png"> LinkedIn
  </a> &nbsp; 
</p>
<p>
  <a href="https://medium.com/@brigitaplika">Medium profile</a>
</p>

## <a href="https://github.com/parapam/portfolio/tree/main/projects/ChurnPrediction" title="Churn prediction">Project #1: Churn prediction</a>

Project goal - build a classification model for the Telco telecommunications company predicting whether customers will churn.

- Analyze data to see which variables have the most impact on churn. For categorical values chi-squared test was used to evaluate whether the feature is correlated with the churn;
- Using kernel density estimation (KDE) check numerical variables' impact on churn;
- Remove non-correlated variables and build a logistic regression model to predict churn rate;

#logistic-regression #exploratory-data-analysis #chi-squared #cramers-v #kde

## <a href="https://github.com/parapam/portfolio/tree/main/projects/LifeExpectancy" title="Life expectancy prediction">Project #2: Life expectancy prediction</a>

Project goal - build a linear model predicting life expectancy.

- Deal with missing values based on their correlation with each other and the dependent variable. Investigate why some of the features are missing (e.g. HepatitisB data is missing for countries that *"have very low endemicity and consider hepatitis B to be a limited public health problem, thus not justifying additional expense", [WHO](https://www.euro.who.int/en/health-topics/disease-prevention/vaccines-and-immunization/vaccine-preventable-diseases/hepatitis-b)*);
- Check for multicollinearity by looking at the correlation matrix;
- Compare how different models (classical, Lasso, and Ridge linear regression) perform with different hyperparameters;

#linear-regression #ridge #lasso #grid-search #feature-engineering #hyperparameters-tuning

## Theory

To better learn some of the topics I've created separate notebooks for the theory, formulas, and experiment with data as it is important to know what's going on under the hood of commonly used methods.

- <a href="https://github.com/parapam/portfolio/blob/main/theoretical_notebooks/correlation_and_cov.ipynb">Correlation and covariance</a>
- <a href="https://github.com/parapam/portfolio/blob/main/theoretical_notebooks/hypothesis-testing.ipynb">Hypothesis testing</a>
- <a href="https://github.com/parapam/portfolio/blob/main/theoretical_notebooks/linear_regression.ipynb">Linear regression</a>
- <a href="https://github.com/parapam/portfolio/blob/main/theoretical_notebooks/PCA.ipynb">PCA</a>
