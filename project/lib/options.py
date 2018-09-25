from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        # overrides usage that is by default something like:
        # usage: PROG [-h] [--foo [FOO]] bar [bar ...]
        usage = './bin/project'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('arch', help='Provide architecture code (e.g. amd64, mips, udeb-i386 etc)')

    def parse(self, args=None):
        # parse known args, returns a Namespace object
        # unknown args are ignored
        # Parse known args returns (Namespace_of_known, list_of_unknown)
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if len(self.unknown) != 0:
            print '*WARNING* Unknown args received: '+repr(self.unknown)