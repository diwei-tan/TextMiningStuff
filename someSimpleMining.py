import os
import re

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

filePaths = []
for dirpath, dirnames, files in os.walk('Root File Path'):
    for filename in files:
        if filename.endswith('Input'):
            filePaths.append(os.path.join(dirpath, filename))

#If empty, there is nothing
if len(filePaths)==0:
    print('No matching files found.')
else:
    print(len(filePaths), ' file matches found. scanning all for <PATTERN> properties')
    contents = []
    for path in filePaths:
        f = open(path, "r")
        contents.append(f.read())
    if len(contents)==0:
        print('No PATTERN found in all matching files.')
    else:
        for content in contents:
            results = re.findall(r'<PATTERN((.|\n)*?)(/>)', content)
            for tuplestring in results:
                str = convertTuple(tuplestring)
                instanceclass = re.search(r'PATTERN=((.|\n)*?) ', str).group()
                if instanceclass:
                    classarray = instanceclass.split('"')
                    instanceclass = classarray[1]
                    print(instanceclass)
                instanceOp = re.search(r'PATTERN=((.|\n)*?) ', str).group()
                if instanceOp:
                    oparray = instanceOp.split('"')
                    instanceOp = oparray[1]
                    print(instanceOp)
                javaFilePaths = []
                for dirpath, dirnames, files in os.walk('Root File Path'):
                    for filename in files:
                        if filename.endswith(instanceclass+'.java'):
                            javaFilePaths.append(os.path.join(dirpath, filename))
                if len(javaFilePaths)==0:
                    print('No such .java file found.')
                else:
                    for path in javaFilePaths:
                        print(javaFilePaths)
