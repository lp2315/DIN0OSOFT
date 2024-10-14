import tkinter as tk


# tkinter config window
class SliderWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Slider Window")

        self.sliders = []
        labels = ["Rows", "Columns", "Scaling", "Speed"]
        ranges = [(3, 15), (3, 25), (40, 60), (0, 2)]

        for i in range(4):
            label = tk.Label(master, text = labels[i])
            label.pack()
            slider = tk.Scale(master, from_ = ranges[i][0], to = ranges[i][1], orient = tk.HORIZONTAL)
            slider.set((ranges[i][0] + ranges[i][1]) // 2)
            slider.pack()
            self.sliders.append(slider)

        float_slider = tk.DoubleVar()
        self.sliders[3].config(variable = float_slider, resolution = 0.05)
        self.sliders[3].set((ranges[3][0] + ranges[3][1]) // 2)
        self.button = tk.Button(master, text = "Get Values", command = self.get_values)
        self.button.pack()

        self.values = None

    def get_values(self):
        self.values = [slider.get() for slider in self.sliders]
        self.master.destroy()


def main():
    root = tk.Tk()
    app = SliderWindow(root)
    root.mainloop()
    return app.values
