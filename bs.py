def binary_search_recursive(start, end, int_list, target):
    # Condition to check if element is not present
    if start <= end:
        mid = (start + end) // 2

        # Check if mid element is the target element
        if int_list[mid] == target:
            return mid + 1

        # If not, check if lesser than mid element
        # Change range to start to mid-1, since less than mid
        elif target < int_list[mid]:
            return binary_search_recursive(start, mid - 1, int_list, target)

        # Check if greater than mid element
        # Change range to mid+1 to end, since greater than mid
        elif target > int_list[mid]:
            return binary_search_recursive(mid + 1, end, int_list, target)
    else:
        return -1

# --- Main part of the program ---
# Read length of list from user
length = int(input("Enter length of list: "))
int_list = []
# Read elements of list
for i in range(length):
    element = int(input("Enter element: "))
    int_list.append(element)
# Sort the list
int_list = sorted(int_list)
print("Sorted list:", int_list)
# Read target element to be found
target = int(input("Enter target element: "))

# --- Using the recursive binary search ---
position_recursive = binary_search_recursive(0, length - 1, int_list, target)
if position_recursive == -1:
    print('Element not found in the list (recursive)')
else:
    print("Element found at position:", position_recursive, "(recursive)")

print("-" * 20) # Separator

# --- Using the iterative binary search ---
start = 0
end = length - 1
position_iterative = -1

while start <= end:
    mid = (start + end) // 2
    if int_list[mid] == target:
        position_iterative = mid
        break
    elif target < int_list[mid]:
        end = mid - 1
    elif target > int_list[mid]:
        start = mid + 1

if position_iterative == -1:
    print('Element not found in the list (iterative)')
else:
    print("Element found at position:", position_iterative + 1, "(iterative)")