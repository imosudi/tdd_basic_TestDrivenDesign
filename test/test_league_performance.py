import unittest
from app.league_performance import LeastGoalPerformer #import the class from target python application

class TddLeastGoalPerformer(unittest.TestCase):

	def setUp(self):
		self.inputFilename = LeastGoalPerformer()
		pass

	def test__return_inputFileIntegrity(self):
		inputFilename = LeastGoalPerformer()
		result = inputFilename.confirmFileIntergrity('football-league-results.txt')
		self.assertEqual('football-league-results.txt', result)
		pass





	"""docstring for TddLeastGoalPerformer"""
	'''def __init__(self, arg):
					super(TddLeastGoalPerformer, self).__init__()
					self.arg = arg'''


if __name__ == '__main__':
    unittest.main()