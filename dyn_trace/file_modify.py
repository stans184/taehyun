import os
import shutil
import csv
import pandas as pd

# 파일 확장자 변경 gh -> csv
# shutil.move('d:/workspace/trace/autosave_tracedata_00 - 복사본.gh', 'd:/workspace/trace/autosave_tracedata_00 - 복사본.csv')
with open('d:/workspace/trace/autosave_tracedata_00 - 복사본.gh') as f:
    # raw_data 가공
    raw_data = f.read().splitlines()
    raw_data = list(filter(None, raw_data))

    # trace 항목 구역 설정
    start = raw_data.index('[Sec]') + 1
    end = int(raw_data.index('2048'))
    trace_item = raw_data[start:end]
    trace_item.insert(0, 'time')

    # trace_data 가공 / 공백 제거
    trace_raw_data = raw_data[end+2:]
    trace_data = []
    i=0
    while i<len(trace_raw_data):
        trace_data.insert(i,trace_raw_data[i].split())
        i = i+1

    # csv 파일로 저장
    trace_data.insert(0,trace_item)
    dataframe = pd.DataFrame(trace_data)
    dataframe.to_csv('c:/dyn_trace_temp/trace.csv', header=False, index=False)