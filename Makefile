#CMSC6950 course project
#vpath %.png output
#vpath %.csv csv_data
#vpath %.gdd csv_data
#vpath %.py src
VPATH = src:csv_data:output
GPATH = $(VPATH)
SRC=./src
DATA=./csv_data
OUTPUT=./output
PY=python3.5


FILES := 50089_2015  50089_2016 \
27211_2015 27211_2016 \
50430_2015 50430_2016

CSVFILESS := $(addsuffix .csv, $(FILES))

CSVFILES := $(addprefix $(DATA)/,$(CSVFILESS))

PLOTFIGSS := $(addsuffix _minmax.png, $(FILES))

PLOTFIGS := $(addprefix $(OUTPUT)/,$(PLOTFIGSS))

GDDFILESS := $(addsuffix .gdd, $(FILES))

GDDFILES := $(addprefix $(DATA)/, $(GDDFILESS))

GDDFIGSS := $(addsuffix _gdd.png, $(FILES))

GDDFIGS := $(addprefix $(OUTPUT)/,$(GDDFIGSS))

ANALYZEGDDFIGSS := $(addsuffix _analyze_gdd.png, $(FILES))

ANALYZEGDDFIGS := $(addprefix $(OUTPUT)/,$(ANALYZEGDDFIGSS))

BOKEHFILESS := $(addsuffix _bokeh_min_max.csv, $(FILES))

BOKEHFILES := $(addprefix $(DATA)/, $(BOKEHFILESS))

TBASE := 10
TUPPER := 30
TTYPE := C

.PHONY: All
All: $(CSVFILESS) $(GDDFILESS) $(PLOTFIGSS) $(GDDFIGSS) $(ANALYZEGDDFIGSS) $(BOKEHFILESS) report.pdf

#Download temperature data from web. 
#Usage: python3.5 src/download.py <param1>
#<param1> csv data file path and name 
#Description: The parameter contains storage path and file name. download.py
#could store the data to assigned path and file. If the file does not exist,
#download.py should creat data file.
#Example: python3.5 src/download.py ./csv_data/stjohns-500890-2015.csv
$(CSVFILESS):
	echo "Download datafiles"
	$(PY) $(SRC)/download.py $(subst csv_data/,,$@)

#Calculate GDD and plot GDD graph for each city
#Usage: python3.5 src/gdd.py <param1> <param2> <param3> <param4> <param5>
#<param1> csv source file path and name
#<param2> tbase
#<param3> tupper
#<param4> temperature type, C: Celsius, F: Fahrenheit
#<param5> output gdd file path and name
#Description: Calculate GDD for each city and station.
#Example: python3.5 src/gdd.py ./csv_data/stjohns-500890-2015.csv 10 30 ./output/stjohns-500890-2015.gdd
$(GDDFILESS):%.gdd:%.csv
	echo "Calculate GDD"
	$(PY) $(SRC)/gdd.py $(addprefix $(DATA)/,$<) $(TBASE) $(TUPPER)
   
#Plot temperature graph for each city and each station
#Usage: python3.5 src/plot.py <param1> <param2>
#<param1> input csv data file name and path
#<param2> output graph file name and path
#Description: plot.py read data file from input .csv file and plot temp graph
#for each .csv file. The output graph file name and path could be got from
#the second parameter
#Example: python3.5 src/plot.py ./csv_data/stjohns-500890-2015.csv ./output/stjohns-500890-2015.png
$(PLOTFIGSS):%_minmax.png:%.csv
	echo "Plot temp graphs"
	$(PY) $(SRC)/plot.py $(addprefix $(DATA)/,$<)

$(GDDFIGSS):%_gdd.png:%.gdd
	$(PY) $(SRC)/plot.py $(addprefix $(DATA)/,$(subst csv_data/,,$<))
$(ANALYZEGDDFIGSS):%_analyze_gdd.png:%.csv
	$(PY) $(SRC)/analyze_gdd.py $(addprefix $(DATA)/,$<)
	mv analyze_gdd.png $(OUTPUT)/$(subst .csv,,$<)_analyze_gdd.png

$(BOKEHFILESS):%_bokeh_min_max.csv:%.csv
	echo "Bokeh!"
	$(PY) $(SRC)/bokeh_html.py $(addprefix $(DATA)/,$(subst csv_data/,,$<))

report.pdf:
	echo "Generate report!"
	pdflatex ./report/GDD.tex
	pdflatex ./report/GDD.tex
	#bibtex  ./report/GDD.tex
	pdflatex ./report/GDD.tex

.PHONY: test
test:
	echo "Test modules"
	nosetests $(SRC)/testsuite


.PHONY: clean
clean:
	rm -rf $(DATA)/*
	rm -rf $(OUTPUT)/*
	rm *.png
	rm *.pdf
