# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23, 17, 35, 29, 12]
# ax.bar(langs, students)
# plt.savefig('fig.png', bbox_inches='tight')
# plt.show()


import matplotlib.pyplot as plt

# Make fake dataset
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')

# Choose the position of each barplots on the x-axis (space=1,4,3,1)
y_pos = [i for i in range(len(height))]
width = [.5 for _ in range(len(y_pos))]

# Create bars
plt.bar(y_pos, height, width=width)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()
