# Import Python packages 
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv

def processing_csv(filepath):
    """
    Description: This function used to read csv files and create event file to insert to csv
    Arguments:  
        filepath: log data file path. 
    Returns:
        None
    """
    #--------------------------
    # create list of filepath
    #--------------------------
    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root,'*'))
        
    #------------------------------------------
    # Processing the files to create 
    # the data file csv that will be used 
    # for Apache Casssandra tables
    #------------------------------------------
    
    full_data_rows_list = []
    for f in file_path_list:
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            csvreader = csv.reader(csvfile) 
            next(csvreader)   
            for line in csvreader:
                full_data_rows_list.append(line) 
    
    #----------------------------------------
    # creating a smaller event data csv file 
    # called event_datafile_full csv 
    # that will be used to insert data into the
    # Apache Cassandra tables
    #----------------------------------------
    
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
        
    