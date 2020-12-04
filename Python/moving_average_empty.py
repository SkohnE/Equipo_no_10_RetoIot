import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.signal import find_peaks


def smooth_curve_average(points, sample_size):
    smoothed_points = [int(sum(points[i:i+sample_size])//sample_size) for i in range(0,len(points), sample_size)]
    print(smoothed_points)
    return smoothed_points

def smooth_curve_exponential(points, factor=0.9):
    smoothed_points = [(points[i-1]*factor + points[i]*(1-factor))for i in range(1, len(points))]
    return smoothed_points

sample_size = 10
data_series = []
peaks = []

random.seed(0)

while len(data_series) < 1000:
    data_series.append(random.uniform(360, 380))

data_series_smooth_ex = smooth_curve_exponential(data_series, 0.95)
data_series_smooth_av = smooth_curve_average(data_series, sample_size)
peaks, _ = find_peaks(data_series_smooth_av)
s = np.array(data_series_smooth_av)
print(peaks)
#plt.plot(data_series)
#plt.plot(data_series_smooth_ex)
plt.plot(peaks, s[peaks], 'x')
plt.plot(data_series_smooth_av)
plt.plot()
plt.ylabel("Data")

plt.show()


