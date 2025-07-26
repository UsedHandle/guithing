import tkinter as tk
import numpy as np # a little excessive but has vectors
#import pynetworktables

class RadioButtons(tk.Canvas):
    def __init__(self, master, options, spacing=70, radius=10, **kwargs):
        super().__init__(master, **kwargs)
        # 6 sides, 2 branches, 3 coral per branch
        self.options = [*enumerate(["Coral"]*6*2*3)]
        self.spacing = spacing
        self.radius = radius
        self.selected = None
        self.items = {}

        self.draw_radio_buttons(kwargs["width"],kwargs["height"])

    def draw_radio_buttons(self, width, height):
        print(width)
        print(height)

        internalHexRad = 50
        radVec = np.array([0, 1])
        leftVec = np.array([-1, 0])
        rightVec = np.array([1, 0])
        center = np.array([width/2, height/2])
        circle = self.create_oval(
            center[0] - self.radius, center[1] - self.radius,
            center[0] + self.radius, center[1] + self.radius,
            outline="grey", fill="grey", width=2
        )
        theta = -np.pi/2
        for i in range(6):
            for j in range(3):
                (x,y) = center + (internalHexRad+j*2*self.radius)*radVec + leftVec*2*self.radius

                print((internalHexRad+j*2*self.radius)*radVec)[1])
                circle = self.create_oval(
                    x - self.radius, y - self.radius,
                    x + self.radius, y + self.radius,
                    outline="grey", fill="grey", width=2
                )
            for j in range(3):
                (x,y) = center + (internalHexRad+j*2*self.radius)*radVec + rightVec*2*self.radius
                circle = self.create_oval(
                    x - self.radius, y - self.radius,
                    x + self.radius, y + self.radius,
                    outline="grey", fill="grey", width=2
                )
            theta += np.pi/3
            radVec = np.array([np.cos(theta), np.sin(theta)])
            leftVec = np.array([-radVec[1], radVec[0]])
            rightVec = np.array([radVec[1], -radVec[0]])

        for i, label in enumerate(self.options):
            x = 50 + i * self.spacing
            y = 50 + i * self.spacing  # Diagonal

            # Draw outer circle
            circle = self.create_oval(
                x - self.radius, y - self.radius,
                x + self.radius, y + self.radius,
                outline="grey", fill="grey", width=2
            )

            # Draw label next to the circle
            text = self.create_text(x + 30, y, text=label, anchor="w", font=("Helvetica", 12))

            self.items[label] = (circle, text)

            # Bind events to both circle and text
            self.tag_bind(circle, "<Button-1>", lambda e, name=label: self.select(name))
            self.tag_bind(text, "<Button-1>", lambda e, name=label: self.select(name))

    def select(self, name):
        # Deselect previous
        if self.selected:
            circle_id, _ = self.items[self.selected]
            self.itemconfig(circle_id, fill="grey")
        
        # Select new
        circle_id, _ = self.items[name]
        self.itemconfig(circle_id, fill="black")
        self.selected = name
        print(f"Selected: {name}")

root = tk.Tk()
root.title("asldfja")
canvas = RadioButtons(root, ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"], width=400, height=400, bg="white")
canvas.pack()

root.mainloop()
