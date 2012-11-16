"""Objects representing yorick's three main types of entity: the Yorick app, closets and skeletons."""

import os
from re import match
from shutil import copy
import yaml
from .renderers import library as renderer_library

class Yorick (object):
	def __init__(self):
		self.dir = os.path.join(os.path.expanduser('~'), '.yorick')
	
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
	"""Represents a collection of skeletons."""
	def __init__(self, yorick, name):
		self.yorick = yorick
		self.name = name
		if name == 'yorick':
			self.dir = os.path.join(os.path.dirname(__file__), 'closet')
		else:
			self.dir = os.path.join(yorick.dir, name)
	
	def get_skeleton(self, name):
		return Skeleton(self.yorick, self, name)

class Skeleton (object):
	"""Represents a project template."""
	def __init__(self, yorick, closet, name):
		self.yorick = yorick
		self.closet = closet
		self.name = name
		self.dir = os.path.join(closet.dir, name)
	
	@property
	def conf(self):
		if hasattr(self, '_conf'):
			return self._conf
		
		with open(os.path.sep.join((self.dir, '-yorick-meta', 'config.yml'))) as f:
			self._conf = yaml.load(f)
		return self._conf
			
	def construct(self, variables, destination_root=None):
		"""Construct the skeleton in `destination_root`, or the cwd if not given."""
		for template_path, dirs, files in os.walk(self.dir):
			
			# path relative to the skeleton root
			relative_path = template_path.replace(self.dir, '', 1)
			if relative_path.startswith(os.sep):
				relative_path = relative_path.replace(os.sep, '', 1)
			
			# determine the destination path for this directory
			destination_path = relative_path.split(os.sep)
			for i, el in enumerate(destination_path):
				# render each path component's name
				destination_path[i] = self.__render_pathname(el, variables)
			# prepend the destination root to the relative dest path
			if destination_root is not None:
				destination_path.insert(0, destination_root)
			destination_path = os.path.sep.join(destination_path)
			
			# skip over any directories called -yorick-meta
			for i, dir in enumerate(dirs):
				if dir == '-yorick-meta':
					del dirs[i]
			
			# make sure the directory exists
			if destination_path != '':
				os.makedirs(destination_path)
			
			# process files
			for file in files:
				matchobj = match(r'(.*)\.yorick-.+', file)
				if matchobj:
					with open(os.path.join(template_path, file)) as infile:
						original_content = infile.read()
						rendered_content = renderer_library['t'](original_content, variables)
					file_outname = matchobj.group(1)
					with open(os.path.join(destination_path, file_outname), 'w') as outfile:
						outfile.write(rendered_content)
				else:
					copy(os.path.join(template_path, file), os.path.join(destination_path, file))
	
	def __render_pathname(self, pathname, variables):
		if pathname.endswith('.yorick-literal'):
			# reverse, do the replacement, put back again
			return pathname[::-1].replace('.yorick-literal'[::-1], '', 1)[::-1]
		else:
			# perform path name substitution
			return pathname.format(**variables)