import sys

from lib import Project
from lib import Options

def run_project(args):
    options = Options()
    options.parse(args[1:])

    project = Project(options)

    print 'Archirtecture chosen:', project.print_arg()
    

if __name__ == '__main__':
    run_project(sys.argv)