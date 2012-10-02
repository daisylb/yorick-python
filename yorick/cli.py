import argparse
from .core import Yorick

class _CliApp (object):
	def __init__(self):
		self.cmds = {}
		
	def subcommand(self, cls):
		self.cmds[cls.__name__.lower().replace('_', '-')] = cls
		return cls
	
	def arg_parser(self):
		parser = argparse.ArgumentParser(prog='yorick', description='Builds skeletons.')
		# global options go here
		
		subparsers = parser.add_subparsers(dest='subcommand')
		for k, v in self.cmds.iteritems():
			subparser = subparsers.add_parser(k)
			v.arg_parser(subparser)
		return parser
	
	def run(self, *argv):
		if len(argv) == 0:
			import sys
			argv = sys.argv
		
		args = self.arg_parser().parse_args(argv[1:])
		
		y = Yorick()
		
		# call subcommand
		self.cmds[args.subcommand].run(y, args)

app = _CliApp()

@app.subcommand
class Construct (object):
	@staticmethod
	def arg_parser(parser):
		parser.add_argument('skeleton')
		
	@staticmethod
	def run(yorick, args):
		s = yorick.get_skeleton(args.skeleton)
		
		# prompt for values
		values = {}
		for name, prefs in s.conf['variables'].iteritems():
			print prefs['prompt']
			values[name] = raw_input(name + '> ')
		
		s.construct(values)