import argparse
import os
from .core import Yorick
from uuid import uuid4

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
class Create_Skeleton (object):
	@staticmethod
	def arg_parser(parser):
		parser.add_argument('name')
	
	@staticmethod
	def run(yorick, args):
		s = yorick.get_skeleton("yorick.skeleton")
		vars = s.variables
		vars.skeleton_name.value = args.name
		vars.description.value = "Example description"
		vars.id.value = str(uuid4())
		path = os.path.sep.join((yorick.dir, '__default__', args.name))
		s.construct(vars, path)
		print "Your skeleton has been created at", path

@app.subcommand
class Construct (object):
	@staticmethod
	def arg_parser(parser):
		parser.add_argument('skeleton')
		parser.add_argument('path', nargs='?', default=None)
		
	@staticmethod
	def run(yorick, args):
		s = yorick.get_skeleton(args.skeleton)
		vars = s.variables
		# prompt
		cli_prompt(vars)	
		s.construct(vars, args.path)

def cli_prompt(varset):
	for v in varset.all_promptable():
		print v.prompt
		while True:
			try:
				v.value = raw_input(v.name + "> ")
			except ValueError as e:
				print "Error: " + e.message
			else:
				break
			
			