# -*- coding: utf-8 -*-
# @Author: Guoxuenan
# @Date:   2016-12-27 22:09:33
# @Last Modified by:   Guoxuenan
# @Last Modified time: 2017-05-19 15:50:14

# -*- coding: utf-8 -*-
import xmlrpclib
import time
import collections
import sys
# 获取所有进程信息
def getAllProcessInfo():
	processInfo=collections.OrderedDict()
	try:
		server=xmlrpclib.Server('http://localhost:9001/RPC2')
		count=1;
		for pro in server.supervisor.getAllProcessInfo():
			pro['start'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pro['start']))
			if pro['stop']!=0:
				pro['stop'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pro['stop']))
			pro['now'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pro['now']))
			processInfo[count]=pro
			count+=1
	except:
		info=sys.exc_info()
		print info[0],":",info[1]
	return processInfo
#关闭指定进程
def stopProcess(name):
	try:
		server=xmlrpclib.Server('http://localhost:9001/RPC2')
		for x in server.supervisor.getAllConfigInfo():
			if x['name']== name:
				if server.supervisor.getProcessInfo(name)['statename']=="RUNNING":
					return server.supervisor.stopProcess(name)
	except:
		info=sys.exc_info()
		print info[0],":",info[1]		
	return True

def startProcess(name):
	try:
		server=xmlrpclib.Server('http://localhost:9001/RPC2')
		for x in server.supervisor.getAllConfigInfo():
			if x['name']== name:
				if server.supervisor.getProcessInfo(name)['statename']=="STOPPED":
					return server.supervisor.startProcess(name)
	except:
		info=sys.exc_info()
		print info[0],":",info[1]				
	return True

def startAllProcesses():
	try:
		server=xmlrpclib.Server('http://localhost:9001/RPC2')
		server.supervisor.startAllProcesses()
	except:
		info=sys.exc_info()
		print info[0],":",info[1]		
	return True

def stopAllProcesses():
	try:
		server=xmlrpclib.Server('http://localhost:9001/RPC2')
		server.supervisor.stopAllProcesses()
	except:
		info=sys.exc_info()
		print info[0],":",info[1]		
	return True
#  @param string name         the name of the process (or 'group:name')
#  @param int offset          offset to start reading from
#  @param int length          maximum number of bytes to return
#  @return array result       [string bytes, int offset, bool overflow]
# def getNewlog(name,start):
# 	try:
# 		server=xmlrpclib.Server('http://localhost:9001/RPC2')
# 		# print server.supervisor.tailProcessStderrLog(name,offset,length)
# 		# length=getTotalBytes(name)-start
# 		length=1000
# 		# print "==========",getTotalBytes(name),start,length
# 		return server.supervisor.readProcessLog(name,start,length)
# 	except:
# 		info=sys.exc_info()
# 		print info[0],":",info[1]		
# 		return None

# def getTotalBytes(name):
# 	try:
# 		server=xmlrpclib.Server('http://localhost:9001/RPC2')
# 		# print server.supervisor.tailProcessStderrLog(name,offset,length)
# 		print server.supervisor.getAllConfigInfo()
# 		return server.supervisor.tailProcessLog(name,0,0)[1]
# 	except:
# 		info=sys.exc_info()
# 		print info[0],":",info[1]		
# 		return -1

# count=getTotalBytes("concentratorback")
# print count
# while True:
# 	log=getNewlog("concentratorback",count)
# 	if(log!=None):
# 		print log.encode("utf-8"),
# 		count=getTotalBytes("concentratorback")
# 	time.sleep(1)
 
	

# stopAllProcesses()
# print getAllProcessInfo()
# print stopProcess('mytest')
# print startProcess('mytest')
# supervisor.stopProcess
# for x in server.system.listMethods():
    # print "## "+x+"\n\t"+server.system.methodHelp(x)
# for x in server.supervisor.getAllConfigInfo():
    # print x 
# for x in server.supervisor.getAllProcessInfo():
#     x['start'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(0))
#     print x 
# '''{'now': 1482462161, 
# 'group': 'aout', 
# 'description': 'Dec 22 10:31 PM',
# 'pid': 0, 
# 'stderr_logfile': '/home/wangyu/myspace/Concentrator/datalog/testsupervisor/aout.stderr.log',
# 'stop': 1482417079, 
# 'statename': 'STOPPED', 
# 'start': 1482417068, 
# 'state': 0,
# 'stdout_logfile': '/home/wangyu/myspace/Concentrator/datalog/testsupervisor/aout.stdout.log', 
# 'logfile':        '/home/wangyu/myspace/Concentrator/datalog/testsupervisor/aout.stdout.log', 
# 'exitstatus': -1, 
# 'spawnerr': '', 
# 'name': 'aout'
# }'''
# print server.supervisor.getAllProcessInfo()
# print "+++++++++++++++++++++++++"
# print server.supervisor.getIdentification()
# print server.supervisor.getPID()
# print server.supervisor.getProcessInfo('mytest')
# print server.supervisor.getState()
# print server.supervisor.readMainLog(0,0)
# print "==========================1"
# print server.supervisor.readProcessLog('mytest',0,0)
# print "==========================2"
# print server.supervisor.readProcessStderrLog('mytest',0,0)
# print "==========================3"
# print server.supervisor.readProcessStdoutLog('mytest',0,0)
# server=xmlrpclib.Server('http://localhost:9001/RPC2')
# for x in server.supervisor.getAllConfigInfo():
# 	print x
