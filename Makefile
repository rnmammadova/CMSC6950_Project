report.pdf: report.tex cases&deaths.jpg death_rate.jpg
	latexmk -pdf report.tex

cases&deaths.jpg: WHO-COVID-19-global-data.csv plot.py
	python3 plot.py

death_rate.jpg: WHO-COVID-19-global-data.csv plot.py
	python3 plot.py

WHO-COVID-19-global-data.csv:
	wget https://covid19.who.int/WHO-COVID-19-global-data.csv

.PHONY: almost_clean clean


clean: almost_clean
	rm WHO-COVID-19-global-data.csv
	rm report.pdf
	rm cases&deaths.jpg death_rate.jpg

almost_clean:
	latexmk -c

