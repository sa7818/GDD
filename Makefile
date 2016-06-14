#CMSC6950 course project
vpath %.csv ./csv_data
vpath %.png ./output
vpath %.py ./src
SRC=./src
DATA=./csv_data
OUTPUT=./output
PY=python3.5

#define cicies
SJ=stjohns
CG=calgary
TR=toronto

FILES := 50089_2015  50089_2016 \
27211_2015 27211_2016 \
5051_2015 5051_2016

CSVFILESS := $(addsuffix .csv, $(FILES))

CSVFILES := $(addprefix $(DATA)/,$(CSVFILESS))

PLOTFIGSS := $(addsuffix .png, $(FILES))

PLOTFIGS := $(addprefix $(OUTPUT)/plot_images/,$(PLOTFIGSS))

GDDFILESS := $(addsuffix .gdd, $(FILES))

GDDFILES := $(addprefix $(DATA)/, $(GDDFILESS))

GDDFIGSS := $(addsuffix .png, $(FILES))

GDDFIGS := $(addprefix $(OUTPUT)/plot_images/,$(GDDFIGSS))

BOKEHFILESS := $(addsuffix _bokeh_min_max.csv, $(FILES))

BOKEHFILES := $(addprefix $(DATA)/, $(BOKEHFILESS))

TBASE := 10
TUPPER := 30
TTYPE := C

.PHONY: All
All: report.pdf $(BOKEHFILES)

report.pdf: $(GDDFIGS) $(BOKEHFILES)
	echo "Generate report!"
	pdflatex ./report/GDD.tex
	pdflatex ./report/GDD.tex
	#bibtex  ./report/GDD.tex
	pdflatex ./report/GDD.tex
        
$(BOKEHFILES): $(CSVFILES)
	echo "Bokeh!"
	for i in $(FILES); \
	do \
		$(PY) $(SRC)/bokeh_html.py $$i.csv $(BOKEHFILES);\
	done
	
$(GDDFIGS): $(GDDFILES)
	for i in $(FILES); \
	do \
		$(PY) $(SRC)/plot.py $(DATA)/$$i.gdd;\
	done

#Calculate GDD and plot GDD graph for each city
#Usage: python3.5 src/gdd.py <param1> <param2> <param3> <param4> <param5>
#<param1> csv source file path and name
#<param2> tbase
#<param3> tupper
#<param4> temperature type, C: Celsius, F: Fahrenheit
#<param5> output gdd file path and name
#Description: Calculate GDD for each city and station.
#Example: python3.5 src/gdd.py ./csv_data/stjohns-500890-2015.csv 10 30 ./output/stjohns-500890-2015.gdd
$(GDDFILES):$(PLOTFIGS)
	echo "Calculate GDD"
	for i in $(FILES); \
	do \
		$(PY) $(SRC)/gdd.py $$i.csv $(TBASE) $(TUPPER);\
	done

#Plot temperature graph for each city and each station
#Usage: python3.5 src/plot.py <param1> <param2>
#<param1> input csv data file name and path
#<param2> output graph file name and path
#Description: plot.py read data file from input .csv file and plot temp graph
#for each .csv file. The output graph file name and path could be got from
#the second parameter
#Example: python3.5 src/plot.py ./csv_data/stjohns-500890-2015.csv ./output/stjohns-500890-2015.png
$(PLOTFIGS):$(CSVFILES) 
#$(PLOTFIGS):%.png:%.csv
	echo "Plot temp graphs"
	for i in $(FILES); \
	do \
		$(PY) $(SRC)/plot.py $(DATA)/$$i.csv;\
	done

#Download temperature data from web. 
#Usage: python3.5 src/download.py <param1>
#<param1> csv data file path and name 
#Description: The parameter contains storage path and file name. download.py
#could store the data to assigned path and file. If the file does not exist,
#download.py should creat data file.
#Example: python3.5 src/download.py ./csv_data/stjohns-500890-2015.csv
$(CSVFILES):
	echo "Download datafiles"
	for i in $(CSVFILESS); \
	do \
		$(PY) $(SRC)/download.py $$i; \
	done


.PHONY: test
test:
	echo "Test modules"
	nosetests $(SRC)/testsuite


.PHONY: clean
clean:
	rm -rf $(DATA)/*
	rm -rf $(OUTPUT)/plot_images/*
