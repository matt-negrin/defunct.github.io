Title: Hello, World!
Date: 2017-02-28 12:00
Category: Pelican
Tags: project, citibike, youtube, R, cron, crontab, ggmap, ggplot2, jsonlite, caffeine
slug:hello-world
Authors: Matt Negrin
Summary: Blog post down project memory lane

### hi there
Welcome to my data blog. For a long time, it has been on my to-do list to document some of the side projects I work on. After 2 years of procrastination, I've finally begun. Welcome!

To kick things off, I thought it would be fun to reflect on the first data project I ever worked on. Being a bit introspective, I think my data science career track genuinely began (unknowingly at the time) in an econometrics class in college. However, I did not formally begin learning about what data science as a practice was until after college, during my first job at FactSet. In early 2014, I began working on data projects, not only as a means of self-learning, but also because I was fascinated by solving historically abstract problems with interesting data sets (this seemed to tie closely to why I enjoyed econometrics in college... nerd alert).

I got hooked pretty quickly and have been working on side projects ever since, ranging from machine learning kaggle competitions to interactive Shiny apps to fantasy football lineup predictions, most recently working more intently on deep learning and image classification. 

The blog will be a work in progress. For now, I hope to write about the side projects I'm working on, or even just about interesting things I've learned recently.

### everyone loves videos
So here it is! The first data project I completed. As an early adopter of Citibike, I was intrigued by its open-sourced data. Citibike was already a popular source for analytical project work in 2014, but not nearly to the extent it is today. 

Let's start with the final product. The video below visualizes the flow of Citibike station capacity onto a map of Manhattan for a 24-hour period (July 9, 2014). Each circle is a different Citibike station. The size of the circle indicates what percentage of its docks were unavailable. If the dock is completely full, the station circle turns red. The time lapse begins at midnight.

[!embed](http://www.youtube.com/watch?v=QxiTnqGxnZg)

### how did i build it?
To say this was a hack-y project is an understatement. With little coding experience, I was really working off the cuff, reading whichever blog posts and Stack Overflow comments I could find to guide me. In retrospect, the project gave me exposure to a couple of great R packages, such as [jsonlite](https://cran.r-project.org/web/packages/jsonlite/jsonlite.pdf) and [ggmap](https://cran.r-project.org/web/packages/ggmap/ggmap.pdf). Additionally, this was my first experience with [Crontab](http://crontab.org/), which has now become a staple for me, both at home and at work.

Citibike generously makes their data easy to access. Annyone can go to [this url](http://citibikenyc.com/stations/json) at any time to get a live snapshot of every station in the system, including the number of bikes available, the number of docks available, and the latitude/ longitutde location. R package [jsonlite](https://cran.r-project.org/web/packages/jsonlite/jsonlite.pdf) makes reading clean json data ridiculously easy, with just one line of code:

    require(jsonlite)
    json_data = jsonlite::fromJSON(txt = "http://citibikenyc.com/stations/json")

The json file provides a time of snapshot and a dataframe with the station data. The next thing I wanted to do was figure out how to plot each of the stations on a map of NYC. I found R package, [ggmap](https://cran.r-project.org/web/packages/ggmap/ggmap.pdf), which provides a great ggplot-like style for plotting latitude and longitude data. 

Here is some sample code to generate the map of NYC and plot the corresponding stations.

    nycmap <- ggmap::get_map(location = c(lon = -73.992920, lat = 40.740075), color ="color", source= "google", zoom = 13, maptype = "roadmap", filename = "ggmapnyc")

    #adding in dots for each station, sized and colored by the bike ratio
    ggmap::ggmap(nycmap) + 
        geom_point(aes(x = longitude, y = latitude, size = (citiframe$bike_ratio)*7), colour = ifelse(citiframe$bike_ratio==1, 'red', 'green4'), data = citiframe) + 
        theme(axis.title.x = element_blank(), axis.text.x = element_blank(), axis.title.y = element_blank(), axis.text.y = element_blank(), title = element_text(face="bold", size=20)) +
        labs(title=json_data$executionTime) + guides(colour = FALSE, size=FALSE)

So I thought this was pretty cool, but a snapshot was only so informative. I wanted to see how the plot changed as the day went on. After a bit of research, I discovered [Cron](http://crontab.org/). I figured out how to schedule my script to run every 5 minutes, saving a copy of the mapped image with a time-stamped filename to a folder on my local computer. I realized shortly thereafater that the cron would not run with my computer closed (duh). My crude solution was to leave my computer open and running for a full 48 hours (thank you, [caffeine](http://lightheadsw.com/caffeine/).

Two days later, I had a folder of images with timestamped titles. I strung them together in a video to represent the 24-hour timeframe, and that was it!

### what was good?
In retrospect, this project was great for me for a number of reasons. 

First, I loved working on it. This was first time I had built something from scratch with code, I found that feeling to be exhilirating. I was proud of the finished product, and that I had managed to figure out how to complete it with just the help of the internet.

Second, the conclusions I drew supported the frustrations I was having at the time with the Citibike service. I was often worried about riding a bike to commute home at night from work because of dock availability. Seeing that how intensely bike availability fluctuated with commuting hours confirmed that I wasn't crazy, which was good. Three years later, I'm sure that rebalancing efforst have led to better bike and dock availabilities during commuting hours, but, from experience, it is still a work in progress.

Lastly, the video ended up being a nugget of an idea that led to my first end-to-end data project at the end of 2014: a [Shiny app](mattnegrin.shinyapps.io/citibike/) that explored the relationship between weather and Citibike usage among different neighborhoods in Manhattan. Apologies for inundating the internet with yet another Citibike project...

### what was bad?
As I said above, this project is pretty hack-y. I still laugh when I think about leaving my computer running for 48 hours as a means of collecting the data I needed, rather than seeking out the help of a server.

My primary gripe with my execution is in the data collection. Rather than generate a static image every 5 minutes, I would have been far better off recording a snapshot of data every 5 minutes instead, compiling those snapshots into one large dataset. This way, I would have the flexibility to do a ton of much more interesting analyses later on.

Of course, I could only store so many 5-minute intervals of data on my local computer before the dataset would have become too large. If redoing the project today, I would keep a script running on AWS that dumps the data into a PostgreSQL database, where I can come back at my leisure to tinker and explore.

### next steps?
For this project, I don't have any! It was fun to go back down project memory lane. For my next post, I'll focus on something I've been working on recently. Happy Citibiking!