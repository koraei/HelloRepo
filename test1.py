#a=56
#b=42
#c=a+b
#m=float(input('give me a number'))
#print('your number is %0.3f ' %m,' and a+b is %0.4f' %c)
#stencil2D9PR_out_16_D_3_csynth.rpt
import re
import os
import csv
#*****************************************
def printDirNames(currentPath):
    subPath="\\syn\\report"

    filenames= os.listdir (".") # get all files' and folders' names in the current directory

    subdirs = []
    for filename in filenames: # loop through all the files and folders
        if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
            subdirs.append(filename)
            
    subdirs.sort()
    fullPath = curPath + "\\"+ subdirs[2] + subPath


    
   
    return subdirs;

#**********************************************
def getRptFilePath(fullPath):
     for file in os.listdir(fullPath):
        if file.endswith(".rpt"):
            return os.path.join(fullPath, file);
           # print(os.path.join(fullPath, file))
     
#**********************************************
def findResources (lines):
    counter = 0
    UtliFound=False
    fBreak =False
    fIntervalsFound = False
    dicResources ={}
    for line in lines:
        counter += 1
        if (line.find("Interval")!=-1 and fIntervalsFound == False):
            fIntervalsFound = True
            words= lines[counter+2].split('|')
            dicResources['Latency'] = words[2].replace(' ', '')
            dicResources['II'] = words[4].replace(' ', '')
            fIntervalsFound = True
        
            
        if (line.find("Utilization Estimates")!=-1):
##            print('we found utilization at line ', counter)
            UtliFound = True
            #print ('next line is',lines[counter+12])
##            print (line)
        if (UtliFound):
            if (line.find("|Total")!=-1):
                words= line.split('|')
    ##            for curWord in words:
    ##                print(curWord)
    ##                curWord=curWord.replace(' ', '')
    ##                print(curWord)
##                print ("BRAM = ",words[2].replace(' ', '')," DSP = " , words[3].replace(' ', ''), " FF = ", words[4].replace(' ', ''), " LUT = ", words[5].replace(' ', ''))
##                strResources = "BRAM = " + words[2].replace(' ', '') + " DSP = "
##                strResources += words[3].replace(' ', '') + " FF = " + words[4].replace(' ', '')
##                strResources += " LUT = " + words[5].replace(' ', '')
                
                dicResources['BRAM']=  words[2].replace(' ', '')
                dicResources['DSP']=  words[3].replace(' ', '')
                dicResources['FF']=  words[4].replace(' ', '')
                dicResources['LUT']=  words[5].replace(' ', '')
                fBreak =True
        if (fBreak): break
    return dicResources;
    


#****************************************

csvfile = open('Resources.csv', 'w', newline='') 
fieldnames = ['Output','Depth','Latency','II','BRAM', 'DSP', 'FF', 'LUT']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

#dirs= os.listdir(path)
curPath=os.getcwd()
#os.chdir("/mydir")
subdirs = []
subdirs=printDirNames(curPath)
subPath="\\syn\\report"
dicResources={}
for index,curSubDir in enumerate(subdirs):
        fullPath = curPath + "\\"+ curSubDir + subPath
        #print(index, " ==> ", fullPath)
        print (getRptFilePath(fullPath))
        rptFileName = getRptFilePath(fullPath)
        frpt = open(rptFileName,'r')
        lines = frpt.readlines()
        dicResources=findResources(lines)
        words = rptFileName.split('_')
        dicResources['Output'] = words[3]
        dicResources['Depth'] = words[5]
        print ("****")
        print("BRAM = ",dicResources['BRAM'])
        print("DSP = ",dicResources['DSP'])
        print("LUT = ",dicResources['LUT'])
        print("FF = ",dicResources['FF'])
        writer.writerow(dicResources)
        frpt.close()
csvfile.close()
##f = open('helloworld.csv','w')
##f.write('hello world')
##f.close()
##
####f = open('stencil2D9PR_out_16_D_3_csynth.rpt','r')
####f2 = open('stencil2D9PR_out_16_D_3_csynth.rpt','r')
#####message = f.read()
#####print(message)
####
####lines = f2.readlines()
####dicResources=findResources(lines)
####print("BRAM = ",dicResources['BRAM'])
####print("DSP = ",dicResources['DSP'])
####print("LUT = ",dicResources['LUT'])
####print("FF = ",dicResources['FF'])
###Boolean UtliFound;
##
##f.close()

    
   



