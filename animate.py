import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from matplotlib.animation import FuncAnimation

# Function to update the plot for each frame in the animation
global co
co = 0
def update(frame):
    global co
    print(co)
    co += 1
    for i, ax_view in enumerate(axes):
        ax_view.cla()  # Clear the current axis
        ax_view.scatter(positions[frame][:, 0], positions[frame][:, 1], positions[frame][:, 2],
                        c=colors, marker='o', s=50)
        ax_view.set_title(f'Frame {frame + 1}/{len(positions)} - {views[i]}')
        ax_view.set_xlim([min_x, max_x])
        ax_view.set_ylim([min_y, max_y])
        ax_view.set_zlim([min_z, max_z])
        ax_view.view_init(elev=elevations[i], azim=azimuths[i])  # Set the view angles

# Read the trajectory file
print('Reading Trajectory')
traj = read('toto.traj', ':')  # Replace 'toto.traj' with your actual file name

# Extract atom positions and individual colors from each frame
print('Extracting Frames')
positions = [traj[i].positions for i in range(10)]
colors = np.arange(traj[0].get_global_number_of_atoms())

# Determine the plot limits
min_x = np.min([pos[:, 0].min() for pos in positions])
max_x = np.max([pos[:, 0].max() for pos in positions])
min_y = np.min([pos[:, 1].min() for pos in positions])
max_y = np.max([pos[:, 1].max() for pos in positions])
min_z = np.min([pos[:, 2].min() for pos in positions])
max_z = np.max([pos[:, 2].max() for pos in positions])

# Set up the initial subplots with 3D projection
fig = plt.figure(figsize=(20, 20))
axes = [fig.add_subplot(2, 2, i+1, projection='3d') for i in range(4)]

# Define views for each subplot
views = ['Top View', 'Side View', 'Front View', 'Corner View']
elevations = [90, 0, 0, 30]  # Elevation angles for each view
azimuths = [0, -90, 0, 45]      # Azimuth angles for each view

# Create the animation
print('Starting Animation')
animation = FuncAnimation(fig, update, frames=len(positions), interval=10, repeat=False)

# Save the animation with higher quality
animation.save('animation_high_quality.mp4', writer='ffmpeg', fps=10, dpi=300)  # Adjust dpi and bitrate as needed

#plt.show()

