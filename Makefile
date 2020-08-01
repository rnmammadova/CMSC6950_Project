report.pdf: report.tex plot1.jpg plot2.jpg
	latexmk -pdf

plot1.jpg: usgs_earthquakes_2014.csv plot.py
	python3 plot.py

plot2.jpg: usgs_earthquakes_2014.csv plot.py
	python3 plot.py

usgs_earthquakes_2014.csv:
	wget http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv

