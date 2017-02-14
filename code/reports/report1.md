#Rich or Poor: To Whom does it Matter More?
######by Kaitlyn Keil

######February 12, 2017

Despite having more money than can be reasonably used in a lifetime, the most wealthy are usually portrayed as
vehement opposers of taxes. Some of the stories involve enough tax evasion and questionable business practices
that it seems we could replace the rich with dragons, curled on their hoard and ready to watch the rest of the 
world go down in fire, so long as they can keep their gold safe. But is this fair? After all, humans are 
notorious story-tellers. 

So then, we had to ask: do the rich actually care more about wealth? And what affect does income have on other
human values, such as equality, creativity, security, and experiences?

###Methods

To answer these queries, I used the code that can be found in [this IPython Notebook](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/report1.ipynb).  The data from the 
[European Social Survey](http://www.europeansocialsurvey.org/download.html?file=ESS7e02_1&y=2014) (ESS) from 2014. 
This survey spanned across 21 countries, with face-to-face interviews conducted with newly selected, cross-sectional samples.
I primarily focused on the Human Values section. Here, questions were posed as:

>Now I will briefly describe some people. 
>Please listen to each description and tell me how much each person is or is not like you.

>It is important to her/him to be rich. She/he wants to have a lot of money and expensive things. 

>She/he thinks it is important that every person in the world should be treated equally. She/he believes everyone should
have equal opportunities in life. 

with the scale ranging from 1 (very much like me) to 6 (not at all like me). After filtering out the responses
from everyone who refused to answer, was unsure, or had a value not in the range of 1-6, I used the entire dataset across
all the European countries surveyed. At first, I broke them up according to income bracket. If they fell into
the 10th percentile (top 10% of income), they became 'wealthy'. If they fell in the 3rd percentile or less (30% and below),
I classified them as 'low income'. The rest fell into the general category of 'other' or 'medium' income.

I also eventually broke them up according to country, in order to do a quick, surface analysis of the different countries.

To visualize the data, I chose to use CDFs (cumulative distribution functions) to easily see the medians and percentiles.
However, given the 6-point scale, this initially returned blocky step functions which were difficult to interpret at a 
glance and not representative of those who may have felt themselves at a 3.5 rather than a 4. To account for this, I jittered
the data when producing the CDFs with a range of 0.5, smoothing out the curves.

I also made a few plots which are represented by the mean and a range showing the standard deviation to either side. This
lets us compare different values (creativity to equality, for example) in another fashion.

###Results

With these methods, I found that those with higher incomes tend to report themselves as caring more about wealth than
the lower-income brackets. Given a 6-point scale, the mean for the 10th percentile of income came out as half a point
(specifically 0.49 points) closer to the side of wealth is important than the those in the 3rd percentile and below.
With a standard deviation of 1.3 points, this is more than a third (0.37) of a standard deviation. With a Cohen Effect Size
falling right between small (generally 0.2) and medium (0.5), this is not an entirely discountable difference.

We can look at the CDFs for the different income groups to visualize this difference, as can be seen in the following figure:

![Image of WealthCDF]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/wealthyCDFs.png)

With the way this survey was posed, low numbers mean the person cares more about the given value. Thus, this figure
shows the tendency for the wealthy to respond with a lower number (a median of 4, or 'a little like me') than the low-income group
(a median of 5, 'not like me') gap between high and low income, with a median difference of an entire point. The others, or 
middle-income group, sit between the two values, as might be expected. This does suggest a significant difference between the 
income brackets.

And it's not just that the wealthy are more passionate in general. For example, when asked about equality, we get a much different
figure, where any difference between the groups is nominal at best, and both mean and median are virtually identical across
 (about 2 for both):

![Image of EqualityCDF]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/equalityCDFs.png)

Not only is the mean response for all three groups lower, but the differences between groups are significantly reduced
as well, lending a hopeful note that maybe we do care about equality in the world more than material wealth.

In fact, with a sampling of the human values enquired about on this survey, we find that wealth is, in fact, the lowest
ranked across Europe, as we can see here, where the mean response for each value is bordered by its standard deviation. The
standard response deviation seems to stay within approximately 1 and 1.5, but the means for all (except, of course, wealth) are
below 3, or 'like me'.

![Image of allvaluesplot]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/allvaluesplot.png)

It should be noted, however, that these are self-reported values, and it feels better to say "Of course I care about
equality" than it does "Ah yes, money is my everything." Unfortunately, there isn't a clear way to measure how strong
this bias is, one way or another, so we'll have to hope that the respondees were as honest with themselves as they 
could be.

As a final note, there is significant variation between countries.

![Image of countriesValues]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/countrywealthplot.png)

When a similar mean/standard deviation plot was spread across the countries surveyed, the country that reported caring 
most about wealth (Hungary) was signficantly high than that which cared least (France). So perhaps greed depends more 
on how you grew up than how much money you have... but that's a different question all together.
