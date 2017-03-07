#set up directory structure
mainDir <- '~/citibike_map'
subDir  <- 'output'
ifelse( !dir.exists(file.path( mainDir )), dir.create(file.path( mainDir )), FALSE)
ifelse( !dir.exists(file.path( mainDir, subDir)), dir.create(file.path( mainDir, subDir )), FALSE)
setwd(mainDir)

#importing data from json file
require(jsonlite)
json_data = jsonlite::fromJSON(txt = "http://citibikenyc.com/stations/json")

#creating dataframe
citiframe = dplyr::tbl_df(json_data$stationBeanList)
citiframe$time = json_data$executionTime

#adding relevant columns
citiframe$total <- citiframe$availableDocks + citiframe$availableBikes
citiframe$bike_ratio <- ifelse(citiframe$total==0,1,citiframe$availableBikes / citiframe$total)

#creating map of manhattan
require(ggmap)
require(ggplot2)
nycmap <- ggmap::get_map(location = c(lon = -73.992920, lat = 40.740075), 
                    color ="color", source= "google", zoom = 13, 
                    maptype = "roadmap", filename = "ggmapnyc")

#creating map with size-dependent dots
dotmap <- ggmap::ggmap(nycmap) + 
    geom_point(aes(x = longitude, y = latitude, size = (citiframe$bike_ratio)*7), colour = ifelse(citiframe$bike_ratio==1, 'red', 'green4'), data = citiframe) + 
    theme(axis.title.x = element_blank(), axis.text.x = element_blank(), axis.title.y = element_blank(), axis.text.y = element_blank(), title = element_text(face="bold", size=20)) +
    labs(title=json_data$executionTime) + guides(colour = FALSE, size=FALSE)

#saving chart to directory
require(png)
mypath <- file.path(mainDir,subDir,paste("citibike_", gsub(" ","__",gsub(":","_",json_data$executionTime)), ".png", sep = ""))
png(file=mypath)
dotmap
dev.off()