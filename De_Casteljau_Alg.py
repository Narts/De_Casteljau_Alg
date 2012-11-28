import Image
import ImageDraw

SIZE = 128
image = Image.new("RGB", (SIZE, SIZE))
d = ImageDraw.Draw(image)


""" recursive calculate the route of points of Bezier curve
    Points: the control points array
    step: granularity about how often will a point on Bezier curve be determind
"""
def bezier_point(points, step):
    len_points = len(points)
    new_points = []
    for x in xrange(0, len_points - 1):
        x1 = points[x][0]
        x2 = points[x + 1][0]
        y1 = points[x][1]
        y2 = points[x + 1][1]
        new_Px = (step * x1 + (10 - step) * x2) / 10
        new_Py = (step * y1 + (10 - step) * y2) / 10
        new_points.append([new_Px, new_Py])
    if len(new_points) == 1:
        return new_points[0]
    else:
        return bezier_point(new_points, step)


""" draw curve
    point_array: the control points array
"""
def draw_curve(point_array):
    """draw control polygon """
    polygon = []
    for x in xrange(0, len(point_array)):
        polygon.append(point_array[x][0])
        polygon.append(point_array[x][1])
    d.line(polygon)
    """draw Bezier curve """
    draw_point = []
    draw_points = []
    for u in xrange(0, 11):
        draw_point.append(bezier_point(point_array, u))
    for x in xrange(0, 11):
        draw_points.append(draw_point[x][0])
        draw_points.append(draw_point[x][1])
    d.line(draw_points)

draw_curve([[10, 70], [30, 10], [80, 20], [100, 90], [70, 60]])

image.save(r"PATH", "PNG")

print "ok."
