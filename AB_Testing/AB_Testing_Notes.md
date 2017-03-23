# Notes on A/B Testing (Udacity)
## Course Link
On [Udacity](https://classroom.udacity.com/courses/ud257/lessons/4018018619/concepts/40043986980923).

## Introduction
- A/B testing is good for testing out new features of products
- A/B test is done in a short time.
- A/B gives very quantitative data.
- Is not good for testing new experience
- Does not tell what you are missing
- Examples: ranking algorithms, backend optimizing (latencies)
- Other techniques to complement A/B testing


## History
- Comes from agriculture
- Clinical trial is also A/B test (control group)
- Online A/B test study: lots of data (large numbers of user), but low resolution (do not know much about each user)

## Case study
- A website wants to increase number of customers who explore their online courses. Customer funnel (fewer and fewer customers going downstream)
- Have a hypothesis. e.g., change the color of a button will increase the customer who exolore the courses
- Have a metric. e.g., total number of courses completed may take too long. *CTR* (click through rate, # clicks/ # pageviews) is a better metric than total number of cliks. A even more reasonable metric is *CTP* (click through probability, # unique visitors who click / # unique visitors)

>> *CTR* vs *CTP*: rate measures the usability of a button (how often users can click the button, and probability measure the impact (how many goes to the next level)

- Repeated measurement would lead to *binomial distribution* of number of clicks (click or no click with a probability $p$). $\mu = p$, stdev $\sigma = \sqrt{\frac{p(1-p)}{n}}$. 2 types of outcome, independent events, identical distribution. 
-Not binomial: Draws cards from a finite deck; Clicks of search results page: correlated; Whether a customer buys goods in a week: highly correlated
- Confident interval. If $N\cdot \hat{p} > 5$ and $N\cdot (1-\hat{p}) > 5$, it can be reasonably approximated by Gaussian distribution.
- margin of error: $m = z \sqrt{ (\hat p (1-\hat p )/N)}$, where $z$ is the z-score of the confidence interval. 1.96 is the z-score of 95% confidence interval of the z-distribution (standard Gaussian distribution), i.e., 1.96$\sigma$ contains 2.5% of the tail on either end. 
- For example, if $\hat p = x/N =100/1000 = 0.1$, then $m = 1.96 * \sqrt{(0.1*0.9/1000)} = 0.019$, so the 95% confidence interval will be 0.081 to 0.119. So it would be really surprising to see numbers larger than 119 in the next repetition.
- Another example, X=300, N=2000, 99% confidence interval would be: 0.15 +/- m = 2.58* (0.15*0.85/2000)^0.5 = 0.021, so 0.129 to 0.171
- Hypothesis testing (or, Inference) is a quantitatively way to establish how likely it is that the results occurred by chance. *Null Hypothesis (Baseline)* vs *Alternative Hypothesis*.
- Null hypothesis: p(results due to chance): $P_{exp} = P_{cont}$, or $P_{exp} - P_{cont} = 0$, represented as $H_0$. Alternative hypothesis $H_A$, i.e., $P_{exp}-P_{cont}\ne 0 $.
- Workflow: compute $P_{cont}$ and $P_{exp}$, and calcualte $P(P_{cont} - P_{exp}|H_0)$. If this probability is small enough, we can reject our null hypothesis if p < 0.05. The cutoff 0.05 is also called $\alpha$.
- If you're going to launch the experiment for a statistically significant positive change, and otherwise not, then you don't need to distinguish between a negative result and no result, so a _one-tailed test_ is good enough. If you want to learn the direction of the difference, then a _two-tailed test_ is necessary.






































	