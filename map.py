import numpy as np
import requests

"""
Map class handling island data and detection.

Fetches and processes map data from an API, detects distinct islands, and calculates 
their average heights. Maintains mappings between fields, islands, and their properties.

Attributes:
    grid (numpy.array): 2D array representing the height map
    island_to_fields (dict): Maps island IDs to lists of coordinate tuples
    field_to_island (dict): Maps field coordinates to island IDs
    island_to_avg_height (dict): Maps island IDs to their average heights
"""


class Map:

    def __init__(self):
        response = requests.get("https://jobfair.nordeus.com/jf24-fullstack-challenge/test")
        data = response.text.strip().split("\n")
        self.grid = np.array([list(map(int, row.split())) for row in data])

        self.island_to_fields = {}
        self.field_to_island = {}
        self.island_to_avg_height = {}

        self.detect_islands()

    def detect_islands(self):
        island_id = 0
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                if self.grid[row, col] > 0 and (row, col) not in self.field_to_island:
                    self.island_to_fields[island_id] = []
                    self.detect_island(row, col, island_id)
                    self.island_to_avg_height[island_id] = self.calculate_avg_height(island_id)
                    island_id += 1

    def detect_island(self, row, col, island_id):
        if (
            0 <= row < self.grid.shape[0] and
            0 <= col < self.grid.shape[1] and
            self.grid[row, col] > 0 and
            (row, col) not in self.field_to_island
        ):
            self.field_to_island[(row, col)] = island_id
            self.island_to_fields[island_id].append((row, col))

            self.detect_island(row + 1, col, island_id)
            self.detect_island(row - 1, col, island_id)
            self.detect_island(row, col + 1, island_id)
            self.detect_island(row, col - 1, island_id)
            self.detect_island(row + 1, col - 1, island_id)
            self.detect_island(row - 1, col - 1, island_id)
            self.detect_island(row + 1, col + 1, island_id)
            self.detect_island(row - 1, col + 1, island_id)

    def calculate_avg_height(self, island_id):
        total_height = 0
        for field in self.island_to_fields[island_id]:
            total_height += self.grid[field]
        return total_height / len(self.island_to_fields[island_id])


