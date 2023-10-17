import numpy as np

def create_XY(X: np.ndarray, y: np.ndarray) -> tuple:
    """
    Returns a tuple of numpy ndarrays.
    
    Parameters:
    - X: numpy ndarray
    - y: numpy ndarray

    Returns:
    - tuple: (X, y)
    """
    return (X, y)

def create_Dataset(train: tuple, test: tuple) -> tuple:
    """
    Returns a tuple of tuples.
    
    Parameters:
    - train: tuple (X_train, y_train)
    - test: tuple (X_test, y_test)

    Returns:
    - tuple: (train, test)
    """
    return (train, test)

def create_LogRegParams(xy: tuple, params: np.ndarray) -> tuple:
    """
    Returns a tuple with given parameters.

    Parameters:
    - xy: tuple (X, y)
    - params: numpy ndarray

    Returns:
    - tuple: (xy, params)
    """
    return (xy, params)

def create_XYList(data_list: list) -> list:
    """
    Returns a list of tuples.
    
    Parameters:
    - data_list: list of tuples (X, y)

    Returns:
    - list: [tuple1, tuple2, ...]
    """
    return data_list

# Example usage
X = np.array([1, 2, 3])
y = np.array([4, 5, 6])

xy = create_XY(X, y)
dataset = create_Dataset(xy, xy)
logreg_params = create_LogRegParams(xy, np.array([0.1, 0.2]))
xy_list = create_XYList([xy, xy])

print(xy)
print(dataset)
print(logreg_params)
print(xy_list)
