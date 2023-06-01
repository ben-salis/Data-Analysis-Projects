# Cyclistic Historical Data
This data is provided by the Divvy bikeshare company, based in Chicago. The scenario surrounding the case study is fictional, and provided by the Google Data Analytics Professional Certificate program. Via this [license](https://ride.divvybikes.com/data-license-agreement), I am able to use Divvy's data for my own analysis. Going forward, Cyclistic will be the name used to refer to the stakeholder company.

## Introduction
Cyclistic has two types of customers that are classified as: **member** or **casual**. 

* Members pay for an annual membership to use Cyclistic bikes. 

* Casual customers pay for either single-ride or full-day passes to use Cyclistic bikes.

Stakeholders believe that members are more profitable than casual customers. As a result, there is an interest in converting casual customers into members. Analysts have been asked to investigate how the two types of customers differ, over the course of the past year. This historical analysis can be done with the data provided, concerning the interval **May 2022 - April 2023**. 

## Preparation
The raw data provided required cleaning. Each table was separated by month and the largest table contained more than 800,000 entries, each detailing information about a bike trip taken that month. Of the attributes given, it became clear that this analysis would only need the following:

|rideable_type|started_at|ended_at|member_casual|
|-------------|----------|--------|-------------|

The other columns were either incomplete or irrelevant to my goals. For instance, the entire column regarding the end station was NULL. With the sheer volume of data in each montly table, I believed I would benefit from downsizing. After this initial culling, I ran a query to check each month for any more NULL entries. I did not find any more empty entries. 

This check gave me confidence that I could move forward. 

## Process
Of the chosen parameters, there was more information that could be garnered. Through SQL, I was able to use the **started_at** and **ended_at** values to calculate the duration of the rides that customers took. I was also able to use the **started_at** value to calculate which weekday the trip was taken on. I was interested in what a weekly trend might look like in a given month. 

So, from these I introduced the **ride_length** and **day_of_week** attributes.

|rideable_type|started_at|ended_at|member_casual|ride_length|day_of_week|
|-------------|----------|--------|-------------|-----------|-----------|

It was here that I was able to consider a useful constraint that could be imposed on the data. Upon the introduction of **ride_length**, I found that there were a number of trips that lasted for less than a minute. To me, it seemed unlikely that these were full rides at all. I wondered if customers may have registered for a bike and changed their minds rather quickly. On that same vein, I found trips that lasted for longer than a day. While these didn't seem errant, I felt that it would be better to look at these separately. 

I imposed the condition that 1 < **ride_length** < 1440 (note: **ride_length** was defined in minutes). I then gathered a separate dataset for **ride_length** > 1440. Due to some lingering questions I had, I decided to keep each month's data seperate. 

## Analysis
Big Query and Google Sheets were instrumental in the analysis of this redefined dataset. As mentioned before, I saw fit to take a granular look at trends in each month. Through the COUNT function I could keep track of trips per customer-tyype. Through **ride_length** and **day_of_week** I was able to use the AVG function to find a the average ride length per day for a given month. 

Once these general calculations were made in Big Query, I combined the monthly tables in Sheets. The table was a bit too long for useful analysis, so I used a pivot table to make it wide. The visualizations were made in [Sheets](https://docs.google.com/spreadsheets/d/1CSMAeb5JT4J9uRJWp2pImGxAOl9dgU8vEK888TsJ43Q/edit?usp=sharing) as well. 
