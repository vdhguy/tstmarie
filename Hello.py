import tkinter as tk
import math


class RotatingHello:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello qui tourne")
        self.root.geometry("500x900")
        self.root.configure(bg="#1e1e2e")

        self.canvas = tk.Canvas(
            root, width=500, height=900, bg="#1e1e2e", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.angle = 0
        self.radius = 130
        self.colors = [
            "#f38ba8", "#fab387", "#f9e2af",
            "#a6e3a1", "#94e2d5", "#89b4fa", "#cba6f7",
        ]

        self.circles = [
            {"text": "Hello", "cx": 250, "cy": 220, "direction": 1},
            {"text": "world", "cx": 250, "cy": 670, "direction": -1},
        ]

        self.animate()

    def animate(self):
        self.canvas.delete("all")

        for circle in self.circles:
            cx, cy = circle["cx"], circle["cy"]
            text = circle["text"]
            direction = circle["direction"]

            self.canvas.create_oval(
                cx - self.radius - 30, cy - self.radius - 30,
                cx + self.radius + 30, cy + self.radius + 30,
                outline="#45475a", width=2, dash=(4, 4),
            )

            n = len(text)
            for i, char in enumerate(text):
                char_angle = direction * self.angle + (i * 360 / n)
                rad = math.radians(char_angle)
                x = cx + self.radius * math.cos(rad)
                y = cy + self.radius * math.sin(rad)
                color = self.colors[i % len(self.colors)]
                self.canvas.create_text(
                    x, y, text=char,
                    font=("Segoe UI", 42, "bold"),
                    fill=color,
                )

            self.canvas.create_text(
                cx, cy,
                text=text,
                font=("Segoe UI", 24, "italic"),
                fill="#cdd6f4",
            )

        self.angle = (self.angle + 2) % 360
        self.root.after(30, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingHello(root)
    root.mainloop()
