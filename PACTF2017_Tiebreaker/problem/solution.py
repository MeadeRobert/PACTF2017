# The code below is used to generate the maps that are hardcoded into the program.
# Hardcoding the maps takes longer to parse, possibly related to file size?
from incredible_hash import *
import itertools as it

# 126 is ord('~')
# not valid if hash_number < 32
def end_string(hash_number):
        passwd = ""
        passwd_number = 0

        # fill with ~'s until no more fit (greedy)
        while passwd_number < hash_number - 126:
                passwd += '~'
                passwd_number += 126
                # return endstring from existing table if possible
                if hash_number - passwd_number in end_strings:
                        return passwd + end_strings[hash_number - passwd_number]

        # handle special cases for last value
        last_value = hash_number - passwd_number        
        # if last_value < 32 use 2 separate chars to make value
        if last_value < 32:
                passwd = passwd[0:len(passwd)-1]
                last_value += 126
                if last_value % 2 == 0:
                        passwd += chr(last_value // 2) * 2
                else:
                        passwd += chr(last_value // 2) + chr(last_value // 2 + 1)
        # if last_value on [60, 62] use chars in valid range to make value
        elif last_value in xrange(60, 63):
                passwd = passwd[0:len(passwd)-1]
                last_value += 126
                passwd += chr(120) + chr(last_value - 120)
        # otherwise, add the appropriate character
        else:
                passwd += chr(hash_number - passwd_number)
                
        return passwd

# generate map of ending strings
end_strings = {}
for i in it.chain(xrange(32, 60), xrange(63, 4033)):
        end_strings[i] = end_string(i)
#print "end_strings =",end_strings
        
# generate map of hashes
hashes = {}
for i in it.chain(xrange(32, 60), xrange(63, 4033)):
        hash = hash_number(i)
        if hash in hashes:
                hashes[hash].append(i)
        else:
                hashes[hash] = [i]
#print "hashes =",hashes

                
def solution(cutoff_string, final_hash):
        passwd_number = sum(bytearray(cutoff_string))
        for hash_number in hashes[final_hash]:
                if hash_number - passwd_number in end_strings.keys():
                        return cutoff_string + end_strings[hash_number - passwd_number]
