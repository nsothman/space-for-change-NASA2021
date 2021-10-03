import csv
import numpy as np
from PIL import Image, ImageOps
import cv2
import math
from sklearn import preprocessing

injusticeDatasets = [["Drought Hazard Economic Risk", "I"],
                     ["Drought Hazard Frequency and Distribution", "I"],
                     ["Drought Hazard Mortality Risk", "I"],
                     ["Flood Hazard Economic Risk", "I"],
                     ["Flood Hazard Frequency and Distribution", "I"],
                     ["Flood Hazard Mortality Risk", "I"],
                     ["Precipitation Rate", "I"],
                     ["Soil Moisture (Normalized Polarization Difference)", "I"],
                     ["Surface Air Temperature (L3, Day, Monthly)", "I"],
                     ["Total Dust Deposition, Dry+Wet All Bins (Monthly)", "I"],
                     ["Vegetation Index (L3, Monthly)", "N"]]
injusticeWeights = [0.028, 0.028, 0.028, 0.105, 0.105, 0.105, 0.131, 0.137, 0.141, 0.0164, 0.176]
populationDatasets = [["Population Density, 2020", "I"],
                      ["Settlements", "N"]]


images = []
for file in injusticeDatasets:
    img = cv2.imread("./Datasets/" + file[0] + ".tiff", cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (980, 2017))
    img_arr = np.asarray(img)
    if file[1] == "I":
        img_arr = (255-img_arr)
        img_arr[img_arr > 254] = 0
    img_arr = img_arr * (255.0/np.max(img_arr))
    images.append(img_arr)

injustice = []
latDiff = -0.0090437
longDiff = 0.008983

for i in range(len(images)):
    images[i] = images[i] * (injusticeWeights[i] / 30)

for i in range(len(images) - 1):
    images[i + 1] = np.array(np.add(images[i], images[i + 1]))

sumArr = np.array(images[-1])

lat = 32.1387
for l in sumArr:
    long = 24.9064
    for v in l:
        injustice.append([lat, long, v])
        long += (longDiff * 2)
    lat += latDiff * 2


with open("./Datasets/injustice.csv", "w") as injustice_file:
    writer = csv.writer(injustice_file)
    for row in injustice:
        writer.writerow(row)

