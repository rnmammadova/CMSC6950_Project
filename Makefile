report.pdf: report.tex cases_deaths.jpg death_rate.jpg
	latexmk -pdf report.tex

cases_deaths.jpg: WHO-COVID-19-global-data.csv cases_deaths.py
	python3 cases_deaths.py

death_rate.jpg: WHO-COVID-19-global-data.csv death_rate.py
	python3 death_rate.py

WHO-COVID-19-global-data.csv:
	wget https://covid19.who.int/WHO-COVID-19-global-data.csv

.PHONY: almost_clean clean


clean: almost_clean
	rm WHO-COVID-19-global-data.csv
	rm report.pdf
	rm death_rate.jpg cases_deaths.jpg

almost_clean:
	latexmk -c

