import numpy as np
import requests


class Map:

    def __init__(self):
        response = requests.get("https://jobfair.nordeus.com/jf24-fullstack-challenge/test")
        data = response.text.strip().split("\n")
        self.grid = np.array([list(map(int, row.split())) for row in data])
        print(self.grid)