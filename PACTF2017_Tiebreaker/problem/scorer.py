from solution import solution
from incredible_hash import string_hash
from time import clock
import random

NUM_ROUNDS = 20000
pool = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ '

def random_string(length):
    string = ""
    for i in range(length):
        index = random.randrange(len(pool))
        string = string + pool[index:index+1]
    return string

def made_of_valid_chars(stri):
    for char in stri:
        if char not in pool:
            return False
    return True

def score():
    correct = 0.0
    total = 0.0
    time_total = 0.0
    for i in range(NUM_ROUNDS):
        string = random_string(random.randrange(24) + 8)
        final_hash = string_hash(string)
        cutoff_string = string[:random.randrange(len(string))]
        start = clock()
        given_text = solution(cutoff_string, final_hash)
        stop = clock()
        time_total = time_total + (stop - start)
        if given_text is not None and \
            made_of_valid_chars(given_text) and \
            string_hash(given_text) == final_hash and \
            len(given_text) <= 32 and \
            given_text.startswith(cutoff_string):
            correct = correct + 1        
            total = total + 1
    time = time_total / total
    print "time: " + str(time) + " // correct: " + str(correct) + " // total: " + str(total)
    score = (1.0 / time) * ((correct/total)**2)
    print "score: " + str(score)

score()
