import sys,os
import csv
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def graph(machine):
    # data를 불러와서, pandas로 사용하기 위한 dataframe으로 변경
    rawdata = pd.read_csv('c:/dyn_trace_temp/' + machine + '_trace.csv')
    df = pd.DataFrame(rawdata)

    # graph declare
    fig = plt.figure(figsize=(15,10))
    i=1

    # RS act motor signal
    if "RS ZS-Z1 Act Motor Out" in df:
        ax1=fig.add_subplot(5,1,i)
        ax0=ax1.twinx()
        ax0.plot(df["WS LS SBC Sync. State"], label='WS LS SBC Sync. State')
        ax1.plot(df["RS ZS-Z1 Act Motor Out"], label='RS ZS-Z1 Act Motor Out')
        ax1.plot(df["RS ZS-Z2 Act Motor Out"], label='RS ZS-Z2 Act Motor Out')
        ax1.plot(df["RS ZS-Z3 Act Motor Out"], label='RS ZS-Z3 Act Motor Out')
        ax1.legend(loc="lower left")
        i = i + 1

    # RS lens acc
    if "RS Lens acc Y Converted Value" in df:
        ax2=fig.add_subplot(5,1,i)
        ax0=ax2.twinx()
        ax0.plot(df["WS LS SBC Sync. State"], label='WS LS SBC Sync. State')
        ax2.plot(df["RS Lens acc Y Converted Value"], label='RS Lens acc Y Converted Value')
        ax2.plot(df["RS Lens acc X Converted Value"], label='RS Lens acc X Converted Value')
        ax2.legend(loc="lower left")
        i = i + 1

    # RS Cap Z2 Converted Value
    if "RS Cap Z2 Converted Value" in df:
        ax4=fig.add_subplot(5,1,i)
        ax0=ax4.twinx()
        ax0.plot(df["WS LS SBC Sync. State"], label='WS LS SBC Sync. State')
        ax4.plot(df["RS Cap Z2 Converted Value"], label='RS Cap Z2 Converted Value')
        ax4.plot(df["RS Cap Z1 Converted Value"], label='RS Cap Z1 Converted Value')
        ax4.legend(loc="lower left")
        i = i + 1

    # stage position err X
    if "RS SS-X Position Error" in df:
        ax3=fig.add_subplot(5,1,i)
        ax0=ax3.twinx()
        ax0.plot(df["WS LS SBC Sync. State"], label='WS LS SBC Sync. State')
        ax3.plot(df["RS SS-X Position Error"], label='RS SS-X Position Error')
        ax3.plot(df["WS SS-X Position Error"]*4, label='WS SS-X Position Error*4')
        ax3.legend(loc="lower left")
        i = i + 1

    # stage position err Y
    if "RS SS-Y Position Error" in df:
        ax3=fig.add_subplot(5,1,i)
        ax0=ax3.twinx()
        ax0.plot(df["WS LS SBC Sync. State"], label='WS LS SBC Sync. State')
        ax3.plot(df["RS SS-Y Position Error"], label='RS SS-Y Position Error')
        ax3.plot(df["WS SS-Y Position Error"]*4, label='WS SS-Y Position Error*4')
        ax3.legend(loc="lower left")
        i = i + 1

    # graph를 보여주기 위해
    plt.show()