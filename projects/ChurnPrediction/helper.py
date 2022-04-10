# Helper functions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import scipy.stats as ss

class ChurnHelper(object):

    def __init__(self, df):
        self.df = df
        self.churn = df[df.Churn=='Yes']
        self.no_chur = df[df.Churn=='No']
        self.figsize = (12,5)

    def plot_kde(self, field):
        plt.figure(figsize=self.figsize)
        sns.kdeplot(self.churn[field], label = 'Yes', shade=True).legend()
        sns.kdeplot(self.no_chur[field], label = 'No', shade=True).legend()
        
    def plot_pie_and_count(self, field):
        fig, axs = plt.subplots(ncols=2, figsize=self.figsize)
        fig.subplots_adjust(wspace = 0.7)
        self.df[field].value_counts().plot.pie(autopct = '%.1f%%', ax=axs[0])
        sns.countplot(x=field, hue='Churn', data=self.df, ax=axs[1])
        print(self.get_group_percentage(field))
        
    def get_group_percentage(self, field):
        return self.df.groupby(field)['Churn'].value_counts(normalize=True)

    def get_p_for_chi_sq(self, field, value_to_exclude = ''):
        if (value_to_exclude == ''):
            contigency = pd.crosstab(self.df.Churn, self.df[field])
        else:
            contigency = pd.crosstab(
                self.df.Churn[self.df[field] != value_to_exclude], 
                self.df[self.df[field] != value_to_exclude][field]
            )
        c, p, dof, expected = chi2_contingency(contigency)
        return p

    # from https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9
    def cramers_v(self, x, y):
        confusion_matrix = pd.crosstab(x,y)
        chi2 = chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2/n
        r,k = confusion_matrix.shape
        phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
        rcorr = r-((r-1)**2)/(n-1)
        kcorr = k-((k-1)**2)/(n-1)
        return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))