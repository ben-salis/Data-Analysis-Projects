# Snapshot Pricelist

This dataset was provided by a user on Kaggle for training use. It can be found [here](https://www.kaggle.com/datasets/shivam2503/diamonds). 
The data should be considered a snapshot of the collective traits of a group of diamonds, with no time component being presented. 
Emphasis will be put on correlation and any trends seen therein. 

## Introduction 

While the context provided on the Kaggle data card is sufficient for analysis purposes, further research revealed some inconsistencies with
certain definitions. That being said, upon preparing the data for analysis I found very little cleaning or sorting to do. Despite this, 
I was still interested in what the data might reveal, and settled on an explorative analysis with a focus on visualizations. Spreadsheets proved to be satisfactory.
I believe I could use this data to design a predictive model in the future and will likely do this fairly soon. 

My tentative goal was to identify majority and minority diamonds with regard to color. Did prices support the respective scarcity or surplus? 

Barring this, I hoped to design a dashboard that would enable someone to gather pricing information on a specific diamond of their choosing.
The final product can be found on [Tableau](https://public.tableau.com/views/DiamondShoppingDashboard/Dashboard?:language=en-US&:display_count=n&:origin=viz_share_link). Feel free to click around to filter the dashboard down. 

## Definitions

*Table* : Term for the largest facet on a diamond. Measured in millimeters.

*Depth* : Term for the height of a diamond. Measured in millimeters.

## Attributes
*Color* : Spanning from D to Z, a diamond's color scale ranges from "colorless" to "noticeably colored," respectively. This dataset ranges from D to J. In this scale, J would be "slightly colored."

*Carat* : Unit used to measure the weight of diamonds. Conversion to SI is 1 carat = 1/5 g. 

*Table Percentage* : Measure used to describe the ratio of a diamond's table width to its total width. 

*Depth Percentage* : Measure used to describe the ratio of a diamond's depth to its total width. 

*Cut* : Term for the quality of a diamond's cut. Lesser to better, this range contains the following set {Fair, Good, Very Good, Premium, Ideal}

*Clarity* : Term for the extent to which a diamond may contain inclusions and impurities. Less clear to more clear, this range contains the set {Included, Slightly Included II, Slightly Included I, Very Slightly Included II, Very Slightly Included I, Very Very Slightly Included, Internally Flawless}

*x* : Measure used to describe the width[mm] of a diamond.

*y* : Measure used to describe the length[mm] of a diamond. 

*z* : Measure used to describe the depth[mm] of a diamond. 


## Process 
As stated above, the raw data did not require restructuring or table joins, so I decided to forego SQL for this analysis. The total row count was enough for a spreadsheet and the validation tools in Sheets were adept for my needs. Upon sorting the columns, I found a few choice diamonds with errant measuremeents. 

The diamonds possessed attributes for width, length, and depth. Whether through an error of recording or some other means, there were a few that had 0 logged in these columns. These diamonds were removed, since this cast doubt as to the validity of their other values.

Now, what traits did I actually need? The dataset possessed a lot of information, but not all of it was interesting. Color and price were necessary, and I knew I'd be counting diamonds for distribution plots. Diamond size was sure to reveal interesting trends, but what metric was best suited for size? 

Between carat, table, depth, x, y, and z, at some point our descriptive coverage becomes superfluous. Best to choose some and see how adequate the choice was during analysis. I decided to keep carat, table percentage, and depth percentage. Understanding that table and depth percentages include the last three metrics helped that decision along. 

## Analysis
With the data structured like it was, a pivot table was the easy choice. It would deploy my aggregate functions and answer the questions I had quickly enough. Note: the respective standard deviations for some colors' mean prices were so large that I assumed I had a skewed distribution. This was a close guess, but not quite on the money.

I have included the pivot tables I generated in this folder, but when it came to visualizations I did not use them for my graphs. 

