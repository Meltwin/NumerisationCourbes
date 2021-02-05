import Image as i
import matplotlib.pyplot as plt

p = i.Picture("./imgs/206.png")
display = i.PictureShow(1, 2, "Test")
display.add_image(p.get_img(), "Original")
b = i.Isolator([0.29019, 0.85882, 0.705882], 0.38)
#zone = [(1, 1), (563, 330)]
zone = [(1, 1), (2254, 1504)]
pTreated = b.isolate(p.get_img(), zone)
display.add_image(pTreated, "Traité", True)
plt.show()

picker = i.PointPicker([48, 279], [1, 0], 0.5, [0, -1], 10/24)
points = picker.pick_point(pTreated)

csv = i.CSVCreator("./out/206full.csv")
csv.write(points)
