#utils.py python3 
from re import sub

def getconf(name):
    # grab the env from jvim.conf
    cname = name
    cfile = open(cname + '.conf')
    
    envars = {}
   

    for line in cfile:
        #print('this is the line: ' + line)

        marker = '#'

        crline = line.partition(marker)[0].strip()
        



        if not crline:
            continue

        # check to see if the line has a comment. using regular experssions
        
        
        line = crline.strip()
        #print('this is the line:' + str(line))
        line = line.replace(' = ','=')
        #print('this is the line:' + str(line))

        cdata = line.split('=')
        
        #print('this is the line: cdata[1] ' + str(cdata[1]))
        print('this is the line:' + str(line))
        envars[str(cdata[0].lower())] = sub('\[|\]|\'', '' , str(cdata[1].lstrip().split(',')))
        


    return envars

envars = getconf('/Users/Noe/workspace/stakenanny/candiapps/test/test')