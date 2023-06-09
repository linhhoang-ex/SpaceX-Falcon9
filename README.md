# SpaceX Falcon 9 First Stage Landing Prediction

SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. 

Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

In this capstone, we collect a record for each payload carried during a SpaceX mission into outer space. We then build several machine learning models to
predict whether the Falcon 9 first stage will land successfully. 


<p align="center">
  <img src="landing_1.gif"  width="550"><br>
  <em>An example of a successful landing</em>
</p>

<p align="center">
  <img src="crash.gif"  width="550"><br>
  <em>An example of failed landings</em>
</p>


## Methodology
The project was conducted through the following labs, in the chronological order: 
* [`Lab1A`](W1A_Data_Collection_API_Lab.ipynb): Collecting the data via making a `get` request to the SpaceX API.
* [`Lab1B`](W1A_Data_Collection_Webscraping.ipynb): Web Scraping for Falcon 9 and Falcon Heavy Launches Records from Wikipedia.
* [`Lab1C`](W1B_Data_Wrangling.ipynb): Data Wrangling on the collected data.
* [`Lab2A`](W2A_Exploratory_Data_Analysis_with_SQL.ipynb): Exploratory Data Analysis (EDA) on the SpaceX dataset using SQL. 
* [`Lab2B`](W2B_Exploratory_Data_Analysis_with_Pandas.ipynb): EDA and Feature Engineering with `Pandas` & `Matplotlib`.
* [`Lab3A`](W3A_Interactive_Visual_Analytics_with_Folium.ipynb): Build an Interactive Map with `Folium`, see a snapshot [here](W3A_launch_site_marker_cluster.png). 
* [`Lab3B`](W3B_SpaceX_Dash_App.py): Build a Dashboard with `Plotly Dash`, see a snapshot [here](W3B-dashboard-1-ipad.jpg).
* [`Lab4`](W4_SpaceX_Machine_Learning_Prediction.ipynb): Predictive Analysis (Classification) with Machine Learning Models.


## Project Report
A complete project report can be found [here](ds-capstone-project-report.pdf). 

[![](project-report-coverpage.png)](ds-capstone-project-report.pdf)


