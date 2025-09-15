Power BI Spotify 2023 Songs Dashboard

![Spotify 2023 Dashboard](images/Spotify%202023%20Songs%20Dashboard.png)

This dashboard visualizes and analyzes Spotify streaming data for 2023. Tracks are ranked by streams, charts position, album covers, etc.
Based largely on the PowerBIPark tutorial: “Spotify Analysis in Power BI (2023)”.

🔍 Overview

Imports a CSV dataset containing songs, artists, streams, and chart positions for 2023.

Enhances the dataset by fetching album cover images via the Spotify API.

Displays insights including:

Top streamed songs

Highest chart positions

Visuals with album cover previews

Dynamic HTML/Vega visuals using measures in Power BI

📚 Tutorial Reference

Tutorial followed: PowerBIPark – Spotify Analysis in Power BI (2023)

Video link: PowerBIPark YouTube Tutorial

🛠️ Tools & Technologies
Tool / Language	Purpose
Power BI	Main dashboard / visuals
DAX (Data Analysis Expressions)	Creating measures for highest chart position, image URL, etc.
Python	Fetching album cover images via Spotify API, cleaning data
Spotify API	Getting track metadata such as album covers
Vega / HTML / CSS	Custom visuals (HTML embedding / Vega chart) in Power BI