'''
updateBun bun to update
bat_file
update_file
'''
__author__ = 'fyu'
from config import *

BUFFERING_SIZE=1048576
#BUFFERING_SIZE=10

def updateBATFast(bat_file_name,update_file_name):
    bat_file=open(bat_file_name,'r+')
    update_file=open(update_file_name,'r')
    for updateLine in update_file:
        (updateLineNumStr,updateValue)=updateLine.split(',')
        updateLineNum=long(updateLineNumStr)
        bat_file.seek((updateLineNum-1)*len(updateLine))
        bat_file.write(updateLine)
        bat_file.seek(0)
    bat_file.close()
    update_file.close()

def updateBAT1(bat_file_name,update_file_name):
    bat_file=open(bat_file_name,'r+', buffering=BUFFERING_SIZE)
    update_file=open(update_file_name,'r', buffering=BUFFERING_SIZE)
    for updateLine in update_file:
        (updateLineNumStr,updateValue)=updateLine.split(',')
        updateLineNum=long(updateLineNumStr)
        currentLineNum=1
        while currentLineNum < updateLineNum: # simulating seeking next line
            bat_file.seek(len(updateLine),1)
            currentLineNum+=1
        # bat_file.seek((currentLineNum-1)*len(updateLine))
        # bat_file.seek((updateLineNum-1)*len(updateLine))
        # print '%d\n' % currentLineNum
        bat_file.write(updateLine)
        bat_file.seek(0)
    bat_file.close()
    update_file.close()
    
def updateBAT2(bat_file_name,update_file_name):
    bat_file=open(bat_file_name,'r+', buffering=BUFFERING_SIZE)
    update_file=open(update_file_name,'r', buffering=BUFFERING_SIZE)
    for updateLine in update_file:
        (updateLineNumStr,updateValue)=updateLine.split(',')
        updateLineNum=long(updateLineNumStr)
        currentLineNum=1
        while currentLineNum < updateLineNum: # simulating seeking next line
            #print '%d\n' % bat_file.tell()
            bat_file.seek(1,1)
            currentLineNum+=1
        # bat_file.seek((currentLineNum-1)*len(updateLine))
        # bat_file.seek((updateLineNum-1)*len(updateLine))
        print '%d\n' % currentLineNum
        bat_file.write(updateLine)
        bat_file.seek(0)
    bat_file.close()
    update_file.close()


def updateTBAT(tbat_file_name,update_file_name):
    updateTimeStamp=time.time()
    tbat_file=open(tbat_file_name,'a', buffering=BUFFERING_SIZE)
    update_file=open(update_file_name,'r', buffering=BUFFERING_SIZE)
    for updateLine in update_file:
        updateLine='%10g,%s' %(updateTimeStamp,updateLine)
        # print updateLine
        tbat_file.write(updateLine)
    tbat_file.close()
    update_file.close()

if __name__=='__main__':
    bat_time_start=time.time()
    updateBAT(bat_file_name,update_file_name)
    bat_time=time.time()-bat_time_start
    print 'bat update time:'+str(bat_time)

    tbat_time_start=time.time()
    updateTBAT(tbat_file_name,update_file_name)
    tbat_time=time.time()-tbat_time_start
    print 'tbat update time:'+str(tbat_time)

    overhead=(bat_time)/tbat_time*100
    print 'overhead=%g%%' % (overhead)

