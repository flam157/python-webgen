# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:41:48 2012

@author: flam
"""


import string
import copy,codecs,os
import re,datetime
    

lst_prop_init=[]
               
lst_prop_convert=[]             


plug_name='copy'


     

   
def plugin_change_lists(website):
    """
    function that can modify the whole website (before content generation)
    """
    pass        

def plugin_change_lists_post(website):
    """
    function that can modify the whole website (after content generation)
    """
    #print len(website.pagelist)

    website.log("Copy files")
    for pattern in website.config[plug_name]['list']:
        for files in glob.glob(website.srcdir+os.sep+pattern):
            file2=files.replace(website.srcdir,website.outdir)
            # copy only if modified or not exists
            if not os.path.isfile(file2):
                shutil.copy(files,file2)
            elif os.path.getmtime(file2)<os.path.getmtime(files):
                shutil.copy(files,file2)
                            
    


def plugin_return(config):
    """
    returns the plugin 
    """
    res=plug_name
    return res
    
    
    
    