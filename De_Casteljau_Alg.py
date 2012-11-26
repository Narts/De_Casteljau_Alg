import Image
import ImageDraw

SIZE = 128
image = Image.new("RGB", (SIZE, SIZE))
d = ImageDraw.Draw(image)


def bezier_point(points, step):
    lenPoints = len(points)
    newPoints = []
    for x in xrange(0, lenPoints - 1):
        x1 = points[x][0]
        x2 = points[x + 1][0]
        y1 = points[x][1]
        y2 = points[x + 1][1]
        newPx = (step * x1 + (10 - step) * x2) / 10
        newPy = (step * y1 + (10 - step) * y2) / 10
        newPoints.append([newPx, newPy])
    if len(newPoints) == 1:
        return newPoints[0]
    else:
        return bezier_point(newPoints, step)


def draw_curve(point_array):
    """draw support polygon """
    polygon = []
    for x in xrange(0, len(point_array)):
        polygon.append(point_array[x][0])
        polygon.append(point_array[x][1])
    d.line(polygon)
    """draw bezier curve """
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
