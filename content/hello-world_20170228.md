Title: Hello, World!
Date: 2017-02-28 12:00
Category: Projects
Tags: project, citibike, youtube, R, cron, crontab, ggmap, ggplot2, jsonlite, caffeine
slug:hello-world
Authors: Matt Negrin
Summary: A blog post down memory lane

<br><br>
<br><br>
##**hi there**
######Welcome to my data blog. For a long time I have wanted to document some of my side projects and learnings. After years of procrastination, I've finally begun. Welcome!
######To kick things off, I thought it would be fun to reflect on the first data project I ever worked on. Being a bit introspective, my data science career track genuinely began (unknowingly) in an econometrics class in college. However, I did not formally begin learning about what data science was as a practice was until well after. In early 2014, I began working on data projects, not only as a means of self-learning, but also because I was fascinated by solving historically abstract problems with interesting data sets (this seemed to tie closely to why I enjoyed econometrics in college... nerd alert).
######I got hooked pretty quickly and have been working on side projects ever since, ranging from machine learning kaggle competitions to interactive Shiny apps to fantasy football lineup predictions, most recently working more intently on deep learning and image classification. 
######The blog will be a work in progress. For now, I hope to write about the side projects I'm working on, or even just about interesting things I've learned recently.

<br><br>
##**everyone loves videos**
######So here it is! The first data project I completed. As an early adopter of Citibike, I was intrigued by its open-sourced data. Citibike was already a popular source for analytical project work in 2014, but not nearly to the extent it is today. 
######Let's start with the final product. The video below visualizes the flow of Citibike station capacity onto a map of Manhattan for a 24-hour period (July 9, 2014). Each circle is a different Citibike station. The size of the circle indicates what percentage of its docks were unavailable. If the dock is completely full, the station circle turns red. The time lapse begins at midnight. Pay attention during commuting hours.
[!embed](http://www.youtube.com/watch?v=QxiTnqGxnZg)

<br><br>
##**how did i build it?**
######To say this was a hack-y project is an understatement. With little coding experience, I was really working off the cuff, reading whichever blog posts and Stack Overflow comments I could find to guide me. In retrospect, the project gave me exposure to a couple of great R packages, such as <a href="https://cran.r-project.org/web/packages/jsonlite/jsonlite.pdf" target="_blank">jsonlite</a> and <a href="https://cran.r-project.org/web/packages/ggmap/ggmap.pdf" target="_blank">ggmap</a>. Additionally, this was my first experience with <a href="http://crontab.org/" target="_blank">Crontab</a>, which has now become a staple for me, both at home and at work.
######Citibike generously makes their data easy to access. Annyone can go to <a href="http://citibikenyc.com/stations/json" target="_blank">this url</a> at any time to get a live snapshot of every station in the system, including the number of bikes available, the number of docks available, and the latitude/ longitutde location. R package <a href="https://cran.r-project.org/web/packages/jsonlite/jsonlite.pdf" target="_blank">jsonlite</a> makes reading clean json data ridiculously easy, with just one line of code:

{% include_code code/citibike_map.R lang:R lines:9-10 :hidefilename: jsonlite %}

######The json file provides a dataframe with the station data. To plot each of the stations on a map of NYC, I found an R package, <a href="https://cran.r-project.org/web/packages/ggmap/ggmap.pdf" target="_blank">ggmap</a>, which provides a great ggplot-like style for plotting latitude and longitude data. 
######Here is some sample code to generate the map of NYC and plot the corresponding stations.

<!-- {% include_code code/citibike_map.R lang:R lines:20-31 :hidefilename: ggmap %} -->

######So I thought this was pretty cool, but a snapshot was only so informative. The natural question is how this plot changes as the day went on. Thus, I discovered <a href="http://crontab.org/" target="_blank">Cron</a>. I scheduled my script to run every 5 minutes, saving a copy of the mapped image with a time-stamped filename to a folder on my local computer. I realized shortly thereafater that the cron would not run with my computer closed (duh). My crude solution was to leave my computer open and running for a full 48 hours (thanks, <a href="http://lightheadsw.com/caffeine/" target="_blank">caffeine</a>)!.
######Two days later, I had a folder of images with timestamped titles. I strung them together in a video to represent the 24-hour timeframe, and that was it!

<br><br>
##**what was good?**
######In retrospect, this project was great for me for a number of reasons. 
######First, I loved working on it. This was first time I had built something from scratch with code, I found that feeling to be exhilirating. I was proud of the finished product, and that I had managed to figure out how to complete it with just the help of the internet.
######Second, the conclusions I drew supported the frustrations I was having at the time with the Citibike service. I was often worried about commuting home at night via Citibike because of dock availability. Seeing how intensely bike availability actually fluctuated with commuting hours confirmed that I wasn't crazy, which is always good. 
######Lastly, the video ended up being a nugget of an idea that led to my first end-to-end data project at the end of 2014: a <a href="" target="_blank"></a>[Shiny app](https://mattnegrin.shinyapps.io/citibike/) that explored the relationship between weather and Citibike usage among different neighborhoods in Manhattan. Apologies for inundating the internet with yet another Citibike project...

<br><br>
##**what was bad?**
######As I said above, this project is pretty hack-y. I still laugh when I think about leaving my computer running for 48 hours as a means of collecting the data I needed, rather than seeking out the help of a server.
######My primary gripe with my execution is in the data collection. Rather than generate a static image every 5 minutes, I would have been far better off recording a snapshot of data every 5 minutes instead, compiling those snapshots into one large dataset. This way, I would have been able to work on much more interesting analyses later on.
######Of course, I could only have stored so many sets of data on my local computer before the dataset would have become too large. If redoing the project today, I would keep a script running on AWS that dumps the data into a PostgreSQL database, where I can come back at my leisure to tinker and explore.

<br><br>
##**next steps?**
######For this project, I don't have any! It was fun to go back down project memory lane. Below is the full script I wrote to generate and save a single map with plotted stations. For my next post, I'll focus on something I've been working on recently. Happy Citibiking!

<!-- {% include_code code/citibike_map.R lang:R %} -->