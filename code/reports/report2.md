# Getting Treatment
###### by Kaitlyn Keil

###### March 20, 2017

Alcohol is no small part of our culture. It features in our movies, our stories, our family gatherings, our nights out with friends. Most of the time, this moderate use doesn't really affect day-to-day life. However, out of all addictions, alcoholism is one of the most prominent and spoken of. Almost everyone knows someone whose life is affected by either their own alcohol addiction or that of a close acquaintance. Because of this, many different treatments have appeared to help those affected: 12 Step programs, residential programs, and intensive outpatient programs (IOPs) are just a few. Knowing how many options there were, and also knowing how difficult struggling with addiction can be, I began to wonder: how many people who struggle with alcohol dependency or abuse actually receive treatment? And, for those who do, what age do they tend to be?

The [National Survey on Drug Use and Health (NSDUH)](http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64) provides some of the data needed to approximate the answers to these questions. The most recent results from this annual survey were from 2014, which is what I used to look into this question. The Jupyter Notebook I used to analyze the data can be found [here](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/report2.ipynb).

To answer my first question (what percentage receive treatment), I took those who were recorded as having struggled with dependency or abuse in the past year. From these, I found the percentage who had received treatment. The definition of dependency in this context can be found [here](http://www.icpsr.umich.edu/icpsrweb/ICPSR/ssvd/studies/36361/datasets/0001/variables/DEPNDALC?q=DEPNDALC), and abuse [here](http://www.icpsr.umich.edu/icpsrweb/ICPSR/ssvd/studies/36361/datasets/0001/variables/ABUSEALC?q=ABUSEALC). In short, both have to do with whether the respondent admitted feeling their use was out of control and the effects were no longer what they desired.

Even with this amount of self-awareness, slightly less than 17% had received treatment at the time of the survey.

The next step was to look at how old the respondents were when they first received treatment. Using the data from those who had already received treatment to produce a survival curve (how long did the person live before treatment) as well as those who reported an alcohol problem in the past year (thus still need treatment) resulted in Figure 1 through Kaplan-Meier estimation. At over 80 years of age, more than 20% of people still have not received any sort of treatment for alcohol, despite an apparent need.

![Treatment SF](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/treatmentSF.png)

*Figure 1: The survival function of those who need or have received treatment.*

Looking at only those who had received treatment, I found that approximately 50% of people who have received treatment did so by age 25, with a fairly steep dropoff in the next several years, as seen in Figure 2.

![Full SF Function](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/fullAgeTXsf.png)

*Figure 2: The survival function for all those who received treatment. By age 25, half of those who reported treatment have been treated. 36% have been treated by age 21, and about 20% have been treated by age 18.*

What are some things that might lead to these people finding treatment, and what might minimize the age at which it happens? Income, it turns out, is likely not the answer. Dividing the respondents into those whose household income falls beneath the US Census [poverty line](http://www.irp.wisc.edu/faqs/faq1.htm), those who have an income of up to twice the poverty line, those above this, and college students, resulted survival curves that began and ended around the same percentages, as seen in Figure 3. In the middle, it appears that those with higher income (above twice the poverty line) tend to get treatment later in life.

![Divided Survival Curve](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/treatmentDividedSF.png)

*Figure 3: survival curve for different income groups. All the curves are very similar, with the exception of college students. This curve cuts off sharply at 22, as this is the upper limit for college student age.*

With these curves so similar, we have to turn towards other potential causes. Using logistical regression on whether or not someone has received treatment while controlling for respondent age, race, income, and gender, I examined what effect whether someone had driven under intoxication had. I found a pseudo R^2 value of 0.04 and a coefficient of 0.85, suggesting that those who have driven while intoxicated are more likely to receive treatment. Comparing this to the pseudo R^2 value and coefficient for income, (0.00017 and -0.0269 respectively, with the negative coefficient suggesting lower income families are more likely to receive treatment), intoxicated driving does seem to have more effect. Figure 4, however, suggests a concerning trend where those who have gotten DUIs are far less likely to undergo treatment. At age 80, nearly 50% will not have received treatment, compared to the 10% of those who did not drive under intoxication.

![DUI Survival Curve](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/treatmentDUI_SF.png)

*Figure 4: survival curve comparing those who have driven under intoxication with those who haven't.*

The age at which someone started drinking alcohol also may have some sort of effect on whether they have received treatment, which makes sense for the tendency towards low treatment ages. The pseudo R^2 value is approximately 0.07, and the coefficient is -0.18. While this isn't particularly steep, it does suggest some influence.

These results could suggest that an outside influence interferring is one of the primary causes of treatment, such as parents with a minor, or a judge for a DUI.

However, there are a few issues as well. The first is with the percentage. Unfortunately, only those reporting alcohol problems within the past year were recorded. This percentage, therefore, is likely higher, as those who have undergone treatment and overcome their dependency or abuse are not represented. Also not captured in the survival curves is anyone who had an alcohol problem, but overcame it without the assistance of treatment.

Despite these issues, it seems as though even our numerous methods of treatment aren't enough to capture all those who do need help with their addiction. Particularly if the best way to get someone to treatment is outside influence, perhaps we need more voices encouraging and taking the shame from needing help, rather than more options.
