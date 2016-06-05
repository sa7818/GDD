filenames=["STJOHNS1988TO1995.txt","STJOHN'SA1996TO2012.txt","STJOHNSWESTCDA1976TO1987.txt"]

for var in filenames:
    f=open(var,'r')
    file_count=0;
    fname= "./Downloaded_files/{}{}.CSV".format(var[:-3],file_count)
    while 1:
        line=f.readline()
        if not line:
            break
        if line:
            line=line[:-1]
            urlline="'{}'".format(line)
            request.urlretrieve(urlline,fname)
            file_count=file_count+1
    f.close()
