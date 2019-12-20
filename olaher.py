import pandas as pd
import matplotlib.pyplot as plt

try:
    ndnDF = { 
        "delay" : pd.read_csv("dataset/simulrev1/app-delays-trace.txt", delimiter="\t"),
        "packetDrop" : pd.read_csv("dataset/simulrev1/drop-trace.txt", delimiter="\t"),
        "cache" : pd.read_csv("dataset/simulrev1/cs-trace.txt", delimiter="\t"),
        "rate" : pd.read_csv("dataset/simulrev1/rate-trace.txt", delimiter="\t"),
    }
    ipDF = { 
        "delay" : pd.read_csv("dataset/simulrev1/app-delays-trace-ip.txt", delimiter="\t"),
        "packetDrop" : pd.read_csv("dataset/simulrev1/drop-trace-ip.txt", delimiter="\t"),
        "cache" : pd.read_csv("dataset/simulrev1/cs-trace-ip.txt", delimiter="\t"),
        "rate" : pd.read_csv("dataset/simulrev1/rate-trace-ip.txt", delimiter="\t"),
    }
except IOError:
    print("Opening data files failed! Exiting")
    exit(1)

nodeList = ndnDF["delay"]["Node"].unique()

'''
for node in nodeList:
    ndndelay = ndnDF["delay"].loc[
            (ndnDF["delay"]["Node"] == node) &
            (ndnDF["delay"]["Type"] == "LastDelay")
            #(ndnDF["delay"]["DelayS"] != 0)
            ]
    ipdelay = ipDF["delay"].loc[
            (ipDF["delay"]["Node"] == node) &
            (ipDF["delay"]["Type"] == "LastDelay")
            #(ipDF["delay"]["DelayS"] != 0)
            ]

    fig, ax = plt.subplots(num=node)
    ax.plot(ndndelay["DelayS"], label='NDN delay (s)', linewidth=0.5)
    ax.plot(ipdelay["DelayS"], label='IP delay (s)', linewidth=0.5)
    legend = ax.legend(loc='upper center', shadow=True, fontsize='small')
    legend.get_frame().set_facecolor('C0')


for node in nodeList:
    ndnrate = ndnDF["rate"].loc[
            (ndnDF["rate"]["Node"] == node)
            ]
    iprate = ipDF["rate"].loc[
            (ipDF["rate"]["Node"] == node)
            ]

    fig_rate, ax_rate = plt.subplots(num=node)

    ax_rate.plot(ndnrate["Kilobytes"], marker='+', linewidth=0, label='NDN rate (Kb)')
    ax_rate.plot(iprate["Kilobytes"], marker='o', linewidth=0, label='IP rate (Kb)')
    legend = ax_rate.legend(loc='upper center', shadow=True, fontsize='small')
'''

for node in nodeList:
    ndndrop = ndnDF["packetDrop"].loc[
            (ndnDF["packetDrop"]["Node"] == node)
            ]
    ipdrop = ipDF["packetDrop"].loc[
            (ipDF["packetDrop"]["Node"] == node)
            ]

    fig_drop, ax_drop = plt.subplots(num=node)

    ax_drop.plot(ndndrop["Packets"], marker='+', linewidth=0, label='NDN packet drop (count)')
    ax_drop.plot(ipdrop["Packets"], marker='o', linewidth=0, label='IP packet drop (count)')
    legend = ax_drop.legend(loc='upper center', shadow=True, fontsize='small')

plt.show()
