import ftplib
import os
import test.test_shutil
# 시간 딜레이 주기 위해
import time, datetime
import pandas as pd
# 파일 수정 함수 불러오기
from file_modify import chg_csv
# graph 함수 불러오기
from visualize import graph

# pas 호기명 입력 받은 후 ftp를 이용한 process 진행
def asml_pas(split_info):
    # ftp 접속
    try:
        ftp_name = ftplib.FTP(split_info[1], split_info[0], 'ftp')
    except TimeoutError as e:
        print("#. 설비에 접속할수 없습니다.")
        print("#. 다시접속하거나 다른 호기에 접속하여 주세요")
    else:
        # ftp서버에서 파일다운로드 server_url은 ftp상의파일경로 [예: /home/server/html_public/index.htm ]
        # local_url은 자신의 파일경로 [예: c:\html\working\index.htm ]

        # ftp / SWAD 폴더 접속
        ftp_name.cwd('/usr/asm/data.0000/service_data/SW/SWAD')
        # bring file list
        file_list = ftp_name.nlst()
        # test1 = []
        # ftp_name.dir('-t', '/usr/asm/data.0000/service_data/SW/SWAD', test1.append)
        # latest_file_path="""ftp://"""+config['user']+""":"""+config['password']+"""@"""+config['host']+"""/""" + list_of_files[0][56:]   df_from_csv=pd.read_csv(latest_file_path, sep=""",""",   skiprows=index_row_to_start, dtype=np.object_)
       
        if 'autosave_tracedata_00.gh' in file_list:
            ftp_name.retrbinary('RETR autosave_tracedata_00.gh',
                                open('c:/dyn_trace_temp/' + machine + '_autosave_tracedata_00.gh', 'wb').write)
            # 불러온 gh 파일을 csv로 변환
            chg_csv(machine)
            # graph 생성
            # graph(machine)

            # 이름 바꿔서 넣기 해야함
            # create_time = datetime.datetime.fromtimestamp(os.path.getctime('RETR autosave_tracedata_00.gh'))
            # print(create_time)
            # print(str(create_time.year) + str(create_time.month) + str(create_time.day) + "_" + str(create_time.hour) + str(create_time.minute))

            # ftp의 연결을 끊습니다
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