import sys

from lib import Project
from lib import Options

def run(args):
    options = Options()
    options.parse(args[1:])

    project = Project(options)

    print 'Architecture chosen:', project.print_arg()
    project.run_command()

if __name__ == '__main__':
    run(sys.argv)