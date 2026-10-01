import matplotlib.pyplot as plt

plt.bar(['Math', 'Science', 'English', 'History', 'Art'], [85, 92, 78, 65, 88])
plt.title('Scores by Subject')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.savefig('bar.png')
plt.show()