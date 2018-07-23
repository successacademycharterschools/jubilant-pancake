#!/usr/bin/env python
#
import unittest
from service import getEditDistance

class TestgetEditDistance(unittest.TestCase):

	# Testing str1 & str2 being equal
	def testStrsEqual(self):
		self.assertEqual('abc', 'abc', 'Strings aren\'t equal')
		self.assertNotEqual('abc', 'eddf', 'Strings aren\'t equal')

		self.assertEqual('Google', 'Google')
		self.assertNotEqual('Apple', 'Amazon')

		# Checking if case-insensitive
		str1 = 'Microsoft'
		str2 = 'microsoft'
		self.assertEqual(str1.lower(), str2.lower())

		self.assertEqual('737525186', '737525186')
		self.assertNotEqual('78365871', '469841321654')


	# Testing one str is blank
	def testStrBlank(self):
		# test str1 is blank
		# Test 1
		answer = getEditDistance('', 'abc')
		self.assertEqual(answer, 3)
		self.assertNotEqual(answer, 0)

		answer = getEditDistance('', 'Spock & McCoy')
		self.assertEqual(answer, 13)
		self.assertNotEqual(answer, 0)

		answer = getEditDistance('', '2392373354')
		self.assertEqual(answer, 10)
		self.assertNotEqual(answer, 0)

		# test str2 is blank
		answer = getEditDistance('abcdef', '')
		self.assertEqual(answer, 6)
		self.assertNotEqual(answer, 0)

		answer = getEditDistance('Riker & Troi', '')
		self.assertEqual(answer, 12)
		self.assertNotEqual(answer, 0)

		answer = getEditDistance('867-5309', '')
		self.assertEqual(answer, 8)
		self.assertNotEqual(answer, 7)

		answer = getEditDistance('83212991545', '')
		self.assertEqual(answer, 11)
		self.assertNotEqual(answer, 0)


	# Comparing two strings
	def test2Strings(self):
		answer = getEditDistance('GUMBO', 'GAMBOL')
		self.assertEqual(answer, 2)
		self.assertNotEqual(answer, 5)

		answer = getEditDistance('abcdef', 'azced')
		self.assertEqual(answer, 3)
		self.assertNotEqual(answer, 5)

		answer = getEditDistance('sZEVTXzOTP4dXbO6', 'sZEVNXjfdr4dXtpK')
		self.assertEqual(answer, 8)
		self.assertNotEqual(answer, 3)

		answer = getEditDistance('30355', '30111')
		self.assertEqual(answer, 3)
		self.assertNotEqual(answer, 10)

		str1 = 'Hello my name is Inigo Montoya, you\' killed my father.  Prepare to die'
		str2 = 'Hello my name is Inigo Montoyia, you: killed my father.  Prepare to die'
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 2)
		self.assertNotEqual(answer, 3)

		###################################################
		# Test 1
		###################################################
		str1 = '   POMAx42YhZqJU9uhT5H7nk'
		str2 = '  POMAx42YhZqJU9uhT5H7nk   '

		# Case sensitive
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 4)
		self.assertNotEqual(answer, 0)

		# Case insensitive
		answer = getEditDistance(str1.strip(), str2.strip())
		self.assertEqual(answer, 0)
		self.assertNotEqual(answer, 4)

		###################################################
		# Test 2
		###################################################
		str1 = '   9mZhNQXTm5ad9fEpmlK  '
		str2 = '9mZhNQXTm5ad9fEpmlK   '

		# Case sensitive
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 4)
		self.assertNotEqual(answer, 0)

		# Case insensitive
		answer = getEditDistance(str1.strip(), str2.strip())
		self.assertEqual(answer, 0)
		self.assertNotEqual(answer, 4)


		###################################################
		# Test 3
		###################################################
		str1 = 'hO3jmYr5Kps31uY9ei5HCsmitUFAKVIOankrBsCNGsJzDNpUDmNNWlBw6Dklc7uJwrM7dBdfbFprDc5aDdK348YHVFyDVdzxFO5k5lmLXxjRNcolWewdDrwF7MEI2mVLosVxLTH7a3MnqRsWTnp27D'
		str2 = 'hO3jmYr5Kps31uY9ei5HaF4aIKN5soKr2l3BiujaaBVmlJ5FzaMDap5CKpRWD6WTnprMs'

		# Case sensitive
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 112)
		self.assertNotEqual(answer, 0)

		# Case insensitive
		answer = getEditDistance(str1.strip(), str2.strip())
		self.assertEqual(answer, 112)
		self.assertNotEqual(answer, 4)

		###################################################
		# Test 4
		###################################################		
		str1 = 'VFBclIi74V7ieMgt  '
		str2 = 'VFBclIi74V7ieMgt   '

		# Case sensitive
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 1)
		self.assertNotEqual(answer, 0)

		# Case insensitive
		answer = getEditDistance(str1.strip(), str2.strip())
		self.assertEqual(answer, 0)
		self.assertNotEqual(answer, 4)

		###################################################
		# Test 4
		###################################################		
		str1 = 'So many books, so little time.' # from Frank Zappa
		str2 = 'A friend is someone who knows all about you and still loves you.' # Elbert Hubbard

		# Case sensitive
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 49)
		self.assertNotEqual(answer, 0)

		# Case insensitive
		answer = getEditDistance(str1.strip(), str2.strip())
		self.assertEqual(answer, 49)
		self.assertNotEqual(answer, 4)


		###################################################
		# Test 5
		###################################################		
		str1 = 'AMADEO'
		str2 = 'ANDREA'

		# Case sensitive
		answer = getEditDistance(str1, str2)
		self.assertEqual(answer, 4)
		self.assertNotEqual(answer, 0)

		# Case insensitive
		answer = getEditDistance(str1.strip(), str2.strip())
		self.assertEqual(answer, 4)
		self.assertNotEqual(answer, 6)


if __name__ == '__main__':
	unittest.main()