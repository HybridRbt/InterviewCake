__author__ = 'JeredYang'

import MergeMeetingTiimes as mmt

def testMerge():
    meeting_list = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 8), (10, 12), (9, 10)]
    #meeting_list = [(1, 5), (2, 3)]
    #meeting_list = [(1, 10), (2, 6), (3, 5), (7,9)]
    print "Original list: \n" + str(meeting_list)
    condensed_list = mmt.merge_meeting_time(meeting_list)
    assert type(condensed_list) == list
    assert condensed_list == [(0, 8), (9, 12)]
    #assert condensed_list == [(1, 5)]
    #assert condensed_list == [(1, 10)]
    print "Condensed list: \n" + str(condensed_list)

testMerge()