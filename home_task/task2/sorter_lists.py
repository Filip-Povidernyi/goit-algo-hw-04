import random
# from datetime import datetime


# def wrapper(func):
#     def inner(*args, **kwargs):
#         start_time = datetime.now()
#         result = func(*args, **kwargs)
#         end_time = datetime.now()
#         print(f"Execution time: {end_time - start_time}")
#         return result
#     return inner


def merge(list1, list2):
    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


# @wrapper
def merge_k_lists(lists):

    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]

    ordered_list = []

    for k in range(0, len(lists), 2):

        ordered_list.append(
            merge(lists[k], lists[k + 1] if k + 1 < len(lists) else []))

    return merge_k_lists(ordered_list)


if __name__ == "__main__":

    quantity = random.randint(0, 20)
    lists = []
    for i in range(quantity):
        lists.append(sorted([random.randint(1, 100)
                             for _ in range(random.randint(0, 20))]))
    print(f"Lists: {lists}\nin count: {quantity}")
    print(merge_k_lists(lists))
