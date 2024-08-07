import random
# Вузол однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Реверсування списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Перевірка на відсортованість списку
def is_sorted(head):
    current = head
    while current and current.next:
        if current.data > current.next.data:
            return False
        current = current.next
    return True

# Злиття двох відсортованих списків
def merge_two_sorted_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data <= list2.data:
        merged_head = list1
        merged_head.next = merge_two_sorted_lists(list1.next, list2)
    else:
        merged_head = list2
        merged_head.next = merge_two_sorted_lists(list1, list2.next)

    return merged_head

# Сортування списку методом злиття
def merge_sort_list(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_list(head)
    right = merge_sort_list(next_to_middle)

    sorted_list = merge_two_sorted_lists(left, right)
    return sorted_list

# Пошук середини списку
def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Вивід списку
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Ініціалізація списку з масиву
def initialize_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Генерація простих чисел в діапазоні
def generate_prime_numbers(start, end, count):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return random.sample(primes, count)

# Ініціалізація списків
list1_values = generate_prime_numbers(13, 97, 12)
list2_values = generate_prime_numbers(13, 97, 8)
list1 = initialize_list(list1_values)
list2 = initialize_list(list2_values)

# Демонстрація роботи функцій
print("Original List 1:")
print_list(list1)
sorted_list1 = list1 if is_sorted(list1) else merge_sort_list(list1)
print("\nSorted List 1:")
print_list(sorted_list1)

print("\nOriginal List 2:")
print_list(list2)
sorted_list2 = list2 if is_sorted(list2) else merge_sort_list(list2)
print("\nSorted List 2:")
print_list(sorted_list2)

# Об'єднання двох списків після перевірки та сортування
merged_list = merge_two_sorted_lists(sorted_list1, sorted_list2)
print("\nMerged Sorted List:")
print_list(merged_list)
