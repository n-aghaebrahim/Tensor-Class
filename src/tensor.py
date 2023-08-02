class Tensor():

  def __init__(self, data, shape):
    self.data = data
    self.shape = shape
    self.tensor = None

  def add_zeros(self):
    size = 1
    new_data = self.data
    for i in self.shape:
      size = size * i
    length = len(self.data)
    if length < size:
      new_data.extend([0]*(size-length))
    return new_data

  def group_data(self, data, size):
    length = len(data)
    grouped = []
    i = 0
    while (i+size) <= length:
      grouped.append(data[i: i+size])
      i += size 
    return grouped

  def shape_data(self):
    if not self.shape:
      self.tensor = []
      #print (self.tensor)
      return

    new_data = self.add_zeros()
    for i in reversed(self.shape):
      new_data = self.group_data(new_data, i)
      #print (new_data)
    self.tensor = new_data[0] #Extract the first element which is a list whose length is shape[0]
    print (self.tensor)
