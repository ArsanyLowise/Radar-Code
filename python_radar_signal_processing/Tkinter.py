import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class RadarPlotCanvas:
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.plot_initial()

    def plot_initial(self):
        # Initial plot
        angles = np.linspace(0, 2 * np.pi, 100)
        radii = np.abs(np.sin(angles))
        self.ax.plot(angles, radii)
        self.ax.set_title('Radar Data Visualization')
        self.canvas.draw()

    def update_plot(self):
        # Update plot with new data
        self.ax.clear()
        angles = np.linspace(0, 2 * np.pi, 100)
        radii = np.abs(np.sin(angles))  
        self.ax.plot(angles, radii)
        self.ax.set_title('Radar Data Visualization')
        self.canvas.draw()

class RadarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Radar Data Visualization')
        self.geometry('800x600')

        self.canvas = RadarPlotCanvas(self)

        self.button = tk.Button(self, text='Update Plot', command=self.canvas.update_plot)
        self.button.pack(side=tk.BOTTOM)

if __name__ == '__main__':
    app = RadarApp()
    app.mainloop()
