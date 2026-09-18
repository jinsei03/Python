numbers = input("Enter numbers separated by spaces: ")

numbers = numbers.split()

for index, number in enumerate(numbers):
    numbers[index] = int(number)

print(numbers)

largest = numbers[0]
smallest = numbers[0]
total = 0
evens = 0
odds = 0
counts = {}
most_seen = None
highest_count = 0

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    total += number
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

average = total / len(numbers)

print("--- RESULTS ---")
print("Largest: ",largest)
print("Smallest: ",smallest)
print("Total: ", total)
print(f"Average: {average:.2f}")
print("Number of evens: ",evens)
print("Number of odds: ",odds)
print("\nOccurences:")
for number, count in counts.items():
    print(f"{number} appears {count} times")
    if count > highest_count:
        most_seen = number
        highest_count = count
print("The most seen number is: ",most_seen)