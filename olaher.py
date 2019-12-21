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

for key in ndnDF:
    print(ndnDF[key].head(10))

fig = plt.figure()
index = 0

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

    ax = plt.subplot2grid((4,4), (index // 4, index % 4), rowspan=1)
    ax.set_title(node, dict(fontsize=9))
    ax.tick_params(labelsize=9)
    ax.plot(ndndelay["DelayS"], label='NDN delay (s)' 
            if index == 0 else '', linewidth=0.5)
    ax.plot(ipdelay["DelayS"], label='IP delay (s)' 
            if index == 0 else '', linewidth=0.5)
    index += 1

legend = fig.legend(loc='upper center', shadow=True, fontsize='x-small')

fig_rate  = plt.figure()
index = 0
for node in nodeList:
    ndnrate = ndnDF["rate"].loc[
            (ndnDF["rate"]["Node"] == node)
            ]
    iprate = ipDF["rate"].loc[
            (ipDF["rate"]["Node"] == node)
            ]

    ax_rate = plt.subplot2grid((4,4), (index // 4, index % 4), rowspan=1, label=node)
    ax_rate.set_title(node,dict(fontsize=9))
    ax_rate.tick_params(labelsize=9)
    ax_rate.plot(ndnrate["Kilobytes"], marker='+', linewidth=0, 
                 label='NDN rate (Kb)' if index == 0 else '')
    ax_rate.plot(iprate["Kilobytes"], marker='o', linewidth=0, 
                 label='IP rate (Kb)' if index == 0 else '')
    
    index += 1

legend = fig_rate.legend(loc='upper center', shadow=True, fontsize='x-small')

fig_drop = plt.figure()
index = 0

for node in nodeList:
    ndndrop = ndnDF["packetDrop"].loc[
            (ndnDF["packetDrop"]["Node"] == node)
            ]
    ipdrop = ipDF["packetDrop"].loc[
            (ipDF["packetDrop"]["Node"] == node)
            ]

    ax_drop = plt.subplot2grid((4,4), (index // 4, index % 4), rowspan=1, label=node)
    ax_drop.set_title(node, dict(fontsize=9))
    ax_drop.tick_params(labelsize=9)
    ax_drop.plot(ndndrop["Packets"], marker='+', linewidth=0, 
                 label='NDN packet drop (count)' if index == 0 else '')
    ax_drop.plot(ipdrop["Packets"], marker='o', linewidth=0, 
                 label='IP packet drop (count)' if index == 0 else '')

    index += 1

legend = fig_drop.legend(loc='upper center', shadow=True, fontsize='x-small')

plt.show()
