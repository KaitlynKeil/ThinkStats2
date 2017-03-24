# Getting Treatment
###### by Kaitlyn Keil

###### March 20, 2017

In 1971, President Nixon grabbed the attention of the United States by declaring drug abuse "public enemy number one". Shortly later, the term "War on Drugs" shot into popularity. This idea, starting with the idea of preventing new addicts and the rehabilitating those who are addicted, has come to nearly 49% of the 208,000 people in federal prisions being there due to drug crimes. This isn't counting those in state prisons. I don't intend to start a debate on the prison politics of the US, however; that can be saved for another day. Nor is today focused on discussing the prevention of new addicts, which spawns programs such as D.A.R.E. and other "Just say no!" mantras. Instead, I'm intrigued by the rehabilitation part. More specifically, how many addicts get treatment? And out of these, how long do addicts typically go before they receive treatment?

The [National Survey on Drug Use and Health (NSDUH)](http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64) provides some of the data needed to approximate the answers to these questions. The most recent results from this annual survey were from 2014, which is what I used to look into this question. The Jupyter Notebook I used to analyze the data can be found [here](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/report2.ipynb).

The first question was a straightforward answer. Out of 42,131 respondents who reported having used drugs, 3,123 had received treatment, or roughly 7.4%.

The next step was to look at how long someone used drugs before they received treatment. Because those responding to the survey have not lived the full course of their lives and thus might still receive treatment in the future, I used Kaplan-Meier Estimation to approximate the hazard function, or the ratio of how many people at any given time unit receive treatment compared to those who do not. Once I found this, as can be seen in Figure 1, I used it to estimate the survival function (Figure 2).

![Full Hazard Function](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/fullTreatmentHF.png)

*Figure 1: The hazard function for all those who received treatment. The ratio seems to have a slight downward trend until it passes 30, at which point the numbers spike upwards. This may be due to fewer respondents who have been using drugs for this many years, so even a few receiving treatment at this point cause the ratio to shoot upward. Otherwise, it seems to trend towards the more years someone has been using drugs, the less likely they are to get treatment.*

![Full Survival Curve](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/fullTreatmentSF.png)

*Figure 2: The survival curve for receiving treatment. Past 57 years, the curve is completely flat as very, very few people receive treatment. Up to that point, the survival curve appears fairly linear.*

While at first glance, this might seem to contradict the 7.4% who have received treatment due to the nearly 25% chance of being treated after 60 years, this isn't actually the case. As there are fewer people who have used drugs for more than 60 years, everyone who is treated at that point carries more weight. 

What are some of the factors that might influence the likelihood of receiving treatment? The first I decided to look into was income. NSDUH provides a variable which divides the population into 4 significant groups: those below the federal poverty line, those above the line and making up to twice as much, those making more than twice the poverty line, and college students living in dorms. Using these categories and the above estimation function again, I produced Figure 3.

![Divided Survival Curve](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/dividedTreatmentSF.png)

*Figure 3: survival curve for different income groups. While those making less than twice the poverty line follow a very similar trend whether they actually fall into a poverty level or not, those with high income never get past 5% receiving treatment. Note again the range of the y-axis. The college student curve cuts off early, as they can, at most, have used drugs for 22 years.*

This plot suggests that the people with higher income are overall less likely to receive treatment, as their chances of making it to a certain year before receiving treatment is, at times, more than 10%. However, when I used logistical regression to see what effect income level had on whether or not a respondent had received treatment, I found that while the coefficient was negative (lower numbers and thus lower income mean it was more likely for the respondant to have been through treatment), the pseudo-R^2 value was low, around 3.3^-4. Scanning through other variables that might have an impact, I found that whether the respondant had driven under the influence of alcohol and how young they were when they began drinking both had a more significant effect. Driving under the influence had an R^2 value of 0.02081, and the age someone started drinking (broken into age categories) weighed in with an R^2 of 0.1123. Based on this, it doesn't seem like it matters as much whether or not you have money in whether you get treatment or not; what matters appears to be the choices around what you do with the money you have.

There are a few potential pitfalls with this analysis. One of the first is the assumption that, should someone be using drugs of any sort, they require treatment. This is not necessarily the case, and this analysis does not look into the extent or severity of any individual's drug use. There are a few other assumptions in this space (the age someone started using cigarettes daily or had five alcoholic beverages on a single occasion stands in as the start of drug use for these substances, lacking better variables). There are also a significant number of missing values in the dataset variables I was working with. Most of these were resampled from the data I did have available, in order not to change the ratio of those in treatment compared to those untreated too drastically.
