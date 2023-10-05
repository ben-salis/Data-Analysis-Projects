#Joining MTA Ridership table to NYC COVID-19 monthly totals table
WITH 
	ridership_reformat AS (
		SELECT
			DATE_FORMAT(Month, '%Y-%m') AS mta_date,
        		`Subway Ridership`, `Bus Ridership`
		FROM 
			MTA_monthly.ridership
	)
    
SELECT 
	`year_month`, monthly_total AS 'Total COVID-19 Cases',
	`Subway Ridership`, `Bus Ridership`
FROM 
	COVID19_long.nyc_monthly_totals AS cov
    
INNER JOIN
	ridership_reformat AS re
	ON re.mta_date = cov.year_month #shared key. 
	#Only want pandemic dates from MTA ridership table. 

WHERE
	Classification = "Cases"
