import os
import subprocess

# Define the directory where the SDF files are located
root_dir = "/home/zai/ros_ws/utils_ws/src/ycb-tools/models"
MESH_WORKSPACE_PATH="/home/zai/ros_ws/utils_ws/src/ycb-tools/models"
# Walk through all directories and subdirectories starting from the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        # Check if the file is an SDF file
        if filename.endswith(".sdf"):
            # Build the full path to the SDF file
            sdf_file_path = os.path.join(dirpath, filename)
            # Build the full path to the URDF file
            urdf_file_path = os.path.splitext(sdf_file_path)[0] + ".urdf"
            # Run the sdf2urdf command using subprocess
            os.environ["MESH_WORKSPACE_PATH"] = MESH_WORKSPACE_PATH
            # pysdf: https://github.com/andreasBihlmaier/pysdf
            subprocess.run(["rosrun", "pysdf", "sdf2urdf.py", sdf_file_path, urdf_file_path])