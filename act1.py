import matplotlib.pyplot as plt

marks=[45, 67, 56, 78, 90, 34, 23, 45, 67, 89, 90, 100, 56, 78, 65, 92, 69, 54, 58, 29]

plt.hist(marks, bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()