#dictionary
import pickle

phone=str(input('phone:'))
digits_mapping= {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
for ch in phone:
    print(digits_mapping.get(ch, "!"))
