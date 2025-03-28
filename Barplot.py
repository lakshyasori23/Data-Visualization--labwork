import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create the bar plot
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title('Sample Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()
