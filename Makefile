report.pdf: report.tex plot1.jpg plot2.jpg
	latexmk -pdf report.tex

plot1.jpg: WHO-COVID-19-global-data.csv plot.py
	python3 plot.py

plot2.jpg: WHO-COVID-19-global-data.csv plot.py
	python3 plot.py

WHO-COVID-19-global-data.csv:
	wget https://covid19.who.int/WHO-COVID-19-global-data.csv

