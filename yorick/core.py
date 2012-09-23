from os import path
import yaml

class Yorick (object):
	def __init__(self):
		self.dir = path.join(path.expanduser('~'), '.yorick')
	
	def get_closet(self, name):
		return Closet(self, name)
	
	def get_skeleton(self, name):
		namelist = name.split('.')
		if len(namelist) == 1:
			closet_name = '__default__'
			skeleton_name = name
		else:
			closet_name, skeleton_name = namelist
		return self.get_closet(closet_name).get_skeleton(skeleton_name)

class Closet (object):
	def __init__(self, yorick, name):
		self.yorick = yorick
		self.name = name
		if name = 'yorick':
			self.dir = path.join(path.dirname(__file__), 'closet')
		else:
			self.dir = path.join(yorick.dir, name)
	
	def get_skeleton(self, name):
		return Skeleton(self.yorick, self, name)

class Skeleton (object):
	def __init__(self, yorick, closet, name):
		self.yorick = yorick
		self.closet = closet
		self.name = name
		self.dir = path.join(closet.dir, name)
	
	@property
	def conf(self):
		if self.hasattr('_conf'):
			return self._conf
		
		with open(path.join(self.dir, '{}.yorick-conf'.format(self.name))) as f:
			self._conf = yaml.load(f.read)
		return self._conf
		
	def construct(self):
		"""Construct the skeleton in the current working directory"""