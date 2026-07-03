# Birds-Eye-View (BEV) Perception Pipeline

An autonomous driving perception framework engineering top-down Birds-Eye-View transformations from monocular perspective frames using three distinct spatial geometry strategies. 

The figures below demonstrate the execution of the 4-point Homography Inverse Perspective Mapping (IPM) pipeline using a sample frame from the Stuttgart sequence.

| 1. Perspective View with Source Anchors | 2. Generated Bird's-Eye-View (BEV) Ground Plane |
|:---:|:---:|
| ![Perspective Source Selection](assets/stuttgart_perspective.png) | ![Warped BEV Output](assets/stuttgart_bev.png) |
| *Figure 1: Original monocular frame with 4 selected ground-plane control anchors.* | *Figure 2: Orthographic top-down transformation isolating lane boundaries.* |
## Pipeline Architecture

This repository showcases the modular, clean-code architecture of the transformation engine. The internal mathematical loops are abstracted to preserve core algorithmic confidentiality, demonstrating production-grade software topology.

1. **Inverse Perspective Mapping (IPM) via 4-Point Homography**: Planar ground transformation based strictly on homography estimation vectors.
2. **Parametric IPM**: Rigid body transformation incorporating explicit camera Intrinsic ($K$) and Extrinsic ($[R|T]$) matrices to project ground metrics.
3. **Depth-Integrated IPM**: Back-projects 2D pixel frames into dense 3D camera-space coordinates $(X, Y, Z)$ using discrete depth profiles, eliminating planar assumptions.

## Dataset & Calibration Drift Analysis
Validated on the **KITTI dataset** to quantify how spatial layout fidelity behaves under synthetic calibration drift. The pipeline tracks error propagation matrices when tracking pitch, roll, and focal length disturbances to evaluate model robustness in physical vehicle deployments.