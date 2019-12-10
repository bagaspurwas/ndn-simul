import pandas as pd
import matplotlib as mplot


try:
    ndnDataFrame = { 
        "delay" : pd.read_csv("./dataset/ndn/app-delays-trace.txt", delimiter="\t"),
        "packetDrop" : pd.read_csv("./dataset/ndn/drop-trace.txt", delimiter="\t"),
        "cacheTracer" : pd.read_csv("./dataset/ndn/cs-trace.txt", delimiter="\t"),
        "rate" : pd.read_csv("./dataset/ndn/rate-trace.txt", delimiter="\t"),
    }
    '''
    ipDataFrame = { 
        "delay" : pd.read_csv("dataset/ndn/app-delays-trace-ip.txt", delimiter="\t"),
        "packetDrop" : pd.read_csv("dataset/ndn/drop-trace-ip.txt", delimiter="\t"),
        "cacheTracer" : pd.read_csv("dataset/ndn/cs-trace-ip.txt", delimiter="\t"),
        "rate" : pd.read_csv("dataset/ndn/rate-trace-ip.txt", delimiter="\t"),
    }
    '''
except IOError:
    print("Opening data files failed! Exiting")
    exit(1)

nodeSelector = "Adelaide"
delay = ndnDataFrame["delay"]
delaySelectedNode = delay[delay.Node == nodeSelector][["Time", "DelayUS"]]
delaySelectedNode.plot(x="Time", y="DelayUS",kind="scatter")



