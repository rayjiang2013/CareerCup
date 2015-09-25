'''
Created on Aug 17, 2015

@author: ljiang
'''
import pytest

import recursive_renaming
import os
import shutil
@pytest.fixture(scope="function",params=['./files'])
def config_test_recursive_renaming(request):
    try:
        print "setup: create file directories"
        folder_list=['/test1/','/test2/','/test1/test3/']
        file_list=['/test1/test1.txt','/test1/test3/test2.txt']
        for drt in folder_list:
            drt = request.param+drt
            if not os.path.exists(drt):
                os.makedirs(drt)
        for fname in file_list:
            fname=request.param+fname
            with open(fname,'w') as f:
                f.write('this is for test purpose')
        def fin():
            print "teardown: clean up all created files"
            shutil.rmtree(request.param)
        request.addfinalizer(fin)
    except Exception,details:
        print Exception,details
        
    
@pytest.mark.parametrize("mode,path,pattern,expected",[('dir','./files','tes',['./files/t1','./files/t2','./files/t1/t3'])])
def test_recursive_renaming_dir(config_test_recursive_renaming,mode,path,pattern,expected):
    assert recursive_renaming.recursive_renaming(mode,path,pattern)==expected
    
@pytest.mark.parametrize("mode,path,pattern,expected",[('file','./files','tes',['./files/test1/t1.txt','./files/test1/test3/t2.txt'])])
def test_recursive_renaming_file(config_test_recursive_renaming,mode,path,pattern,expected):
    assert recursive_renaming.recursive_renaming(mode,path,pattern)==expected
    