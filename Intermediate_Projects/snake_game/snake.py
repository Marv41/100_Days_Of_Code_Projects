import turtle as tm

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15

class Snake:
    def __init__(self):
        self.shape = "square"
        self.color = "white"
        self.size = .5
        self.segments = []
        self.create_starting_snake()
        self.head = self.segments[0]

    def create_starting_snake(self,):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = tm.Turtle(self.shape)
        new_segment.shapesize(self.size)
        new_segment.color(self.color)
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for _ in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[_ - 1].position()
            self.segments[_].goto(next_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def check_wall_collision(self):
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if xcor > 300 or xcor < -300 or ycor > 300 or ycor < -300:
            return True
        else:
            return False

    def check_self_collision(self):
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 5:
                return True
        return False

    def add_tail(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_starting_snake()
        self.head = self.segments[0]

