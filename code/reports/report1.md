#Rich or Poor: To Whom does it Matter More?

Despite having more money than can be reasonably used in a lifetime, the most wealthy are usually portrayed as
vehement opposers of taxes. Some of the stories involve enough tax evasion and questionable business practices
that it seems we could replace the rich with dragons, curled on their hoard and ready to watch the rest of the 
world go down in fire, so long as they can keep their gold safe. But is this fair? After all, humans are 
notorious story-tellers. 

However, it turns out that those with higher incomes tend to report themselves as caring more about wealth than
the lower-income brackets. Given a 6-point scale, the mean for the 10th percentile of income came out as half a point
(specifically 0.49 points) closer to the side of wealth is important than the those in the 3rd percentile and below.
With a standard deviation of 1.3 points, this is more than a third (0.37) of a standard deviation.

We can look at the CDFs for the different income groups to visualize this difference, as can be seen in the following figure:

![Image of WealthCDF]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/wealthyCDFs.png)

As a note, the way this survey was posed, low numbers mean the person cares more about the given value. Thus, this figure
shows the gap between high and low income, with a median difference of an entire point.

This is in contrast to what the different income groups tend to think of other values. For example, when the same 
process is performed based on the value of equality, we get a much different figure:

![Image of EqualityCDF]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/equalityCDFs.png)

Not only is the mean response for all three groups lower, but the differences between groups are significantly reduced
as well, lending a hopeful note that maybe we do care about equality in the world more than material wealth.

In fact, with a sampling of the human values enquired about on this survey, we find that wealth is, in fact, the lowest
ranked across Europe, as we can see here, where the mean response for each value is bordered by its standard deviation
in answer:

![Image of allvaluesplot]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/allvaluesplot.png)

It should be noted, however, that these are self-reported values, and it feels better to say "Of course I care about
equality" than it does "Ah yes, money is my everything."

As a final note, there is significant variation between countries.

![Image of countriesValues]
(https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/reports/countrywealthplot.png)

When a similar mean/standard deviation plot was spread 
across the countries surveyed, the country that reported caring most about wealth (Hungary) was signficantly high than that
which cared least (France). So perhaps greed depends more on how you grew up than how much money you have... but that's a
different question all together.

###Methods

The code I used to generate these results is in [this IPython Notebook](https://github.com/KaitlynKeil/ThinkStats2/blob/master/code/report1.ipynb).  I used data from the 
[European Social Survey](http://www.europeansocialsurvey.org/download.html?file=ESS7e02_1&y=2014) (ESS) from 2014. 
This survey spanned across 21 countries, with face-to-face interviews conducted with newly selected, cross-sectional samples.
I primarily focused on the Human Values section. Here, questions were posed as:

>Now I will briefly describe some people. 
>Please listen to each description and tell me how much each person is or is not like you.

>It is important to her/him to be rich. She/he wants to have a lot of money and expensive things. 

>She/he thinks it is important that every person in the world should be treated equally. She/he believes everyone should have equal opportunities in
life. 

with the scale ranging from 1 (very much like me) to 6 (not at all like me).
