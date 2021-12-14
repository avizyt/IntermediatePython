import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        X = np.array(list).reshape((3, 3))
        flattend_X = np.array(X).reshape(1,9)

        axis1_mean = np.mean(X, axis=0).tolist(),
        axis2_mean = np.mean(X, axis=1).tolist(),
        flattend_mean = np.mean(flattend_X)

        axis1_var = np.var(X, axis=0).tolist(),
        axis2_var = np.var(X, axis=1).tolist(),
        flattend_var = np.var(flattend_X)

        axis1_std = np.std(X, axis=0).tolist(),
        axis2_std = np.std(X, axis=1).tolist(),
        flattend_std = np.std(flattend_X)

        calculations = {
            "mean": [axis1_mean, axis2_mean, flattend_mean],
            "variance": [axis1_var, axis2_var, flattend_var],
            "standard deviation": [axis1_std, axis2_std, flattend_std],
        }

    return calculations

# Driver code
if __name__ == "__main__":
    print(calculate([2,6,2,8,4,0,1,5,7]))
    print(calculate([9,1,5,3,3,3,2,9,0]))
    print(calculate([2,6,2,8,4,0,1,]))