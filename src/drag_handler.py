class DragHandler:

    drag_data = {"element": None, "x": 0, "y": 0}
    canvas = None
    scale_range = 0

    def __init__(self, scale_range):
        self.scale_range = scale_range

    def find_closest_scale_range(self, x):
        return x - (x % self.scale_range) + self.scale_range / 2

    def make_draggable(self, canvas, token):
        self.canvas = canvas
        self.canvas.tag_bind(token, "<ButtonPress-1>", self.on_start)
        self.canvas.tag_bind(token, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(token, "<ButtonRelease-1>", self.on_drop)

    def on_start(self, event):
        """Begin drag of an object"""
        print('on_start', event)

        # record the element and its location
        self.drag_data["element"] = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        """Handle dragging of an object"""
        print('on_drag', event)
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]
        self.canvas.move(self.drag_data["element"], delta_x, delta_y)
        # Update drag data
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drop(self, event):
        """End drag of an object"""
        self.canvas.coords(
            self.drag_data["element"],
            self.find_closest_scale_range(self.drag_data["x"]),
            self.find_closest_scale_range(self.drag_data["y"])
        )

        # Reset the drag data
        self.drag_data["element"] = None
        self.drag_data["x"] = 0
        self.drag_data["y"] = 0
