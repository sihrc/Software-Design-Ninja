class Student (object):
  def __init__(self, name="", email="", user="", **kwargs):
    self.indexes = ["name", "email", "user"]

    self.name = name
    self.email = email
    self.user = user

    if kwargs is not None:
      for key, value in kwargs.iteritems():
        self.indexes.append(key)
        self.key = value

  def __str__(self):
    return "%s, Github handle: %s" % (self.name, self.user)

  def __repr__(self):
    return self.__str__()

  @property
  def student_dict(self):
    return { attr : getattr(self, attr) for attr in self.indexes }