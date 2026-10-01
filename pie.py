import matplotlib.pyplot as plt

plt.pie([35, 25, 20, 15, 5], labels=['Math', 'Science', 'English', 'History', 'Art'], autopct='%1.1f%%')
plt.title('Time Spent by Subject')
plt.show()