/* This query is adapted from my BigQuery code.
Parameters day_of_week and ride_length are created 
here. 
- Ben Salis */
USE Cyclistic_trips;
WITH -- needed temp table to generate multiple parameters that require aggregate functions
  avg_mem_ride AS (
    SELECT
      day_of_week, ROUND(AVG(ride_length),2) as avg_ridem
    FROM
      (SELECT
        member_casual, DAYOFWEEK(started_at) AS day_of_week,
        TIMESTAMPDIFF(MINUTE, started_at, ended_at) AS ride_length 
        FROM
          `Trips`.`01_2023-divvy-tripdata`
      ) as a
    WHERE 
		member_casual = "member" AND 
		ride_length > 0 AND ride_length < 1440 
        -- Only interested in rides that last 1 day or less
        
    GROUP BY day_of_week),

  avg_cas_ride AS (
    SELECT
      day_of_week, ROUND(AVG(ride_length),2) as avg_ridec
    FROM
      (SELECT
        member_casual, DAYOFWEEK(started_at) AS day_of_week,
        TIMESTAMPDIFF(MINUTE,started_at,ended_at) AS ride_length
        FROM
          `Trips`.`01_2023-divvy-tripdata`
      ) as b
    WHERE 
		member_casual = "casual" AND 
		ride_length > 0 AND ride_length < 1440
        
    GROUP BY day_of_week),

  mem_count AS (
    SELECT
      day_of_week, COUNT(member_casual) AS m_count 
    FROM
      (SELECT
        member_casual, DAYOFWEEK(started_at) AS day_of_week,
        TIMESTAMPDIFF(MINUTE, started_at, ended_at) AS ride_length
        FROM
          `Trips`.`01_2023-divvy-tripdata`
      ) as c
    WHERE 
		member_casual = "member" AND
		ride_length > 0 AND ride_length < 1440
        
    GROUP BY day_of_week
  ),
  cas_count AS (
    SELECT
      day_of_week, COUNT(member_casual) AS c_count
    FROM
      (SELECT
        member_casual, DAYOFWEEK(started_at) AS day_of_week,
        TIMESTAMPDIFF(MINUTE, started_at, ended_at) AS ride_length
        FROM
          `Trips`.`01_2023-divvy-tripdata`
      ) as d

    WHERE 
		member_casual = "casual" AND
		ride_length > 0 AND ride_length < 1440
        
    GROUP BY day_of_week
  )


SELECT
  DISTINCT(t.day_of_week), t.month, mc.m_count AS member_count, 
  am.avg_ridem AS avg_member_ride, cc.c_count AS casual_count,
  ac.avg_ridec AS avg_casual_ride
FROM 
  (SELECT
      DAYOFWEEK(started_at) AS day_of_week, 
      DATE_FORMAT(started_at, "%b %Y") AS month
   FROM 
      `Trips`.`01_2023-divvy-tripdata`
  ) AS t

INNER JOIN 
  avg_mem_ride AS am
  ON am.day_of_week = t.day_of_week
INNER JOIN
  avg_cas_ride AS ac
  ON ac.day_of_week = t.day_of_week
INNER JOIN
  mem_count AS mc
  ON mc.day_of_week = t.day_of_week
INNER JOIN
  cas_count as cc
  ON cc.day_of_week = t.day_of_week

ORDER BY day_of_week ASC

/* I considered using UNION to join the tables 
for each month together, but wanted to see what
I could do in Sheets with a pivot table. 
- Ben Salis */

