*Package Statistics*
## Author: Odiljon (Odil) Akhmedov


After analyzing https://wiki.debian.org/DebianRepository/Format?action=show&redirect=RepositoryFormat#A.22Contents.22_indices and the content indices file format,
I came up with the following solution.

I created a python command line utility with only one argument expected; the architecture code (amd64, mips etc).
I structured the project in a way that I separated command line options hanldin, program logic, and processing.

I borrowed the structure from one of the git repos, it's like a boilerplate for Python projects.
This program utilizes virtual env to save all the neccessary packages locally. I really didn't want to do that, but one of the libraries I was using (Pandas) required this type of special treatment.

I ended up using Pandas, since size of the extacted file can be pretty big, and using standard python file reading in line-by-line mode can potentially hog up IO resources.

After the user runs the command, the script grabs the arch code, applies it to a predefined URL structure like so:

```
project/lib/project.py 
...
url = 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-' + arch + '.gz'
...

```

The script then downloads the archive file and extracts the content index file. 
I decided to use Linux commands instead of something like urllib, again because the sizes are considerable, the extracted files is close to 500 MB.


```
command = "wget -O archive.gz " + url
os.system(command)

command = "gzip -d -k archive.gz"
os.system(command)
```

Lastly, python's csv reader reads the extracted file, grabs the last columns values, solit the comma separation and loads them into Pandas data frame.
Then, we are grabbing the top ten packages. 

```
        with open("archive", "r", ) as fp:
            reader = csv.reader(fp, delimiter=' ')
            # Grabbing the last column, split the comma-separation into newline separation
            rows = [ x[-1:][0].replace(',','\n') for x in reader] 
            
            # Saving into pandas' data frame
            data_cols = ['packages']
            df = pd.DataFrame(rows, columns=data_cols)
            print df['packages'].value_counts().head(10)
```

***HOW TO USE***

1. Download, extact the project, navigate to 'package_statistics' directory
$ unzip package_statistics.zip
$ cd package_statistics/
2. Install virtualenv and configure virtualenv

```
$ pip install virtualenv 
$ virtualenv .
```

3. "Activate" the virtualenv 
```
$ source bin/activate
``` 

4. Install pandas, wheel
```
$ pip install pandas wheel
```

5. Run the command
```
$ bin/package_statistics mips
```
Use amd64, mips or other architecture codes

6. "Deactivate" virtualenv
```
$ deactivate
```

** If you are experiencing any difficulties: **
 1. Exit/deactivate virtualenv
 2. Uncomment and edit line 5 in "project/lib/project.py". Change the path to your local python local packages path"
```
  5 sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
```
 3. Run "$ pip install pandas wheel

***THINGS TO IMPROVE***

You can infinitely improve your code (c)

1. There is a minimum validations in place. Ideally, we need to check if the file exists.
2. More sophisticated arguments handling.
3. Testing. 
4. Performance tuning.
5. More general solution. 
6. Get rid of the virtualenv
