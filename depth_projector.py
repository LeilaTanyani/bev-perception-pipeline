import numpy as np


class DepthIntegratedProjector:
    """
    Implements depth-integrated 3D-to-2D back-projection, utilizing explicit depth maps
    to map pixels directly to accurate 3D coordinates, bypassing flat ground assumptions.
    """

    def __init__(self, intrinsic_matrix: np.ndarray, extrinsic_matrix: np.ndarray):
        self.K = intrinsic_matrix
        self.K_inv = np.linalg.inv(intrinsic_matrix) if intrinsic_matrix is not None else None
        self.R_t = extrinsic_matrix

    def back_project_pixels(self, depth_map: np.ndarray) -> np.ndarray:
        """
        Transforms 2D pixel spaces back to 3D camera coordinates using a dense depth map.

        Args:
            depth_map (np.ndarray): H x W matrix representing spatial depth per pixel.

        Returns:
            np.ndarray: 3 x N matrix representing dense (X, Y, Z) point clouds in camera space.
        """
        pass

    def map_to_bev_occupancy(self, point_cloud: np.ndarray, grid_size: tuple) -> np.ndarray:
        """
        Discretizes the 3D point cloud into a 2D top-down occupancy grid representation.
        """
        pass