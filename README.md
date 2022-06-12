# Regression_Project

# Goal 
Construct an ML Regression model that predict propery tax assessed values ('taxvaluedollarcnt') of Single Family Properties using attributes of the properties from the year 2017
* Find the key drivers of property value for single family properties. what are the most profitable aminites to have a bedroom or bathroom. and what does that have to do with value.
* Deliver a report and recomendations to Zillow executives with further recomendations on what to do next.
* Fix Zacks mistake and recover the FIPS numbers
# Why
* the job is to help Zillow make more informed decisions when offering houses 
* Find what drives tax value and what does not 
* Fix zacks mistake 
* using the data science pipeline we with mithodicly prove why our models work and in turn help Zillow become more profitable 
# Hypotheses
1.  There is not a linear correlation between square footage of home and tax value.
2.  There is not a linear correlation between bedrooms and tax value.
3.  There is not a linear correlation between bathrooms and tax value.
4.  there is no linear correlation between county and tax value
# Data Dictionary
* bedrooms: the amount of bedroom identity
* bathrooms: the amount of bathrooms identity
* yearbuilt: the identity of the year the home was build
* square_feet: the identity of how many square_feet are in the home
* tax_value: the tax_value identity
* property_age: the amount of time the property has in age identity
* tax_rate: the rate at wich the incurring taxes identity 
# Executive Summary 
* In this presention I will attack and perform a heavy proccess of regression analysis on the tax assesed values from the year of 2017, to predict future tax values. I will also be searching for the key drives of property value, that turned out to be bathrooms and sqr feet and county that the house was located in. I created a ols regressor model with a 30% effective over my baseline so I as a data scientist would recommend further analysis with my model.
* Final RMSE of 200650 
# Recommendations
* look at thing like crime rate, police response time, distance to city center ect...
* cont following bond and interest rates, political climate
* get in contact with realestate agents and survey the thought of people in field. 
* this model will need constant watching so a full time team to work on this project 
