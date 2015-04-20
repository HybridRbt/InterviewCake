__author__ = 'JeredYang'

def combine_item(item_list):
    first_item = 1000
    second_item = 0

    for each_item in item_list:
        if each_item[1] > second_item:
            second_item = each_item[1]

        if each_item[0] < first_item:
            first_item = each_item[0]

    return first_item, second_item

def merge_meeting_time(meeting_time_list):
    new_list = sorted(meeting_time_list, key=lambda x:x[0])
    result = []

    index1 = 0
    index2 = 1
    while index1 < len(new_list) and index2 < len(new_list):
        if new_list[index1][1] < new_list[index2][0]:
            result.append(new_list[index1])
            #result.append(new_list[index + 1])
        else:
            combine_list = []
            current_item = new_list[index1]
            combine_list.append(current_item)
            while index2 < len(new_list) and current_item[1] >= new_list[index2][0]:
                combine_list.append(new_list[index2])
                current_item = new_list[index2]
                index2 += 1
            new_item = combine_item(combine_list)
            result.append(new_item)
        index1 = index2
        index2 = index1 + 1

    return result
