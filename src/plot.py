import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from typing import List, Any, Optional, Tuple


# Point: Tuple[float,float]
# Point[0]: x, Point[1]: y
class Point(list): ...


# Matplotlib stuff
class Plot:
    fig: Any
    ax: Any
    lines: List[Any] = []
    dots: List[Any] = []
    colors: List[float]
    color_idx: int = 0
    
    def __init__(self, num_of_iteration: int, subplot_: Optional[int] = 111,
                 figsize_: Optional[Tuple[float,float]] = (6.4, 4.8), dpi_: Optional[int] = 100):
        self.fig = plt.figure(figsize=figsize_, dpi=dpi_)
        self.ax = self.fig.add_subplot(subplot_)
        self.colors = cm.rainbow(np.linspace(0, 1, 2**num_of_iteration + 1))
        
    def add_dot(self, point: Point, color_: Optional[str] = None, save: Optional[bool] = True):
        dot = self.ax.scatter(point[0], point[1], color=color_ if color_ else self.colors[self.color_idx])
        self.color_idx += 1 if not color_ else 0
        if save:
            self.dots.append(dot)            
    
    def remove_saved_dots(self):
        for i in range(len(self.dots)):
            self.dots[i].remove()
        self.dots = []
    
    def add_line(self, points: List[Point], linestyle_: Optional[str] = 'solid', color_: Optional[str] = None, save: Optional[bool] = True):
        line, = self.ax.plot(points[0], points[1], linestyle=linestyle_, color=color_ if color_ else self.colors[self.color_idx])
        self.color_idx += 1 if not color_ else 0
        if save:
            self.lines.append(line)
    
    def remove_saved_lines(self):
        if self.lines:
            for line in self.lines:
                line.remove()
    
    def plot(self, points: List[Point]):
        for i in range(len(points)):
            plt.scatter(points[i][0], points[i][1], color=self.colors[self.color_idx])
        plt.plot(points.transpose()[0], points.transpose()[1], color=self.colors[self.color_idx])

    @staticmethod
    def pause(delay_time: float = 0.05):
        plt.pause(delay_time)
    
    @staticmethod
    def show():
        plt.show()
    