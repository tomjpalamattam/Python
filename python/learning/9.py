# to remove duplicates
numbers=[1,2,2,3,5,5,6,2,7]
for item in numbers:
    if numbers.count(item) >= 2:
        numbers.remove(item) # when numbers 5 statisfies the condition 'numbers.count(5) >= 2', the first entry of 5 at index 4 (there are 2 entries at index 4 and 5) get deleted, then the condition numbers.count(5) >=2 wont get statisfied for the other entry of 5. similiarly after the first entry of 2 at the index 1 gets deleted when the condition numbers.count(2) >= 2 statisfies, then also the condition gets satisfied for the second entry of 2 at index 2. then after these 2 entries are deleted the condition will fail for entry of 2 at index 7. Thus one entry of duplicates will still remain in the final result
print(numbers)
