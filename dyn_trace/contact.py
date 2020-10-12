import ftplib
import os
import test.test_shutil
import time, datetime
import pandas as pd
# 파일 수정 함수 불러오기
from file_modify import chg_csv
# graph 함수 불러오기
from visualize import graph
# 현재 년 불러오기
from now import now_year

# pas 호기명 입력 받은 후 ftp를 이용한 process 진행
def asml_pas(split_info):
    # ftp 접속
    try:
        ftp_name = ftplib.FTP(split_info[1], split_info[0], 'ftp')
    except TimeoutError as e:
        print("#. 설비에 접속할수 없습니다.")
        print("#. 다시접속하거나 다른 호기에 접속하여 주세요")
    else:
        # ftp / SWAD 폴더 접속
        ftp_name.cwd('/usr/asm/data.0000/service_data/SW/SWAD')
        test_list = []

        # 현재 directory의 file 및 info 뽑아옴
        ftp_name.retrlines('LIST -t', test_list.append) # -t를 넣어서, 최신순으로 정렬 & 같은 년도가 반복되면, 시간이 받아짐,,, why?
        test_list = [line.split() for line in test_list]
   
        # list adjust
        list_df = pd.DataFrame(test_list[1:8], columns=['authorize','etc','machine_num','machine','file_capa','month','day','time','file_name'])
        list_df.drop(['authorize', 'etc', 'machine_num', 'machine'], axis = 'columns', inplace=True)
        list_df['month'] = [datetime.datetime.strptime(x, '%b') for x in list_df['month']] # 숫자로 변환
        list_df['month'] = list_df['month'].dt.strftime("%m") # 월만 따오기
        list_df['file_capa'] = list_df['file_capa'].astype(int)
       
        list_df['time'] = pd.to_datetime(list_df['time'])
        list_df['time'] = list_df['time'].dt.strftime("%H%M")

        list_df['need_file'] = list_df[list_df['file_capa']>40000]['file_name'] # sort file_capa above 40000
        list_df = list_df[list_df['need_file'].notnull()] # delete emtpy row

        list_df.to_csv("d:/workspace/trace/"+machine+"list.csv")
   
        if 'autosave_tracedata_00.gh' in list_df['need_file'].values:
            ftp_name.retrbinary('RETR autosave_tracedata_00.gh',
                                open('c:/dyn_trace_temp/' + machine + '_autosave_tracedata_00.gh', 'wb').write)
             # 불러온 gh 파일을 csv로 변환
            chg_csv(machine)
            # graph 생성
            graph(machine)
            # rename trace file
            new_name = 'autosave_tracedate_'+now_year()+list_df.loc[1,'month']+list_df.loc[1,'day']+'_'+list_df.loc[1,'time']+'.gh'
            ftp_name.rename('autosave_tracedata_00.gh', new_name)

            ftp_name.close()
        else:
            print("#. 새로 받아진 trace file이 없습니다.")
            print("#. 호기명을 입력하여 주세요 ex) 601, 750, 804, 003")
            print("#. 종료하고 싶은경우 q를 입력하세요")
            ftp_name.close()

### main script ###
print("#. Dynamic Trace view v1.0 입니다. 2020.10, LTH")
print("#. autosave_tracedata_00 받아진 설비 기준입니다.")
print("#. 호기명을 입력하여 주세요 ex) 601, 750, 804, 003")
print("#. 종료하고 싶은경우 q를 입력하세요")
######

# 파일이 있는지 확인하고 없으면 만들어 준다
try:
    os.mkdir("c:\dyn_trace_temp")
except FileExistsError as e:
    pass

# 임시 생성된 파일을 전부 삭제 진행해준다.
# 하위 폴더만 지우고 싶은데 다지우네 다시 확인 필요
# shutil.rmtree(r"c:\err_view_temp")

# 딕셔너리로 키값과 valure 값을 가져온다
machines = {}


# 다운받을 호기명을 입력
while True:
    machine = input()
    if machine == 'q' or machine == 'Q':
        break
    try:
        split_info = machines[machine]
    except KeyError as e:
        print("일치하는 호기가 없습니다. 다시 입력해주세요")
        print("#. 종료하고 싶은경우 q를 입력하세요")
    else:
        if split_info[2] == 'ASML':
            type_machine = asml_pas(split_info)
        else:
            print("아직 작업중입니다.")