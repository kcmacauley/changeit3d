import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Load the STL file using Open3D
mesh = o3d.io.read_triangle_mesh("../data/vase_aligned.stl")

# Step 2: Convert the mesh to a point cloud
point_cloud = mesh.sample_points_uniformly(number_of_points=1000)
points = np.asarray(point_cloud.points)

# Extract x, y, and z coordinates
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Find the maximum and minimum values of x, y, and z
max_x, min_x = np.max(x), np.min(x)
max_y, min_y = np.max(y), np.min(y)
max_z, min_z = np.max(z), np.min(z)

# Find the maximum absolute values of x, y, and z
max_abs_x = max(abs(min_x), abs(max_x))
max_abs_y = max(abs(min_y), abs(max_y))
max_abs_z = max(abs(min_z), abs(max_z))

# Calculate the scaling factor
scaling_factor = max(max_abs_x, max_abs_y, max_abs_z)

# Scale x, y, and z coordinates
scaled_x = x / scaling_factor
scaled_y = y / scaling_factor
scaled_z = z / scaling_factor

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(scaled_x, scaled_y, scaled_z, c='b', marker='.')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Show plot

plt.show()
np.savez("vase_0576.npz", pointcloud=points)
