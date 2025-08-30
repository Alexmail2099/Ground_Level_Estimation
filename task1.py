"""
Assignment 5 - Task 1
Goal: 
    - Estimate ground level from LiDAR data using a histogram
    - Save histogram plots for both datasets
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def get_ground_level(pcd, bins=200, save_path=None):
    """
    Estimate ground level using histogram of Z-values.

    Parameters:
        pcd (np.ndarray): LiDAR point cloud, shape (N,3)
        bins (int): Number of bins for histogram
       

    Returns:
        float: Estimated ground level (z-value)
    """
    z_vals = pcd[:, 2]

    # Compute histogram of heights
    hist, bin_edges = np.histogram(z_vals, bins=bins)

    # Find the bin with the maximum frequency (most common height)
    max_bin_idx = np.argmax(hist)

    # Take the center of that bin as the ground level
    ground_level = (bin_edges[max_bin_idx] + bin_edges[max_bin_idx + 1]) / 2

    # Plot histogram
    plt.figure(figsize=(8, 5))
    plt.hist(z_vals, bins=bins, color='skyblue', edgecolor='black')
    plt.axvline(ground_level, color='red', linestyle='--', label=f'Ground: {ground_level:.2f}')
    plt.xlabel("Height (Z)")
    plt.ylabel("Frequency")
    plt.title("Ground Level Estimation")
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()

    return ground_level


if __name__ == "__main__":
    # Ensure working directory is script folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Create folder for images if it doesn't exist
    os.makedirs("images", exist_ok=True)

    # Load datasets (from the same folder as the script)
    dataset1 = np.load("dataset1.npy")
    dataset2 = np.load("dataset2.npy")

    # Compute ground levels
    ground1 = get_ground_level(dataset1, save_path="images/dataset1_ground_hist.png")
    ground2 = get_ground_level(dataset2, save_path="images/dataset2_ground_hist.png")

    # Print results
    print(f"Dataset 1 Ground Level: {ground1:.2f}")
    print(f"Dataset 2 Ground Level: {ground2:.2f}")
