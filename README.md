# sqlalchemy-challenge
Using SQLAlchemy ORM queries, Pandas, and Matplotlib to analyze the Hawaii climate.

### Climate Analysis and Exploration
First, connected to the hawaii.squlite database using SQLAlchemy to start a session referencing Station and Measurement data.

Then found the most recent date in the data and calculated the 12 preceding months of data to plot the percipitation values.
**Precipitation Analysis**
![Precipitation over a 1-year period.](https://github.com/KristaJoy/sqlalchemy-challenge/blob/main/Images/yearofrain.pngs | width=100px)

Next, I queried the total number of weather stations in the dataset and found which station was the most active. Using that station's data I found the temperature data and plotted it into a histogram with 12 bins to see how the temperature observation data (TOBS) was grouped.

**Station Analysis**
![Temperature over a 1-year period.](https://github.com/KristaJoy/sqlalchemy-challenge/blob/main/Images/temp_frequency.png)

After this initial analysis I designed a Flask API based on the queries I just developed. I created multiple routes that I outlined on my home page.

**Routes**
![Routes homepage.](https://github.com/KristaJoy/sqlalchemy-challenge/blob/main/Images/flask_homepage.png)j

### Bonus
The first bonus section was to do a further temperature analysis to discern if there is any meaningful difference between the temperature in June and December.

**Comparing June and December**
![Analyzing the difference between June and December temperatures.](https://github.com/KristaJoy/sqlalchemy-challenge/blob/main/Images/comparing_junedec.png)

The difference between June and December's average temps is not much—3.90 degrees! Using a t-test on the data I found that there is very strong evidence that it rejects the null hypothesis that the two groups are equal.

After this I looked at data for just one week—a proposed trip during the first week of August.

I plotted the average temperature and it's yerror.

**Trip's Average**
![Average for the week of my trip.](https://github.com/KristaJoy/sqlalchemy-challenge/blob/main/Images/trip_avgplot.png)

Looks like really nice weather!

I also calculated the daily rainfall average. Finding that I'd most like to stay out of the rain near the weather stations in Pearl City or Waikiki, as they had the least rain.

Finally, I calculated the daily temperature normals for the week of my trip. I created an area plot of the high, low, and average temps over the first week in August.

**Daily Temperature Normals**
![Daily temperature normals for the first week of August.](https://github.com/KristaJoy/sqlalchemy-challenge/blob/main/Images/trip_areaplot.png)

