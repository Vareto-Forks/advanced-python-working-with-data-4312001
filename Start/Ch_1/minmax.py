# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values  = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
# print(min(values))
# print(min(strings))

# TODO: The max() function finds the maximum value
# print(max(values))
# print(max(strings))

# TODO: define a custom "key" function to extract a data field
# print(min(strings, key=len))
# print(max(strings, key=len))
# print(min(strings, key=lambda x:len(x)))
# print(max(strings, key=lambda x:len(x)))


# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data['metadata']['title'])
print(len(data['features']))

def getfeat(dataitem, featname='mag', convert=float):
    feature = dataitem['properties'][featname]
    if feature is None:
        feature = 0
    if convert is not None:
        return convert(feature)
    return feature

print(min(data['features'], key=getfeat))
print(max(data['features'], key=getfeat))
