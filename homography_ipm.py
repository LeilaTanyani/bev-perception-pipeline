import numpy as np
import cv2
from typing import Tuple, Optional


class HomographyIPM:
    """
    Implements Inverse Perspective Mapping (IPM) using a 4-point homography matrix.
    Useful for planar ground-plane estimation without explicit camera matrices.
    """

    def __init__(self, src_points: np.ndarray, dst_points: np.ndarray):
        """
        Initializes the homography transformer with source and destination coordinates.

        Args:
            src_points (np.ndarray): 4x2 array of pixel coordinates in the perspective view.
            dst_points (np.ndarray): 4x2 array of desired coordinates in the BEV plane.
        """
        self.src_points = src_points
        self.dst_points = dst_points
        self.H: Optional[np.ndarray] = None
        self._compute_homography()

    def _compute_homography(self) -> None:
        """Computes the 3x3 homography matrix using OpenCV's findHomography."""
        pass

    def transform(self, image: np.ndarray, output_dims: Tuple[int, int]) -> np.ndarray:
        """
        Warps the input perspective image into a Bird's-Eye-View projection.

        Args:
            image (np.ndarray): Input RGB/BGR image (H x W x C).
            output_dims (Tuple[int, int]): Target width and height of the BEV grid.

        Returns:
            np.ndarray: Wrapped Bird's-Eye-View image.
        """
        pas