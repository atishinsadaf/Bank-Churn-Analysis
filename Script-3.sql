SELECT 
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM churn), 2) AS churn_rate_pct
FROM churn
WHERE churn_label = 'Churned';

SELECT 
    geography,
    ROUND(SUM(CASE WHEN churn_label = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM churn
GROUP BY geography;

SELECT 
    gender,
    ROUND(SUM(CASE WHEN churn_label = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM churn
GROUP BY gender;

SELECT
	churn_label,
	avg(balance) as churn_vs_retained
	from churn
	group by churn_label;

SELECT
	numofproducts,
	ROUND(SUM(CASE WHEN churn_label = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM churn
GROUP BY numofproducts;
	
SELECT
	hascrcard,
	ROUND(SUM(CASE WHEN churn_label = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM churn
GROUP BY hascrcard;

SELECT
	isactivemember,
	ROUND(SUM(CASE WHEN churn_label = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM churn
GROUP BY isactivemember;

SELECT
	churn_label,
	avg(tenure) as churn_rate_pct
	from churn
	group by churn_label;