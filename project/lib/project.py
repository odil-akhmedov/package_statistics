from process import Process
import sys
import csv
# If you don't want to use virtualenv, edit the following line
# sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
import pandas as pd
import os
import urllib

class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def print_arg(self):
        return self.options.known.arch

    def run_command(self):
        arch = self.options.known.arch
        url = 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-' + arch + '.gz'
        # print url

        # # ********************** #
        # Downloading the file
        # Python libraries handle large size file downloads poorly
        # Instead, we will use Linux to handle download and extract
        file_path = "project/files/archive.gz"
        archive_path = "project/files/archive"
        command = "wget -O " + file_path + " " + url
        os.system(command)

        command = "gzip -d -k " + file_path
        os.system(command)

        # ********************** #
        # Reading the file
        # We will use python's csv reader to read and transform the file
        # Then we will use Pandas to get the desired data

        # Due to non-standard format of the data, we really are interested 
        # in the last column data
        with open(archive_path, "r", ) as fp:
            reader = csv.reader(fp, delimiter=' ')
            # Grabbing the last column, split the comma-separation into newline separation
            rows = [ x[-1:][0].replace(',','\n') for x in reader] 
            
            # Saving into pandas' data frame
            data_cols = ['packages']
            df = pd.DataFrame(rows, columns=data_cols)
            print df['packages'].value_counts().head(10)

        