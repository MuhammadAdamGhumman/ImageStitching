import numpy as np
import random 


def calculate_projection_matrix(points_2d, points_3d):
    """
    To solve for the projection matrix. You need to set up a system of
    equations using the corresponding 2D and 3D points:

                                                      [ M11      [ u1
                                                        M12        v1
                                                        M13        .
                                                        M14        .
    [ X1 Y1 Z1 1 0  0  0  0 -u1*X1 -u1*Y1 -u1*Z1        M21        .
      0  0  0  0 X1 Y1 Z1 1 -v1*X1 -v1*Y1 -v1*Z1        M22        .
      .  .  .  . .  .  .  .    .     .      .       *   M23   =    .
      Xn Yn Zn 1 0  0  0  0 -un*Xn -un*Yn -un*Zn        M24        .
      0  0  0  0 Xn Yn Zn 1 -vn*Xn -vn*Yn -vn*Zn ]      M31        .
                                                        M32        un
                                                        M33 ]      vn ]

    Then you can solve this using least squares with np.linalg.lstsq() or SVD.
    Notice you obtain 2 equations for each corresponding 2D and 3D point
    pair. To solve this, you need at least 6 point pairs.

    Args:
    -   points_2d: A numpy array of shape (N, 2)
    -   points_2d: A numpy array of shape (N, 3)

    Returns:
    -   M: A numpy array of shape (3, 4) representing the projection matrix
    """

    # Placeholder M matrix. It leads to a high residual. Your total residual
    # should be less than 1.
    #M = np.asarray([[0.1768, 0.7018, 0.7948, 0.4613],
    #                [0.6750, 0.3152, 0.1136, 0.0480],
    #                [0.1020, 0.1725, 0.7244, 0.9932]])

    ###########################################################################
    # TODO: YOUR PROJECTION MATRIX CALCULATION CODE HERE
    ###########################################################################

    #raise NotImplementedError('`calculate_projection_matrix` function in ' +
    #    '`student_code.py` needs to be implemented')
    
    A = np.zeros([len(points_2d)*2, 12])

    B = np.zeros([len(points_2d)*2, 1])

    k = 0
    for i in range(len(points_2d)):
        A[i + k][0], A[i + k][1], A[i + k][2], A[i + k][3] = points_3d[i][0], points_3d[i][1], points_3d[i][2], 1
        A[i + k][8], A[i + k][9], A[i + k][10], A[i + k][11] = points_2d[i][0]*points_3d[i][0], points_2d[i][0]*points_3d[i][1], points_2d[i][0]*points_3d[i][2], -points_2d[i][0]

        A[i + k + 1][4], A[i + k + 1][5], A[i + k + 1][6], A[i + k + 1][7] = points_3d[i][0], points_3d[i][1], points_3d[i][2], 1
        A[i + k + 1][8], A[i + k + 1][9], A[i + k + 1][10], A[i + k + 1][11] = points_2d[i][1]*points_3d[i][0], points_2d[i][1]*points_3d[i][1], points_2d[i][1]*points_3d[i][2], -points_2d[i][1]
        
        B[i + k] = points_2d[i][0]

        B[i + 1 + k] = points_2d[i][1]

        k = k + 1

    U, S, V = np.linalg.svd(A)
    #print(V)

    M = V[-1:12]
    M = np.reshape(M, (3,4))

    ###########################################################################
    # END OF YOUR CODE
    ###########################################################################
    
    return M

def calculate_camera_center(M):
    """
    Returns the camera center matrix for a given projection matrix.

    The center of the camera C can be found by:

        C = -Q^(-1)m4

    where your project matrix M = (Q | m4).

    Args:
    -   M: A numpy array of shape (3, 4) representing the projection matrix

    Returns:
    -   cc: A numpy array of shape (1, 3) representing the camera center
            location in world coordinates
    """

    # Placeholder camera center. In the visualization, you will see this camera
    # location is clearly incorrect, placing it in the center of the room where
    # it would not see all of the points.
    #cc = np.asarray([1, 1, 1])

    ###########################################################################
    # TODO: YOUR CAMERA CENTER CALCULATION CODE HERE
    ###########################################################################

    #raise NotImplementedError('`calculate_camera_center` function in ' +
        #'`student_code.py` needs to be implemented')
        
    Q = M[0:3, 0:3]
    m4 = M[0:3, 3:4]
    Q_inv = np.linalg.inv(Q)
    cc = -1 * Q_inv.dot(m4)
    cc = cc.flatten()

    ###########################################################################
    # END OF YOUR CODE
    ###########################################################################

    return cc

def estimate_fundamental_matrix(points_a, points_b):
    """
    Calculates the fundamental matrix. Try to implement this function as
    efficiently as possible. It will be called repeatedly in part 3.

    You must normalize your coordinates through linear transformations as
    described on the project webpage before you compute the fundamental
    matrix.

    Args:
    -   points_a: A numpy array of shape (N, 2) representing the 2D points in
                  image A
    -   points_b: A numpy array of shape (N, 2) representing the 2D points in
                  image B

    Returns:
    -   F: A numpy array of shape (3, 3) representing the fundamental matrix
    """

    # Placeholder fundamental matrix
    #F = np.asarray([[0, 0, -0.0004],
                    #[0, 0, 0.0032],
                    #[0, -0.0044, 0.1034]])

    ###########################################################################
    # TODO: YOUR FUNDAMENTAL MATRIX ESTIMATION CODE HERE
    ###########################################################################

    #raise NotImplementedError('`estimate_fundamental_matrix` function in ' +
        #'`student_code.py` needs to be implemented')
        
    points_2d_pic_a = points_a
    
    points_2d_pic_b = points_b
        
    A = np.zeros([len(points_2d_pic_a), 9])
    
    for i in range(len(points_2d_pic_a)):
        A[i][0] = points_2d_pic_a[i][0] * points_2d_pic_b[i][0]
        A[i][1] = points_2d_pic_a[i][0] * points_2d_pic_b[i][1]
        A[i][2] = points_2d_pic_a[i][0]
        A[i][3] = points_2d_pic_a[i][1] * points_2d_pic_b[i][0]
        A[i][4] = points_2d_pic_a[i][1] * points_2d_pic_b[i][1]
        A[i][5] = points_2d_pic_a[i][1]
        A[i][6] = points_2d_pic_b[i][0]
        A[i][7] = points_2d_pic_b[i][1]
        A[i][8] = 1

    U, S, V = np.linalg.svd(A)

    M = V[-1:9]
    M = np.reshape(M, (3,3))

    U1, S1, V1 = np.linalg.svd(M)
    S1[np.argmin(S1)] = 0
    F = U1.dot(np.diag(S1).dot(V1))
    F = F / np.max(F)

    ###########################################################################
    # END OF YOUR CODE
    ###########################################################################

    return F

def ransac_fundamental_matrix(matches_a, matches_b):
    """
    Find the best fundamental matrix using RANSAC on potentially matching
    points. Your RANSAC loop should contain a call to
    estimate_fundamental_matrix() which you wrote in part 2.

    If you are trying to produce an uncluttered visualization of epipolar
    lines, you may want to return no more than 100 points for either left or
    right images.

    Args:
    -   matches_a: A numpy array of shape (N, 2) representing the coordinates
                   of possibly matching points from image A
    -   matches_b: A numpy array of shape (N, 2) representing the coordinates
                   of possibly matching points from image B
    Each row is a correspondence (e.g. row 42 of matches_a is a point that
    corresponds to row 42 of matches_b)

    Returns:
    -   best_F: A numpy array of shape (3, 3) representing the best fundamental
                matrix estimation
    -   inliers_a: A numpy array of shape (M, 2) representing the subset of
                   corresponding points from image A that are inliers with
                   respect to best_F
    -   inliers_b: A numpy array of shape (M, 2) representing the subset of
                   corresponding points from image B that are inliers with
                   respect to best_F
    """

    # Placeholder values
    #best_F = estimate_fundamental_matrix(matches_a[:10, :], matches_b[:10, :])
    #inliers_a = matches_a[:100, :]
    #inliers_b = matches_b[:100, :]

    ###########################################################################
    # TODO: YOUR RANSAC CODE HERE
    ###########################################################################

    #raise NotImplementedError('`ransac_fundamental_matrix` function in ' +
    #    '`student_code.py` needs to be implemented')
    
    numofiter = 5000
    
    num_corr = 10
    
    prev_inlier = 0
    
    most_inlier = 0
    
    one = np.ones([len(matches_a), 1])
    
    one_matches_a = np.append(matches_a, one, axis = 1)
    
    one_matches_b = np.append(matches_b, one, axis = 1)
    
    thresh = 0.001
    
    while(numofiter > 0):
        idx = random.sample(range(0, len(matches_a)), num_corr)
        
        a_corr = np.zeros([num_corr, 2])
        
        b_corr = np.zeros([num_corr, 2])
        
        for i in range(num_corr):
            a_corr[i] =  matches_a[idx[i]]
            b_corr[i] =  matches_b[idx[i]]
            
        F = estimate_fundamental_matrix(a_corr, b_corr)
        
        
        for i in range(len(matches_a)):
            dist = one_matches_a[i].dot(F)
            tran_b = np.transpose(one_matches_b[i])
            dist = dist.dot(tran_b)
            if(np.absolute(dist) < thresh):
                #print(dist)
                most_inlier = most_inlier + 1
        
        #print("prev_inlier = ", prev_inlier)
        if(most_inlier > prev_inlier):
            best_F = F
            #print("best_F = ", best_F)
            prev_inlier = most_inlier
        #print("most_inlier = ", most_inlier)
        #print("")
        most_inlier = 0
        
        numofiter = numofiter - 1
        
    inliers_a = np.zeros([prev_inlier, 2])
    inliers_b = np.zeros([prev_inlier, 2])
    
    k = 0
        
    for i in range(len(matches_a)):      
        dist = one_matches_a[i].dot(best_F)
        tran_b = np.transpose(one_matches_b[i])
        dist = dist.dot(tran_b)
            
        if(np.absolute(dist) < thresh):
            inliers_a[k] = matches_a[i]
            inliers_b[k] = matches_b[i]
            k = k + 1
    
    inliers_a = inliers_a[:100, :]
    inliers_b = inliers_b[:100, :]
    print(prev_inlier)
    ###########################################################################
    # END OF YOUR CODE
    ###########################################################################

    return best_F, inliers_a, inliers_b