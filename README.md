# Optical Flow using Lucas-Kanade Method

## Objective

The goal of this task was to implement sparse optical flow using the Lucas-Kanade method and then visualize how objects move between video frames. In the second part, the objective was to use this motion information to control an agent in a simulation environment.

---

## Subtask 1: Optical Flow

## Approach

For this, I followed a simple pipeline:

--> First, I used Shi-Tomasi corner detection to find good feature points (basically strong corners that are easier to track).  
--> Then, I applied the Lucas-Kanade optical flow method to track those points from one frame to the next.  
--> After tracking, I calculated the displacement (how far each point moved).  
--> Finally, I visualized the motion by drawing arrows for movement direction and marking the tracked points.  

---

## Implementation Details

--> Language: Python  
--> Libraries used: OpenCV, NumPy  
--> Environment: Ran inside a Docker container  

---

## Output

--> The program generates frames where:  
    --> Arrows show the motion vectors (direction + magnitude of movement)  
    --> Red dots show the feature points being tracked  

---

## Observations

--> The optical flow results look much better when the video has clear motion and noticeable features (edges or corners).  
--> In low-texture areas (plain walls, blank surfaces, etc.), there are fewer good points to track, so the tracking becomes limited or less stable.  

---

## Subtask 2: Control using Optical Flow (Attempt)

## Objective

The goal of this part was to use the computed optical flow to generate control commands (steering and throttle) for an agent in the simulator.

---

## Approach

I tried to use a simple and intuitive idea:

--> Divide the frame into left and right halves  
--> Compute the total motion (optical flow magnitude) on both sides  
--> Compare motion on both sides to decide direction  

Basic logic used:

- More motion on left → turn right  
- More motion on right → turn left  
- Constant forward throttle  

---

## Implementation

--> Used optical flow between consecutive frames  
--> Extracted displacement of tracked points  
--> Computed magnitude of motion on left vs right side  
--> Generated steering values based on comparison  

Example logic:

python-
if left_flow > right_flow:
    steering = 0.5
else:
    steering = -0.5

throttle = 1.0

---

## Challenges Faced

--> Faced issues with GUI rendering (RViz / simulator display) inside Docker  
--> Errors like "Failed to open display" prevented visualization  
--> Simulator ran but without proper GUI output  
--> Optical flow values were sometimes not stable enough for smooth control  

---

## What I Learned

--> How optical flow can be used beyond visualization, for decision-making  
--> Basics of integrating perception with control  
--> Challenges of running vision + simulation pipelines in Docker/ROS environments  

---

## Conclusion

Subtask 1 was successfully implemented and visualized.  
For Subtask 2, I was able to implement the core idea and logic, but due to environment and visualization issues, full behavior in simulation could not be verified.  

However, the overall pipeline of:  

**vision → motion estimation → control decision**  

was understood and partially implemented.

---

## Docker Environment

The project is inside a Docker container.

To run:

1. docker start -ai agvdocker

2. cd /root

Inside root, subtask2.py will directly be present, and the subtask1 is inside the optional_flow folder, in that u can run python optional_flow.py.
You can use any video to test out althought i got gui interruptions in subtask2 processing :(

