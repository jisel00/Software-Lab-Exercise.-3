
def sclist(self, data):

	if (self.last != None):
		return self.last

	# Creating the newnode temp
	temp = Node(data)
	self.last = temp

	# Creating the link
	self.last.next = self.last
	return self.last

