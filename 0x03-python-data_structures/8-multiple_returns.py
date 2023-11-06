#!/usr/bin/python3

def multiple_returns(sentence):
    # if len(sentence) == 0:
        # return 0, None
    return len(sentence), None if len(sentence) == 0 else sentence[0]
