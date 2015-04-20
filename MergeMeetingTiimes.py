__author__ = 'JeredYang'

list = []
list.sort()


def combine_time(first_time, second_time):
    return first_time[0], second_time[1]


def merge_meeting_time(meeting_time_list):
    new_list = meeting_time_list
    new_list.sort(key=lambda x:x[0])
    result = []
    for index in range(len(new_list) - 1):
        if new_list[index][1] < new_list[index + 1][0]:
            result.append(new_list[index])
            result.append(new_list[index + 1])
        else:
            new_time = combine_time(new_list[index], new_list[index + 1])
            result.append(new_time)
        index += 2

    return result
