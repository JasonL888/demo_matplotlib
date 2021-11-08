import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

# Create a Figure with 2 rows and 1 columns of subplots:
fig, ax = plt.subplots(2, 1, figsize=(16,9))

# X axis parameter:
xaxis = np.array([
    '11-Nov',
    '12-Nov',
    '13-Nov',
    '14-Nov',
    '15-Nov',
    '16-Nov',
    '17-Nov',
    '18-Nov',
    '19-Nov',
    '20-Nov',
])

yaxis_numlogin = np.array([
    523455,
    523455,
    523455,
    523455,
    523455,
    523455,
    523455,
    523455,
    523455,
    523455,
])

yaxis_devicesonline = np.array([
    32825,
    60999,
    120134,
    153003,
    200838,
    300514,
    352138,
    345136,
    353780,
    347899,
])

yaxis_devicesonline_percent = np.divide(yaxis_devicesonline, yaxis_numlogin)

# Index 4 Axes arrays in 4 subplots within 1 Figure:
# top-left: num-login/Devices-online vs date
# bottom-left: % Devices-online vs date
# top-right: num-cpe-swap vs date
# bottom-right: online=>offline, offline=>online vs date
ax[0].plot(xaxis, yaxis_numlogin, 'b', marker = "o", label='Num Login') #row=0, column=0
ax[0].plot(xaxis, yaxis_devicesonline, 'g', marker = "o", label='Num Online Devices') #row=0, column=0
ax[0].set_title('Trend of Devices online')
ax[0].legend()
for xy in zip(xaxis, yaxis_numlogin):
    ax[0].annotate('%s' % xy[1], xy=xy, textcoords='data')
for xy in zip(xaxis, yaxis_devicesonline):
    ax[0].annotate('%s' % xy[1], xy=xy, textcoords='data')


ax[1].plot(xaxis, yaxis_devicesonline_percent, 'g', marker = 'o')
ax[1].set_title('Trend of % Devices online')
ax[1].set_ylabel('% Devices online')
ax[1].yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
for xy in zip(xaxis, yaxis_devicesonline_percent):
    ax[1].annotate('%.2f%%' % (100 * xy[1].item()), xy=xy, textcoords='data')
#ax[1, 0].plot(xaxis, 'b') #row=1, column=0
#ax[0, 1].plot(xaxis, np.cos(x), 'r') #row=0, column=1
#ax[1, 1].plot(xaxis, np.tan(x), 'k') #row=1, column=1

plt.savefig('demo_chart.png')
plt.show()
