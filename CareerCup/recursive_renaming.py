'''
Created on Aug 17, 2015

@author: ljiang

Recursively renaming directory/file structures on a local file system
'''
import os

def recursive_renaming(mode,path,pattern):
    pass
    newnames=[]
    for root, dirs, files in os.walk(path,topdown=False):
        if mode=='dir':
            for dir in dirs:                
                if pattern in dir:
                    dirname=dir.replace(pattern,'',1)
                    newname=os.path.join(root,dirname)
                    os.rename(os.path.join(root,dir),newname)
                    #newnames.append(newname)
        elif mode=='file':
            for file in files:
                if pattern in file:
                    filename=file.replace(pattern,'',1)
                    newname=os.path.join(root,filename)
                    os.rename(os.path.join(root,file),newname)
                    #newnames.append(newname)
    for root, dirs, files in os.walk(path,topdown=True):
        if mode=='dir':
            for dir in dirs:
                newnames.append(os.path.join(root,dir))
        elif mode=='file':
            for file in files:
                newnames.append(os.path.join(root,file))
            
    return newnames