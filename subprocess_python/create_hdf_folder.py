#!/usr/bin/python

import subprocess
from subprocess import Popen
import sys

def hadoop_new_folder(path):
    #the parameter path must start with the simbol /, e.x /path
    full_command = 'hadoop dfs -mkdir '+ path
    p = Popen(full_command , shell=True)
    p.wait()
    p = Popen('hadoop dfs -ls /' , shell=True)
    output = p.stdout
    return output

def hadoop_delete_folder(path):
    #the parameter path must start with the simbol /, e.x /path
    full_command = 'hadoop dfs -rm -r '+ path
    p = Popen(full_command , shell=True)
    p.wait()
    p = Popen('hadoop dfs -ls /' , shell=True)
    output = p.stdout
    return output

def hadoop_upload_data(path,name_file):
    full_command = 'hadoop dfs -put '+ path + '/' + name_file
    p = Popen(full_command , shell=True)
    p.wait()

def hadoop_download_data(path,name_file):
    full_command = 'hadoop dfs -get '+ path + '/' + name_file 
    p = Popen(full_command , shell=True)
    p.wait()

#p = Popen('hadoop dfs -mkdir /test_delete', shell=True)
#p.wait()
#p = Popen('hadoop dfs -ls /',shell=True)
#output = p.stdout
#print(output)


def main():
    print("python main function folder name", sys.argv[1])
    #str = '/test_delete'
    str = sys.argv[1]
    hadoop_new_folder(str)

if __name__ == '__main__':
   main()
