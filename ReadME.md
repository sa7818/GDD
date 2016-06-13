## Growing Degree Days in Canada

The goal of this project is to calculate GDD for three cities in Canada (St John's, Calgary, Toronto)
- The workflow for the project is as follow:

    Automation for downloading tempreture data

    Extracting required columns from data files

    Calculating GDD (via command line program)

    Storing calculations in .csv and .gdd files

    Creating plot showing an annual cycle of min/max daily temperatures.

    Producing reports based on the generated plots.

    Presentation (Web-based)

<br>
To view the web presentation [click here](https://sa7818.github.io/GDD/)
<br>


- GDD Project:
                     Version 1.0.0:

               The Project exists in Github repository(https://github.com/sa7818/GDD)
###### System Requirenments:
                      Linux/Mac
                      Python Python( 3.5.1 )
                      Latex/TexStudio
                      HTML(Web Based Presentation)

######  Contact Information:

- Sara Ayubian                   Email:sa7818@mun.ca
- Ghasem Alaee Khangha           Email:gak488@mun.ca
- Faramarz Dorani                Email:fd6713@mun.ca
- Stanley Uche Godfrey           Email:sug670@mun.ca
- Shuyue Qi                      Email:sq5222@mun.ca
- Lianbo Li                      Email:ll4734@mun.ca
- Oluwatosin Ifeoluwa Adelegan   Email:oia133@mun.ca

- File List(Directories):

<pre>
 	csv_data 
	output
	report 
	src 
	.gitignore 	
	GDDRequirements.md 	
	Makefile 
	ReadME.md
</pre>
---------
<pre>
csv_data/ 
	data.csv 
	st.johns_50089_.csv 
	stjohns_50089_2015.csv 
	stjohns_50089_2015_extracted.csv
</pre>
-----
<pre>
/src/
 	testsuite 
	download.py 
	gdd.py 	
	main.py 
	plot.py

</pre>
------
<pre>
/report/
 	GDD.tex
 </pre>

<b>USER GUIDE:<b>
<p> To run this project, you must have the following packages installed on your python 2.7 or 3x environment:
<pre>
	pip
	pandas
	sys
	urllib.request
</pre>
</p>

##CLONING THIS REPOSITORY:
<p> To clone this repository, do the following:
<pre>
	cd ~ or cd ~/<Workspace>
	git clone https://github.com/sa7818/GDD.git
</pre>
</p>
<p><b>N.B:</b> After cloning you need to run <b>make</b> command from the cloned repository to recompile this project(program)
</br>

<b> Please feel free to contact us for more information...
