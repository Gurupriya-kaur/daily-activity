from typing import List, TypeVar

T = TypeVar("T")

THRESHOLD = 16   # switch to insertion sort below this size


def _insertion_sort(arr: List, lo: int, hi: int) -> None:
    for i in range(lo + 1, hi + 1):
        key = arr[i]
        j = i - 1
        while j >= lo and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def _merge(arr: List, lo: int, mid: int, hi: int) -> None:
    left = arr[lo:mid + 1]
    right = arr[mid + 1:hi + 1]
    i = j = 0
    k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]; i += 1
        else:
            arr[k] = right[j]; j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]; i += 1; k += 1
    while j < len(right):
        arr[k] = right[j]; j += 1; k += 1


def _merge_sort(arr: List, lo: int, hi: int) -> None:
    if hi - lo < THRESHOLD:
        _insertion_sort(arr, lo, hi)
        return
    mid = (lo + hi) // 2
    _merge_sort(arr, lo, mid)
    _merge_sort(arr, mid + 1, hi)
    _merge(arr, lo, mid, hi)


def merge_sort(arr: List) -> List:
    """Return a new sorted list; does not mutate the input."""
    result = list(arr)
    if len(result) > 1:
        _merge_sort(result, 0, len(result) - 1)
    return result
