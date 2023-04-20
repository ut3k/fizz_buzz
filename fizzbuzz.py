print("Value for Start range")
start_range = int(input())
print("Value for end range")
end_range = int(input())

numbers = list(range(start_range,end_range+1))

print(f"You selected range starting from {start_range} and ending at {end_range}")

print("value for fizz")
fizz_value = int(input())
print("value for buzz")
buzz_value = int(input())
print("-------------")
print(f"FIZZ BUZZ for numbers: {fizz_value} and {buzz_value} in range {start_range} to {end_range}")

for i in numbers:
    if (i % fizz_value) == 0 and (i % buzz_value) == 0 :
        print("fizz buzz")
    elif (i % fizz_value) == 0 :
        print("fizz")
    elif (i % buzz_value) == 0 :
        print ("buzz")
    else:
        print(i)
