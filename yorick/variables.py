class VariableSet (object):
    _vars = {} # list of variables
    
    def __init__(self, spec):
        self._vars = {}
        for name, props in spec.iteritems():
            v = Variable(name, props)
            self._vars[name] = v
    
    def __repr__(self):
        reprs = ", ".join([repr(x) for x in self])
        return "VariableSet({})".format(reprs)
    
    def __getitem__(self, name):
        return self._vars[name]
    
    __getattr__ = __getitem__
    
    def __iter__(self):
        for _, var in self._vars.iteritems():
            yield var
    
    def __contains__(self, item):
        return item in self._vars
    
    def all_empty(self):
        return (var for var in self if var.value is None)
    
    def all_mandatory(self):
        return (var for var in self if var.default is None)
    
    def all_promptable(self):
        return (var for var in self if var.prompt is not None and var.value is None)
    
    def as_dict(self):
        return {v.name: v.value for v in self}

class Variable (object):
    name = '' # variable name
    _props = {} # variable properties
    _value = None
    
    def __init__(self, name, props):
        self.name = name
        self._props = props
    
    def __repr__(self):
        if self.value is not None:
            return "Variable({}, type={}, value={})".format(self.name, self.type, self.value)
        else:
            return "Variable({}, type={})".format(self.name, self.type)
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, dirty_value):
        self._value = self.coerce(dirty_value)
    
    @value.deleter
    def value(self):
        self._value = None
        
    @property
    def prompt(self):
        """The message to present to the user when prompting for this variable.
        
        Returns ``None`` if the user shouldn't be prompted.
        """
        return self._props.get('prompt')
    
    @property
    def default(self):
        """The default value if one isn't supplied.
        
        Returns ``None`` if the variable is mandatory.
        """
        return self._props.get('default')
    
    @property
    def type(self):
        """The type.
        
        Returns either ``'string'``, ``'boolean'``, ``'integer'`` or ``'decimal'``.
        """
        
        t = self._props.get('type', 'string')
        if t in ('str', 'string', 's'): return 'string'
        if t in ('bool', 'boolean', 'b'): return 'boolean'
        if t in ('integer', 'int', 'i'): return 'integer'
        if t in ('decimal', 'float', 'number', 'd'): return 'decimal'
        raise ValueError("{} has an invalid type {}".format(self.name, t))
    
    def coerce(self, value):
        """Coerce a value to the appropriate type.
        
        Raises ``ValueError`` if the value is invalid.
        """
        
        t = self.type
        if t == 'string':
            return str(value)
        if t == 'integer':
            return int(value)
        if t == 'decimal':
            return float(value)
        if t == 'boolean':
            yes = ('yes', 'y', 'true', 't', 'ok', 'okay')
            no = ('no', 'n', 'false', 'f')
            if type(t) == str:
                v = value.lower()
                if v in yes:
                    return True
                elif v in no:
                    return False
                else:
                    raise ValueError("{} isn't a yes/no value".format(value))
            else:
                return bool(value)