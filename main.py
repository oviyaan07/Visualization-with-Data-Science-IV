import matplotlib.pyplot as plt

blood_sugar_men=[113, 85, 90, 84, 104, 120, 100, 134, 92, 68, 85, 99, 111,154]
blood_sugar_women=[95, 110, 88, 102, 120, 72, 115, 105, 79, 90, 159, 108, 135]
data=[blood_sugar_men, blood_sugar_women]
colors=['g','r']
labels=['Men','Women']
bins=[80, 100, 125, 150]

plt.hist(data, bins=bins, rwidth=0.9, color=colors, label=labels, orientation='horizontal')
plt.xlabel('total number of patients')
plt.ylabel('blood sugar level')
plt.title('Blood Sugar Level Distribution')
plt.legend()
plt.show()