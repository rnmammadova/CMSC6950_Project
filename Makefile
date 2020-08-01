report.pdf: report.tex myplot.png
	latexmk -pdf

myplot.png:data.txt plot.py
	python plot.py

data.txt: makedata.py

covid19.csv:
	curl -L https://health-infobase.canada.ca/src/data/covidLive/covid19.csv

.PHONY: clean almost_clean
	rm report.pdf
	rm myplot.png

almost clean:
	latxemk -c
