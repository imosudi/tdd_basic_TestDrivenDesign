class LeastGoalPerformer(object):
	filename = 'football-league-result.txt'

	'''def confirmFileType(self, filename):
					if filename.endswith('.txt')
					pass'''
	def confirmFileIntergrity():
		if os.path.isfile(filename):
			return filename
		pass




	"""docstring for LeastGoalPerformer"""
	def __init__(self, arg):
		super(LeastGoalPerformer, self).__init__()
		self.arg = arg
		