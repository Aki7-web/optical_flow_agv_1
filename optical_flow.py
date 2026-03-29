import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

# Detect more features
feature_params = dict(maxCorners=1000,
                      qualityLevel=0.01,
                      minDistance=3,
                      blockSize=7)

lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

ret, old_frame = cap.read()
if not ret:
    print("Error reading video")
    exit()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is None:
        break

    good_new = p1[st == 1]
    good_old = p0[st == 1]

    output = frame.copy()

    # 🔥 Amplify motion
    scale = 5

    for new, old in zip(good_new, good_old):
        a, b = new.ravel()
        c, d = old.ravel()

        dx = int((a - c) * scale)
        dy = int((b - d) * scale)

        # Draw arrows
        cv2.arrowedLine(output,
                        (int(c), int(d)),
                        (int(c + dx), int(d + dy)),
                        (0, 255, 0),
                        3,
                        tipLength=0.5)

        # 🔴 Red dot (bigger)
        cv2.circle(output, (int(a), int(b)), 6, (0, 0, 255), -1)

        # ⚪ White outline (for visibility)
        cv2.circle(output, (int(a), int(b)), 6, (255, 255, 255), 1)

    # Save frames
    if frame_count % 10 == 0:
        cv2.imwrite(f"flow_{frame_count}.jpg", output)

    # Re-detect features if too few
    if len(good_new) < 20:
        p0 = cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)
    else:
        p0 = good_new.reshape(-1, 1, 2)

    old_gray = frame_gray.copy()
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
