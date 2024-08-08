def sum_of_list-elements(lst):
    return sum(lst)
print(sum_of_list([3,5,8,10]))

     ### question 2
def smallest_number(*numbers):
    return min(numbers)
print(smallest_number(* (4,6,3,9)))
       ## question 3
def set_numbers(*numbers):
    return {num**2 for num in numbers}

print(set_numbers(*{2,4,6,7,9,13}))
###    question 4

def dic(person={
    "name":"M. Zeeshan",
    "Gender":"Male",
    "Age":"19",
    "City":"Karachi"
}):
    return list(person.keys())
print(dic())
