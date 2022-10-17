import pandas as pd
from matplotlib import pyplot as plt

# y_values = [1, 2, 3, 4, 10]
# print [i ** 3 for i in y_values]
# plt.plot(y_values, [i ** 3 for i in y_values])
# plt.show()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# hurricanes_data = np.loadtxt('Hurricanes.csv', dtype=str, delimiter=',')
#   Read file
hurricanes_data = pd.read_csv('Hurricanes.csv', dtype=str, delimiter=',')
# print(hurricanes_data)

#   capture headers of table
hurricanes_data.head()
df = pd.DataFrame(hurricanes_data)

year = df['Year'].head(0)
nums = df['Hurricanes'].head(0)
dataFrame = pd.DataFrame(hurricanes_data.head(), columns=['Year','Hurricanes'])
print(dataFrame)
dataFrame.plot(x='Year', y='Hurricanes', kind='bar', figsize=(100, 90))
# fig = plt.figure(figsize=(50, 30))
# df1 = pd.DataFrame({'Year': [year], 'Hurricanes': [nums]})
# #= df.plot.bar(x='Year', y='Hurricanes', rot=0)
# plt.bar(year,nums[1:24])
# plt.ylabel('Hurricanes')
# plt.xlabel('Year')
# plt.title('Hurricanes in the US')
plt.show()

# print('Hurricanes',nums)
# df_hurricanes=pd.DataFrame(hurricanes)
# x_axis=df_hurricanes[[0]]
#               df = pd.DataFrame(d)
#               df.plot(kind='bar')
# print('op',x_axis)
# y_axis=df_hurricanes[[1]]
# print('op',y_axis)
# plt.bar([x_axis],[y_axis])
# plt.show()
