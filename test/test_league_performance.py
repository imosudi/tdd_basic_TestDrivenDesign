import unittest


class TddLeastGoalPerformer(unittest.Testcase):

	def setUp(self):
		self.inputFilename = LeastGoalPerformer()
		pass

	def test__inputFileIntegrity(self):
		inputFilename = LeastGoalPerformer()
		result = inputFilename.confirmFileIntergrity('football-league-result.txt')
		self.assertEqual('football-league-result.txt', result)
		pass





	"""docstring for TddLeastGoalPerformer"""
	def __init__(self, arg):
		super(TddLeastGoalPerformer, self).__init__()
		self.arg = arg
