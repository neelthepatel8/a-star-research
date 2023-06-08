import matplotlib.pyplot as plt

# Create a list of grid sizes
grid_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
              110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

# Create a list of distance metrics
distance_metrics = ['Manhattan', 'Euclidian', 'Diagonal', 'Octile']

# Create a dictionary to store the data for each distance metric
data = {}

# Add the data for each distance metric to the dictionary
data['Manhattan'] = [18, 42, 78, 138, 186, 222, 398, 322, 242,
                     334, 434, 398, 810, 1610, 694, 1970, 734, 1762, 1094, 1090]
data['Euclidian'] = [18, 42, 70, 158, 194, 218, 330, 770, 390,
                     306, 542, 506, 886, 650, 2474, 1166, 1298, 1226, 1142, 1114]
data['Diagonal'] = [18, 54, 170, 186, 166, 342, 498, 330, 470,
                    434, 474, 450, 738, 1158, 746, 606, 906, 1962, 1398, 1722]
data['Octile'] = [18, 46, 74, 110, 234, 150, 370, 794, 646,
                  558, 314, 726, 542, 1398, 1238, 846, 1006, 1038, 1862, 1810]

# Create the scatter plot
plt.scatter(data['Manhattan'], data['Euclidian'],
            c=grid_sizes, s=100, cmap='viridis')
plt.xlabel('Number of Nodes Expanded (Manhattan)')
plt.ylabel('Path Length (Euclidian)')
plt.title('A* Algorithm Performance for Different Grid Sizes and Distance Metrics')
plt.colorbar()

# Display the plot
plt.show()
