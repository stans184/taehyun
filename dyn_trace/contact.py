# ftp 실행하기 위해
import ftplib
# 파일 디렉토리 확인 및 만들어 주기 위해
import os
# 파일 삭제를 위해
import shutil
# 키보드 컨트롤을 위해
import pyautogui
# 시간 딜레이 주기 위해
import time, datetime
def asml_pas(split_info):
    # ftp 접속
    while True:
        try:
            ftp_name = ftplib.FTP(split_info[1], split_info[0], 'ftp')
        except TimeoutError as e:
            print("설비에 접속할수 없습니다.")
            print("다시접속하거나 다른 호기에 접속하여 주세요")
        else:
            # ftp서버에서 파일다운로드 server_url은 ftp상의파일경로 [예: /home/server/html_public/index.htm ]
            # local_url은 자신의 파일경로 [예: c:\html\working\index.htm ]
            # ftp.cwd("받아올  파일 위치")
            # fd = open("./" + filename,'wb')
            # ftp.retrbinary("RETR " + filename, fd.write)
            # fd.close()
            ftp_name.retrbinary('RETR /usr/asm/data.0000/service_data/SW/SWAD/autosave_tracedata_00.gh',
                                open('c:/dyn_trace_temp/' + machine + 'trace.gh', 'wb').write)
            create_time = datetime.datetime.fromtimestamp(os.path.getctime('c:/dyn_trace_temp/' + machine + 'trace.gh'))
            ftp_name.rename('RETR /usr/asm/data.0000/service_data/SW/SWAD/autosave_tracedata_00.gh', 'RETR /usr/asm/data.0000/service_data/SW/SWAD/autosave_tracedata_' + create_time.year + create_time.month + create_time.day + create_time.hour + create_time.minute + '.gh')

            # ftp의 연결을 끊습니다
            ftp_name.close()
            break
    type_machine = "C:\Program Files (x86)\AcroSoft\AcroEdit\AcroEdit.exe C:\err_view_temp\\" + machine + "_error.txt"
    return type_machine

print("#. Dynamic Trace view v1.0 입니다. 2020.10, LTH")
print("#. 호기명을 입력하여 주세요 ex) 601, 750, 804, 003")
print("#. 종료하고 싶은경우 q를 입력하세요")

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
    else:
        if split_info[2] == 'ASML':
            type_machine = asml_pas(split_info)
        else:
            print("아직 작업중입니다.")
        # 파일 실행시키기
        pyautogui.hotkey('win', 'r')
        # 너무 빨리치면 error 날까봐 delay
        time.sleep(0.5)
        pyautogui.typewrite(type_machine)
        time.sleep(0.1)
        pyautogui.press('enter')