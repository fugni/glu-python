import matplotlib.pyplot as plt

# pie chat information
pie_data = [10, 80, 100]
pie_labels = 'food', 'pac', 'food'
pie_colors = ['#72bcd4', '#ffea00', '#4ee44e']

# make the pie chart
plt.pie(pie_data, labels=pie_labels, colors=pie_colors)
plt.title('pac man')
plt.show()