files = ['../samples/vmware-perf-host', '../samples/vmware-perf-guest']
numfiles = 10

for filename in files:
    source = open(filename+'.csv', 'rU')
    sourcelines = source.readlines()
    numlines = len(sourcelines)

    line = 1
    filenum = 0
    dest = None
    
    headerline = sourcelines[0]

    while line < numlines:
        print "%s %s %s %s" % (line, numlines, numfiles, filenum)
        if line >= ((numlines / numfiles ) * filenum) and filenum < numfiles:
            if type(dest) == file:
                dest.close()
            destfilename = "%s%s.csv" % (filename, filenum)
            print "opening %s" % destfilename
            dest = open("%s%s.csv" % (filename, filenum), 'w+')
            dest.write(headerline)
            filenum += 1
        dest.write(sourcelines[line])
        line += 1
    dest.close()
        
