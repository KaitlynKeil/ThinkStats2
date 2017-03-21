# Getting Treatment
###### by Kaitlyn Keil

###### March 20, 2017

In 1971, President Nixon grabbed the attention of the United States by declaring drug abuse "public enemy number one". Shortly later, the term "War on Drugs" shot into popularity. This idea, starting with the idea of preventing new addicts and the rehabilitating those who are addicted, has come to nearly 49% of the 208,000 people in federal prisions being there due to drug crimes. This isn't counting those in state prisons. I don't intend to start a debate on the prison politics of the US, however; that can be saved for another day. Instead, I'm intrigued by the rehabilitation part. More specifically, how many addicts get treatment? And out of these, how long do addicts typically go before they receive treatment?

The [National Survey on Drug Use and Health (NSDUH)](http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64) provides some of the data needed to approximate the answers to these questions. The most recent results from this annual survey were from 2014, which is what I used to look into this question. The Jupyter Notebook I used to analyze the data can be found [here](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/report2.ipynb).

The first question was a straightforward answer. Out of 42,131 respondents who reported having used drugs, 3,123 had received treatment, or roughly 7.4%.

The next step was to look at how long someone used drugs before they received treatment. Because those responding to the survey have not lived the full course of their lives and thus might still receive treatment in the future, I used Kaplan-Meier Estimation to approximate the hazard function, or the ratio of how many people at any given time unit receive treatment compared to those who do not. Once I found this, as can be seen in Figure 1, I used it to estimate the survival function (Figure 2).

![Full Hazard Function](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/fullTreatmentHF.png)

*Figure 1: The hazard function for all those who received treatment. The ratio is higher for lower numbers, with the exception of a spike around 50 years. The 50 year spike may be due to very few respondents who have been using drugs for 50 years, so even a few receiving treatment at this point cause the ratio to shoot upward. Otherwise, it seems to trend towards the more years someone has been using drugs, the less likely they are to get treatment.*

![Full Survival Curve](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/fullTreatmentSF.png)

*Figure 2: The survival curve for receiving treatment. As suggested by the decreasing hazard function ratios, it flattens out fairly quickly. Note that the y-axis spans from 91% to 100%, due to the low percentages of people who have received treatment.*

What are some of the factors that might influence the likelihood of receiving treatment? The first I decided to look into was income. NSDUH provides a variable which divides the population into 3 significant groups: those below the federal poverty line, those above the line and making up to twice as much, and those making more than twice the poverty line. Using these categories and the above estimation function again, I produced Figure 3.

![Divided Survival Curve](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/dividedTreatmentSF.png)

*Figure 3: survival curve for different income groups. While those making less than twice the poverty line follow a very similar trend whether they actually fall into a poverty level or not, those with high income never get past 5% receiving treatment. Note again the range of the y-axis.*

This plot suggests that the people with higher income are overall less likely to receive treatment.
