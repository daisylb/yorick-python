class _RendererLibrary (object):
	def __init__(self):
		self.renderers = {}
	
	def add(self, ext):
		"""Decorator to add a renderer"""
		def inner(fun):
			self.renderers[ext] = fun
			return fun
		return inner
	def __getitem__(self, key):
		return self.renderers[key]

library = _RendererLibrary()

@library.add('t')
def python_string_formatting(file, vars):
	return file.format(**vars)