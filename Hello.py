import tkinter as tk
import math


class RotatingHello:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello qui tourne")
        self.root.geometry("500x500")
        self.root.configure(bg="#1e1e2e")

        self.canvas = tk.Canvas(
            root, width=500, height=500, bg="#1e1e2e", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.text = "Hello"
        self.angle = 0
        self.cx = 250
        self.cy = 250
        self.radius = 130
        self.colors = [
            "#f38ba8", "#fab387", "#f9e2af",
            "#a6e3a1", "#94e2d5", "#89b4fa", "#cba6f7",
        ]

        self.animate()

    def animate(self):
        self.canvas.delete("all")

        self.canvas.create_oval(
            self.cx - self.radius - 30, self.cy - self.radius - 30,
            self.cx + self.radius + 30, self.cy + self.radius + 30,
            outline="#45475a", width=2, dash=(4, 4),
        )

        n = len(self.text)
        for i, char in enumerate(self.text):
            char_angle = self.angle + (i * 360 / n)
            rad = math.radians(char_angle)
            x = self.cx + self.radius * math.cos(rad)
            y = self.cy + self.radius * math.sin(rad)
            color = self.colors[i % len(self.colors)]
            self.canvas.create_text(
                x, y, text=char,
                font=("Segoe UI", 42, "bold"),
                fill=color,
            )

        self.canvas.create_text(
            self.cx, self.cy,
            text="Hello",
            font=("Segoe UI", 24, "italic"),
            fill="#cdd6f4",
        )

        self.angle = (self.angle + 2) % 360
        self.root.after(30, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingHello(root)
    root.mainloop()
