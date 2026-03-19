# Week 3 Python Assessment - Section 1: MCQ Answers
# IIT Gandhinagar | PG Diploma in AI-ML & Agentic AI Engineering

"""
Q1.  Median (28 min)
     - When there are extreme outliers (late-night orders at 90-110 min), 
       the mean gets pulled way up. Median stays unaffected by those extremes.

Q2.  7.4 kg
     - IQR = Q3 - Q1 = 3.8 - 1.4 = 2.4
     - Upper fence = Q3 + 1.5 * IQR = 3.8 + 3.6 = 7.4

Q3.  10.0
     - total = 80, count = 8, mean = 80/8 = 10.0

Q4.  200.0
     - mean = 30, squared deviations = 400+100+0+100+400 = 1000
     - population variance = 1000/5 = 200.0

Q5.  Poisson distribution
     - Models count of independent events at a constant average rate (lambda = 7/day)

Q6.  H0: mu_new = 3.4  vs  H1: mu_new > 3.4
     - H0 always represents "no change" (status quo)
     - H1 is the claim being tested (one-tailed, increase only)

Q7.  App B has highly polarised ratings
     - High std dev (1.6 on a 1-5 scale) means many 1s and 5s, very divided opinions

Q8.  Type I error
     - H0 was actually true (no improvement), but team rejected it = false positive

Q9.  Sample means form approximately normal distribution
     - This is exactly what Central Limit Theorem says, regardless of original shape

Q10. p (0.02) < alpha (0.05) -> reject H0, result is statistically significant

Q11. df[(df['exp_years'] > 2) & (df['comm_score'] > 7)]
     - Must use & not 'and', and each condition needs its own parentheses

Q12. Disagree - p (0.08) > alpha (0.05), fail to reject H0
     - 1.9% difference might just be due to random chance

Q13. SELECT * FROM orders WHERE city = 'Bengaluru' AND amount > 5000;
     - String values need single quotes, WHERE for row-level filtering

Q14. df.iloc[1:4]
     - iloc is position-based; [1:4] gives positions 1, 2, 3 (4 is exclusive)

Q15. Right-skewed - mean (18.4) > median (11.2) > mode (9)
     - A few high-return sellers are pulling the mean up

Q16. 100.0
     - Delhi orders are [120, 80], avg = 200/2 = 100.0 (groupby computes per group)

Q17. Non-numeric strings like Rs.399 and N/A prevent pandas from inferring float
     - Entire column defaults to object dtype

Q18. 280 and 400
     - COUNT(email) ignores NULLs -> 400-120 = 280
     - COUNT(*) counts all rows -> 400

Q19. GROUP BY category HAVING AVG(order_value) > 3000 AND COUNT(*) >= 50
     - HAVING filters AFTER aggregation; WHERE cannot use aggregate functions

Q20. LEFT JOIN
     - Keeps all employees; unassigned ones get NULL for dept_name

Q21. df['temperature_C'].ffill()
     - Forward fill uses last known value, most clinically appropriate for vitals

Q22. 'Gold'
     - Done orders: c10(400+800=1200) + c30(1100) = 2300 for Gold
     - Silver (c20) only has order #2 (900) since order #5 is cancelled
     - Gold total > Silver total -> Gold is first after sort descending

Q23. Interval narrows
     - Larger sample -> smaller standard error (SE = sigma/sqrt(n)) -> tighter CI

Q24. Type II error risk increases
     - Very strict alpha means we miss more real effects (false negatives go up)

Q25. P(alert|fraud) * P(fraud) / [P(alert|fraud) * P(fraud) + P(alert|genuine) * P(genuine)]
     - Bayes' theorem formula

Q26. Seller 10 IS an outlier
     - Upper fence = 6 + 1.5*2 = 9; 18 > 9 -> flagged
     - Median (4.5) is better representation than mean (5.9)

Q27. 36.4 hours, vendor IS flagged
     - x = mu + z * sigma = 24 + 3.1 * 4 = 36.4
     - z = 3.1 > threshold of 2.5

Q28. Right-skewed
     - mode (42k) < median (51k) < mean (68k) -> classic positive skew pattern

Q29. DROP TABLE temp_staging;
     - Removes table + all data + structure permanently

Q30. how='left'
     - Keeps all orders; guest orders get NaN for customer columns

Q31. ALTER TABLE accounts RENAME COLUMN acc_no TO account_number;

Q32. Statements I, II, and IV only
     - Statement III is wrong: statistical significance alone doesn't mean immediate 100% rollout

Q33. Run ROLLBACK to undo all changes in the current transaction
     - Session still open, no COMMIT issued yet -> ROLLBACK is safe
"""

print("MCQ Answers documented above in comments.")
print("Refer to the docstring for all 33 answers with explanations.")
