"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np

class Patient:
    def __init__(self,name, weight=None, height=None):
        self.name =name 
        self.weight = weight
        self.height = height

    def get_body_mass_index(self, ):

        '''
        compute the body mass index (BMI) of a patient using the formula: 
        BMI = weight (kg) / (height (m))^2
        '''

        return self.weight / (self.height ** 2)








def load_csv(filename: str) -> np.ndarray:
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data: np.ndarray) -> np.ndarray:
    """ calculates the mean for a given input array 

    Args:
        data (np.ndarray): 2D array of inflammation data

    Returns:
        np.ndarray: 1D array of daily means
    """    
    return np.mean(data, axis=0)


def daily_max(data: np.ndarray) -> np.ndarray:
    """Calculate the daily max of a 2d inflammation data array.

    Args:
        data (np.ndarray): 2D array of inflammation data

    Returns:
        np.ndarray: 1D array of daily max values
    """
    return np.max(data, axis=0)


def daily_min(data: np.ndarray) -> np.ndarray:
    """Calculate the daily min of a 2d inflammation data array.

    Args:
        data (np.ndarray): 2D array of inflammation data

    Returns:
        np.ndarray: 1D array of daily min values
    """
    return np.min(data, axis=0)

