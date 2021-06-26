""""
This class implements a list data structure
which has the following properties
    - There is a constant empty space between elements
     in the list
    - The elements are in sorted order in the list

input:
    - `space` int (optional): specify the space/gap between
    elements of a list. default is 2.
    member functions
    - `len()` -> int : number of elements in the list
    - `append(x)` -> None : adds an element in the list
    - `median()` -> float : returns the median
Usage:
    # >>> arr = SortedSpacedList()
    # >>> arr.append(2) # 2
    # >>> arr.append(5) # 2 None None 5
    # >>> arr.append(1) # 1 2 4 None 5 6 None 7-> 1 None None 2 None
     None 4 None None 5
    # >>> arr.median()
    # 2
    # >>> len(arr)
    # 3

"""
