
# Import necessary libraries
import numpy as np

# Define the class for a network schedule
class NetworkSchedule:

    # Initialize the network schedule
    def __init__(self, activities, durations):
        self.activities = activities
        self.durations = durations

    # Construct the network schedule
    def construct_network(self):
        # Create a dictionary of predecessors
        predecessors = {}
        for activity in self.activities:
            predecessors[activity] = []
        for activity in self.activities:
            for predecessor in activity.predecessors:
                predecessors[activity].append(predecessor)

        # Create a dictionary of successors
        successors = {}
        for activity in self.activities:
            successors[activity] = []
        for activity in self.activities:
            for successor in activity.successors:
                successors[activity].append(successor)

        # Return the network schedule
        return predecessors, successors

    # Calculate the earliest and latest dates of occurrence of events
    def calculate_dates(self):
        # Initialize the earliest and latest dates
        earliest_dates = {}
        latest_dates = {}
        for activity in self.activities:
            earliest_dates[activity] = 0
            latest_dates[activity] = self.durations[activity]

        # Calculate the earliest dates
        for activity in self.activities:
            for predecessor in self.predecessors[activity]:
                earliest_dates[activity] = max(earliest_dates[activity], earliest_dates[predecessor] + self.durations[predecessor])

        # Calculate the latest dates
        for activity in self.activities:
            for successor in self.successors[activity]:
                latest_dates[activity] = min(latest_dates[activity], latest_dates[successor] - self.durations[successor])

        # Return the earliest and latest dates
        return earliest_dates, latest_dates

    # Find a critical path
    def find_critical_path(self):
        # Initialize the critical path
        critical_path = []

        # Find the activities with zero total float
        for activity in self.activities:
            if self.latest_dates[activity] - self.earliest_dates[activity] == self.durations[activity]:
                critical_path.append(activity)

        # Return the critical path
        return critical_path

    # Determine the full and independent time reserves of all works
    def determine_time_reserves(self):
        # Initialize the full and independent time reserves
        full_time_reserves = {}
        independent_time_reserves = {}
        for activity in self.activities:
            full_time_reserves[activity] = self.latest_dates[activity] - self.earliest_dates[activity] - self.durations[activity]
            independent_time_reserves[activity] = min(self.earliest_dates[activity] - self.latest_dates[activity], 0)

        # Return the full and independent time reserves
        return full_time_reserves, independent_time_reserves

    # Determine the coefficients of tension of non-critical arcs
    def determine_coefficients_of_tension(self):
        # Initialize the coefficients of tension
        coefficients_of_tension = {}
        for activity in self.activities:
            if activity not in self.critical_path:
                coefficients_of_tension[activity] = (self.latest_dates[activity] - self.earliest_dates[activity]) / self.durations[activity]

        # Return the coefficients of tension
        return coefficients_of_tension

# Example usage
activities = [
    Activity("A", [], 10),
    Activity("B", ["A"], 5),
    Activity("C", ["A"], 15),
    Activity("D", ["B", "C"], 10),
    Activity("E", ["D"], 5),
]
durations = [10, 5, 15, 10, 5]

network_schedule = NetworkSchedule(activities, durations)

# Construct the network schedule