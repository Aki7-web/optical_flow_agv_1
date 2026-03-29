# Optical Flow using Lucas-Kanade Method

## Objective
To implement sparse optical flow using the Lucas-Kanade method and visualize motion between frames.

## Approach
- Used Shi-Tomasi Corner Detection to identify feature points
- Applied Lucas-Kanade Optical Flow to track motion across frames
- Computed displacement vectors for each feature point
- Visualized motion using arrows and tracked points

## Implementation Details
- Language: Python
- Libraries: OpenCV, NumPy
- Environment: Docker container

## Output
- Generated frames showing motion vectors (arrows)
- Red dots indicate tracked feature points

## Observations
- Optical flow performs better in videos with clear motion and distinct features
- Low-texture regions produce fewer trackable points

## How to Run
```bash
python optical_flow.py