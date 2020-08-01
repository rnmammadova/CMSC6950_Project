report.pdf: report.tex plot1.jpg plot2.jpg
	latexmk -pdf

plot1.jpg:usgs_earthquakes_2014.csv.csv plot.py
	python plot.py

plot2.jpg:usgs_earthquakes_2014.csv plot.py
	python plot.py

usgs_earthquakes_2014.csv:
	curl -L http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv
.PHONY: clean almost_clean
	rm report.pdf
	rm myplot.png

almost clean:
	latxemk -c
