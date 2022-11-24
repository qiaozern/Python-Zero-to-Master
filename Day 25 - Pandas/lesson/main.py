# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
    
    
# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd

# data = pd.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data['temp']))


# # convert data into dict
# data_dict = data.to_dict()
# print(data_dict)


# # convert data into list
# temp_list = data['temp'].to_list()
# print(len(temp_list))


# # Find average and max of temp
# print(data['temp'].mean())
# print(data['temp'].max())


# # Get data in columns; can use either way below
# print(data["condition"])
# print(data.condition)


# # Get data in row
# print(data[data.day == 'Monday'])


# # Print the row of data which had the highest temperature
# print(data[data['temp'] == max(data['temp'])])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)

# # Convert Monday's temperature to Fahrenheit
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')

# Data Analysis for Central Park Squirrel
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squrirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squrirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squrirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_squrirrels_count)
print(red_squrirrels_count)
print(black_squrirrels_count)

data_dict = {
    "Fur Color": ["Gray","Red","Black"],
    "Count": [gray_squrirrels_count, red_squrirrels_count, black_squrirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv('squrirrel_count')
