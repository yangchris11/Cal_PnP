import cv2
import numpy as np

if __name__ == '__main__':
    im_src = cv2.imread('../data/c076.jpg')

    im_dst = cv2.imread('../pic/s014.jpg')

    h = np.array([[-3.197556667655673, -0.546073102979902, 3670.615331626416719],
         [-0.365785685005658, 0.267660032953031, 730.330719988622150],
         [-0.001090190391681, 0.001123052257074, 1.000000000000000]])

    # pts_src = np.array([[141, 131], [480, 159], [493, 630], [64, 601]])
    # pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]])
    # # Calculate Homography
    # h, status = cv2.findHomography(pts_src, pts_dst)
    # print(h)

    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    cv2.imshow("Warped Source Image", im_out)
    cv2.waitKey(0)