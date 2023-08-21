# Snapshot Pricelist

This dataset was provided by a user on Kaggle for training use. It can be found [here](https://www.kaggle.com/datasets/shivam2503/diamonds). 
It should considered a snapshot of the collective traits of a group of diamonds, with no time component being presented. 
Emphasis will be put on correlation and any trends seen therein. 

## Introduction 

While the context provided on the Kaggle data card is sufficient for analysis purposes, further research revealed some inconsistencies with
certain definitions. That being said, upon preparing the data for analysis I found very little cleaning or sorting to do. Despite this, 
I was still interested in what the data might reveal, and settled on an explorative analysis with a focus on visualizations. Spreadsheets proved to be satisfactory.
I believe I could use this data to design a predictive model in the future and will likely do this fairly soon. 

My tentative goal was to identify majority and minority diamonds with regard to color. Did prices support the resulting scarcity or surplus? 

Barring this, I hoped to design a dashboard that would enable someone to gather pricing information on a specific diamond of their choosing.
The final product can be found [here](https://public.tableau.com/views/DiamondShoppingDashboard/Dashboard?:language=en-US&:display_count=n&:origin=viz_share_link). Feel free to click around to filter the dashboard down. 

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



