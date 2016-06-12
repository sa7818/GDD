#CMSC6950 course project
vpath %.csv csv_data
vpath %.png output
vpath %.py ./src
SRC=./src
DATA=./csv_data
OUTPUT=./output

#define cicies
SJ=stjohns
CG=calgary
TR=toronto

FILES := $(SJ)-500890-2015  $(SJ)-50089-2016 \
$(CG)-27211-2015 $(CG)-27211-2016 \
$(TR)-5051-2015 $(TR)-5051-2016

CSVFILESS := $(addsuffix .csv, $(FILES))

CSVFILES := $(addprefix $(DATA)/,$(CSVFILESS))

PLOTFIGSS := $(addsuffix .png, $(FILES))

PLOTFIGS := $(addprefix $(OUTPUT)/,$(PLOTFIGSS))

GDDFILES := $(addprefix GDD-,$(FILES))

GDDFIGSS := $(addsuffix .png, $(GDDFILES))

GDDFIGS := $(addprefix $(OUTPUT)/,$(GDDFIGSS))

TBASE := 10
TUPPER := 30
TTYPE := C

.PHONY: All
All: report.pdf $(GDDFIGS) $(PLOTFIGS)

report.pdf: $(GDDFIGS) $(PLOTFIGS)
	echo "Generate report!"
	pdflatex ./report/GDD.tex
	pdflatex ./report/GDD.tex
	#bibtex  ./report/GDD.tex
	pdflatex ./report/GDD.tex
        
.PHONY: test
test:
	echo "Test modules"
	nosetests $(SRC)/testsuite
	

#Calculate GDD and plot GDD graph for each city
#Usage: python3.5 src/gdd.py <param1> <param2> <param3> <param4> <param5>
#<param1> csv source file path and name
#<param2> tbase
#<param3> tupper
#<param4> temperature type, C: Celsius, F: Fahrenheit
#<param5> output gdd graph file path and name
#Description: Calculate GDD for each city and station. Plot gdd graph.
#Example: python3.5 src/gdd.py ./csv_data/stjohns-500890-2015.csv 10 30 C ./output/GDD-stjohns-500890-2015.png
$(GDDFIGS):$(PLOTFIGS)
	echo "Calculate GDD and plot graph"
	for i in $(FILES); \
	do \
		python3.5 $(SRC)/gdd.py $(DATA)/$$i.csv $(TBASE) $(TUPPER) $(TTYPE) $(OUTPUT)/GDD-$$i.png;\
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
		python3.5 $(SRC)/plot.py $(DATA)/$$i.csv $(OUTPUT)/$$i.png;\
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
		python3.5 $(SRC)/download.py $(DATA)/$$i; \
	done



.PHONY: clean
clean:
	rm -rf $(DATA)/*
	rm -rf $(OUTPUT)/*
