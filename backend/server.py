"""This flask web server takes two arguments, val1 and val2 as strings.
Then it computes the distance between the two character by character"""

import unittest
from flask import Flask, jsonify, request
APP = Flask(__name__)

@APP.route("/")
def hello():
    """For this simple code test, we just need one endpoint for the front end to hit"""
    val_one = request.args.get('val1')
    val_two = request.args.get('val2')
    result = compute_distance(val_one, val_two)
    response = jsonify({'result':result})
    # for a code test, just let cors through.
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def compute_distance(val_one, val_two):
    """Compute the distance, char by char, between the two strings.
    This assumes that they are not null."""
    #to be returned
    op_count = 0

    #turn strings into lists of characters to be worked with
    val_one_list = list(val_one)
    val_two_list = list(val_two)

    #the loop below is a bit easier when you know which is bigger
    bigger_list = val_two_list
    smaller_list = val_one_list
    if len(val_one_list) > len(val_two_list):
        bigger_list = val_one_list
        smaller_list = val_two_list

    for i, small_list_item in enumerate(smaller_list):
        if i < len(bigger_list):
            if small_list_item != bigger_list[i]:
                op_count += 1
    op_count += (len(bigger_list) - len(smaller_list))
    return op_count


class TestComputeDistance(unittest.TestCase):
    """ a simple class for testing the compute distance method used by the server"""
    def test_compute_distance(self):
        """ a simple couple test cases for the compute distance method."""
        self.assertEqual(compute_distance("test", "test"), 0)
        self.assertEqual(compute_distance("", ""), 0)
        self.assertEqual(compute_distance("12345", "123456"), 1)
        self.assertEqual(compute_distance("123456", "12345"), 1)
