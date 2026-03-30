import cv2
import numpy as np

prev_gray = None  # global memory

def calculate(image):

    global prev_gray

    # Convert to grayscale
    curr_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # First frame case
    if prev_gray is None:
        prev_gray = curr_gray
        return 0.0, 0.5   # slow forward start

    # Detect features
    p0 = cv2.goodFeaturesToTrack(prev_gray, maxCorners=100, qualityLevel=0.3, minDistance=7)

    if p0 is None:
        prev_gray = curr_gray
        return 0.0, 0.5   # move forward if no features

    # Optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(prev_gray, curr_gray, p0, None)

    if p1 is None:
        prev_gray = curr_gray
        return 0.0, 0.5

    good_new = p1[st == 1]
    good_old = p0[st == 1]

    flow = good_new - good_old

    # Split frame
    mid_x = curr_gray.shape[1] // 2

    left_flow = 0
    right_flow = 0

    for i, (new, old) in enumerate(zip(good_new, good_old)):
        x, y = old.ravel()
        dx, dy = flow[i]

        magnitude = np.sqrt(dx**2 + dy**2)

        if x < mid_x:
            left_flow += magnitude
        else:
            right_flow += magnitude

    # Decision logic
    if left_flow > right_flow:
        steering = 0.5    # turn RIGHT
    else:
        steering = -0.5   # turn LEFT

    throttle = 1.0  # move forward

    # Debug prints (VERY IMPORTANT for evaluation)
    print(f"Left: {left_flow:.2f}, Right: {right_flow:.2f}, Steering: {steering}, Throttle: {throttle}")

    prev_gray = curr_gray

    return steering, throttle
