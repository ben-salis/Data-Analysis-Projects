# COVID-19 Daily Counts of Cases, Hospitalizations, and Deaths
This is historical data retrieved from [NYC Open Data](https://opendata.cityofnewyork.us). Specifically, the counts were provided
by the Department of Health and Mental Hygiene (DOHMH). This dataset is the product of diligent reporting efforts on their part and provides
objective numbers from a time of tension and confusion. They have provided a record of confirmed positive cases, hospitilizations, and deaths as a result of
COVID-19 in NYC boroughs. Any interested parties may find the raw data and DOHMH supporting documents [here](https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3).

This dataset ranges from 02/29/2020 to 05/01/2023. I will likely seek more recent data soon, but for now this will do. The page has not 
been updated since 05/10/2023, but there are sources for current counts. 
## Introduction
My initial goal with this dataset was to design a dashboard. I'd already found shapefiles for the NYC boroughs, and felt that
a map of the counts could describe the data very well. Which boroughs had more COVID-19 cases? Which years had the largest hospitalizations? 
Which months had the least COVID related deaths? My SQL queries answered these questions, but visualizations are always useful. 

Trends within a time series are always interesting, since there are so many factors influencing a given result. Whether it is
seasonal, external, random, or some combination of the three, trends can be attributed to something. 

## Preparation 

DOHMH provided a lot of data for each day. I imagine that a lot of these attributes were necessary for monitoring the health
of NYC during various pivotal moments. Since I had a very simple task, I was able cull the dataset by a quite a lot. 

The raw data contained columns for cases, hospitalizations, and deaths for each borough. This alone meant that there were 15 columns
with the information I required. In addition to this, There were 7-day averages for each attribute, as well as probable counts. 
I couldn't find documentation on the method they were using to calculate a "PROBABLE_CASE_COUNT," but there was information on the
recorded "PROBABLE_DEATH_COUNT." Until I decided what to do with either one, I decided to stick to confirmed events. 

By the end of the culling I would have the 15 attributes I needed, in addition to the date_of_interest field. 

Per the User Guide provided by the DOHMH: 

* date_of_interest: Date of COVID-19 diagnosis (i.e., date of specimen collection), hospital admission, or death.

* {Borough}_case_count: Count of patients tested who were confirmed to be COVID-19 cases on date_of _interest in the {Borough}.

* {Borough}_hospitalized_count: Count of COVID-19 patients who were hospitalized on date_of_interest in the {Borough}.

* {Borough}_death_count: Count of deaths occurring among confirmed COVID-19 cases on date_of_interest in the {Borough}.
  
**Where Borough is in (BX, QN, MN, SI, BK)**

This new dataset would have the information I needed. After some consideration, I decided to restructure the table. My shapefiles would
need location fields to act as a shared key, and the current form was not great for grouping with SQL. 

[Here](https://github.com/ben-salis/Data-Analysis-Projects/blob/main/NYC%20COVID-19%20and%20MTA%20Joint%20Analysis%20/DOHMH%20COVID-19%20Counts%20NYC/restructuring-covid19-count.ipynb) is the full code
for my restructuring. With a few nested loops and keyword searching, I was able to create a dataframe with the form I wanted. Below is a generalized sample. I used a borough's abbreviation and name in place of 'Borough' and 'Borough_prefix':

```py
for elem in cov_header:
    for row in range(len(cov_count)):
        date = cov_count['date_of_interest'][row]
        val = cov_count[elem][row]
        if elem.startswith('Borough_prefix') == True: #could use "in" operator.
            borough = 'Borough'
            if 'CASE' in elem:
                category = 'Cases'
                pre_df += [(date,borough,category,val)]
            elif 'DEATH' in elem:
                category = 'Deaths'
                pre_df += [(date,borough,category,val)]
            elif 'HOSPITALIZED' in elem:
                category = 'Hospitalized'
                pre_df += [(date,borough,category,val)]
```

My dataframe took the following form: 
|Date|Location|Classification|Count|
|----|--------|--------------|-----|

It was a longer dataset, but filtering and grouping was far easier in this form. 

## Process / Visualization
Aggregation was done in Tableau for the most part. I included the shapefiles with TableauPrep. Then I went about considering what 
an average person might be interested in when looking for a dashboard for COVID-19. I'm pleased with how it turned out, and it
allows people to answer borough specific questions with ease. Feel free to click around. 
The dashboard can be found [here](https://public.tableau.com/app/profile/ben.salis/viz/NYCCOVID-19Dashboard_16956794400990/NYCCOVID-19Dashboard).

A snapshot: 

![NYC COVID-19 Dashboard](https://github.com/ben-salis/Data-Analysis-Projects/assets/134881005/d595e529-1c23-4457-9962-7588c5af63dc)


## Analysis
I found that the boroughs with more people tended to have more cases, deaths, and hospitalizations. In total, Brooklyn held 
30% of the COVID-19 cases in NYC. Queens came close with 27%, which is expected considering its relative size. In accordance to this
trend, Staten Island had the least cases at 7%. 

Suprisingly, the worst year for cases wasn't the first one. NYC saw more cases in 2022 than in 2020. This is due to the Omicron strain,
which affected even vaccinated individuals. 

Still, there were many deaths in the first year, totalling 20,324 across all boroughs. Thankfully, this decreased as response and
protocols improved. 

## Conclusion
This was a very sobering endeavor, but insightful nonetheless. My idea for a timeline vizualization stemmed from my work with this dataset. I believe I can use the probable counts on the dashboard, but I will think on it. 
