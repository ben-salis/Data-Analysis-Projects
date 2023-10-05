USE COVID19_long;
# Need to reformat Date attribute to match MTA data for future join. 
CREATE TABLE nyc_monthly_totals AS (
	SELECT
		DATE_FORMAT(`Date`, '%Y-%m') AS `year_month`, 
		Classification, # Cases are my primary curiosity, but we'll keep all three for now.
		SUM(Count) AS monthly_total
	FROM
		longform

	GROUP BY `year_month`, Classification
	ORDER BY `year_month` ASC
)