import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math
import time

from typing import List
from plot import Point, Plot
from execution_time import ExecutionTime


class BezierCurve:
    num_of_iteration: int
    control_points: List[Point]
    result_points: List[Point]
    
    def __init__(self, num_of_iteration: int, control_points: List[Point]):
        self.num_of_iteration = num_of_iteration
        self.control_points = control_points
        self.result_points = np.zeros((2**num_of_iteration + 1, 2))
        self.result_points[0] = control_points[0]
        self.result_points[len(self.result_points)-1] = control_points[len(control_points)-1]
    
    def find_middle_point(self, p1: Point, p2: Point) -> Point:
        return (p1 + p2) / 2
    
    def brute_force(self, plot: Plot, execution_time: ExecutionTime):
        execution_time.start()
        coefficient = np.zeros(len(self.control_points))
        for i in range(len(self.control_points)):
            coefficient[i] = math.comb(len(self.control_points)-1, i)
        t = 0
        delta_t = 1 / 2**self.num_of_iteration
        execution_time.stop()
        
        for i in range(1, 2**self.num_of_iteration):
            execution_time.start()
            t += delta_t
            for j in range(len(self.control_points)):
                coefficient_result = coefficient[j] * (1-t)**(len(self.control_points)-j-1) * (t**j)
                self.result_points[i] += coefficient_result * self.control_points[j]
            execution_time.stop()
            
            plot.add_dot(self.result_points[i])
            plot.pause(1 / 2**self.num_of_iteration)
    
    def divide_and_conquer(self, num_of_iteration: int, control_points: List[Point], l: int, r: int, plot: Plot, execution_time: ExecutionTime):
        if num_of_iteration == 0:
            return
        
        execution_time.start()
        next_control_points_1, next_control_points_2 = np.zeros((len(control_points), 2)), np.zeros((len(control_points), 2))
        next_control_points_1[0] = control_points[0]
        next_control_points_2[len(next_control_points_2)-1] = control_points[len(control_points)-1]
        execution_time.stop()
        
        # Variables for displaying dots and lines
        temp = np.zeros((math.ceil(len(control_points)*(len(control_points)-1)/2), 2))
        temp_idx, last_temp_idx = 0, 0
        current_iteration = self.num_of_iteration - num_of_iteration
        
        for i in range(1, len(control_points)):
            for j in range(len(control_points)-i):
                execution_time.start()
                control_points[j] = self.find_middle_point(control_points[j], control_points[j+1])
                execution_time.stop()
                
                if current_iteration < 4:
                    plot.add_dot(control_points[j], color_='0.5')
                    temp[temp_idx] = control_points[j]
                    temp_idx += 1
                
            # Display dashed lines
            if current_iteration < 4:
                delay_time = current_iteration+2 if current_iteration <= 2 else current_iteration**2
                plot.pause(1 / 2**delay_time)
                if temp_idx - last_temp_idx > 1:
                    line = temp[last_temp_idx:temp_idx].transpose()
                    plot.add_line(line, linestyle_='dashed', color_='0.5')
                    plot.pause(1 / 2**delay_time)

            execution_time.start()
            next_control_points_1[i] = control_points[0]
            next_control_points_2[len(next_control_points_2)-i-1] = control_points[len(control_points)-i-1]
            execution_time.stop()
            
            last_temp_idx = temp_idx
        
        plot.remove_saved_dots()
        plot.add_dot(control_points[0], None, save=False)
        
        execution_time.start()
        mid = (l+r) // 2
        self.result_points[mid] = control_points[0]        
        execution_time.stop()
        
        self.divide_and_conquer(num_of_iteration-1, next_control_points_1, l, mid, plot, execution_time)
        self.divide_and_conquer(num_of_iteration-1, next_control_points_2, mid+1, r, plot, execution_time)
  