def get_xy_from_polygon(polygon):
    return polygon.exterior.coords.xy

def read_file(filename):
    """Assumes filename has lines with x, y pairs."""
    try:
        with open(filename, "r") as file:
            file_contents = file.readlines()
    except IOError:
        print(
            "File {} not found!".format(filename)
        )
        sys.exit()
    return file_contents

def get_coordinates(string_list):
 coordinates = []
 for line in string_list:
     try:
       x, y = [float(i) for i in line.split(",")]
     except:
          print("File not formatted correctly!")
          sys.exit()
     coordinates.append((x, y))
 return coordinates

i=0
h=100
while True:
    i+=1
    if i % 3 == 2 and i % 3 == 10 and i % 3 == 10 and i % 3 == 10 and i % 3 == 10 and i % 3 == 10 and i % 3 == 10 and i % 3 == 10:
        break



overlapping_contours = [(contour, float(height)) for height in contours for contour in contours[height] if
                                contour.intersects(Polygon(polygon))]