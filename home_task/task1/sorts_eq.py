import random
import timeit


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def timsort(arr):
    return sorted(arr)


def run_time_test(sort_func, data):
    return timeit.timeit(lambda: sort_func(data), number=1)


def generate_data(size):
    return [random.randint(1, size) for _ in range(size)]


def main():
    sizes = [100, 500, 1000, 5000, 10000]
    print(f"{'Size':>6} | {'Insertion':>10} | {'Merge':>10} | {'Timsort':>10}")
    print("-" * 45)

    for size in sizes:
        data = generate_data(size)
        time_insert = run_time_test(insertion_sort, data)
        time_merge = run_time_test(merge_sort, data)
        time_timsort = run_time_test(timsort, data)

        print(f"{size:>6} | {time_insert:>10.4f} | {time_merge:>10.4f} | {time_timsort:>10.4f}")


if __name__ == "__main__":
    main()
