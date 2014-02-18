class Student (object):
  def __init__(self, **kwargs):
    self.indexes = kwargs.keys()

    if kwargs is not None:
      for key, value in kwargs.iteritems():
        setattr(self, key, value)

  def __get(self, attrname):
    '''returns the model's attribute with attrname'''
    try:
      return getattr(self, attrname)
    except AttributeError:
      raise Exception("No such attribute exists. Current attributes are:", self.indexes)

  def __str__(self):
    return "%s, %s, Github handle: %s" % (self.__get('last'), self.__get('first'), self.__get('github'))

  def __repr__(self):
    return self.__str__()

  @property
  def student_dict(self):
    return { attr : self.__get(attr) for attr in self.indexes }

  def get_group(self):
    # not supported
    return self.__get('group')

  @property
  def user(self):
    return self.__get('github')

  @property
  def name(self):
    return self.__get('first') + ' ' + self.__get('last')