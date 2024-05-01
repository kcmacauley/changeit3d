import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_point_cloud(file_path):
    # Load the point cloud data
    data = np.load(file_path)
    points = data['pointcloud']
    print(max(points[:, 0]), max(points[:, 1]), max(points[:, 2]))
    print(min(points[:, 0]), min(points[:, 1]), min(points[:, 2]))

    # Plot the point cloud
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Point Cloud')
    plt.show()

def plot_point_clouds_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter .npz files
    npz_files = [f for f in files if f.endswith('.npz')]

    # Plot point clouds from each .npz file
    for file in npz_files:
        file_path = os.path.join(folder_path, file)
        print(file_path)
        plot_point_cloud(file_path)

# Plot point clouds from all .npz files in the folder
folder_path = "/home/kcmacauley/changeit3d/changeit3d/data/shapetalk/point_clouds/scaled_to_align_rendering/vase/ModelNet/"
plot_point_clouds_in_folder(folder_path)
