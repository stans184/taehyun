# 파일 열기 test 버전
# C:\K\UTILITY\AcroEdit.exe D:\SFTest.log
# ftp 실행하기 위해
import ftplib
# 파일 디렉토리 확인 및 만들어 주기 위해
import os
# 파일 삭제를 위해
import shutil
# 키보드 컨트롤을 위해
import pyautogui
# 시간 딜레이 주기 위해
import time

# 해당 설비가 pas일때 호출하는 함수
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
            ftp_name.retrbinary('RETR /usr/asm/data.0000/.ER/ER_event_log',
                                open('c:/err_view_temp/' + machine + '_error.txt', 'wb').write)
            # ftp의 연결을 끊습니다
            ftp_name.close()
            break
    type_machine = "C:\Program Files (x86)\AcroSoft\AcroEdit\AcroEdit.exe C:\err_view_temp\\" + machine + "_error.txt"
    return type_machine

# 해당 설비가 twin일때 호출하는 함수
def twin(split_info):
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
            ftp_name.retrbinary('RETR /usr/asm/data.0000/.ER/ER_event_log',
                                open('c:/err_view_temp/' + machine + '_error.txt', 'wb').write)
            # ftp의 연결을 끊습니다
            ftp_name.close()
            break
    type_machine = "C:\Program Files (x86)\AcroSoft\AcroEdit\AcroEdit.exe C:\err_view_temp\\" + machine + "_error.txt"
    return type_machine

# 해당 설비가 canon일때 호출하는 함수
def canon(split_info):
    # ftp 접속
    while True:
        try:
            ftp_name = ftplib.FTP(split_info[1], 'ifour', 'ifour22')
        except TimeoutError as e:
            print("설비에 접속할수 없습니다.")
            print("다시접속하거나 다른 호기에 접속하여 주세요")
        else:
            # ftp서버에서 파일다운로드 server_url은 ftp상의파일경로 [예: /home/server/html_public/index.htm ]
            # local_url은 자신의 파일경로 [예: c:\html\working\index.htm ]
            ftp_name.retrbinary('RETR /console/i4/work/misc/ERR/error10k.log',
                                open('c:/err_view_temp/error.txt', 'wb').write)
            # ftp의 연결을 끊습니다
            ftp_name.close()
            # 파일을 읽어서 다시만들기
            myFile = open("C:\err_view_temp\error.txt", "r")
            res = myFile.read()
            myFile.close()
            f = open("C:\err_view_temp\error_edit.txt", 'w')
            f.write(res)
            f.close()
            f = open("C:\err_view_temp\error_edit.txt", 'a')
            f.write('last line')
            f.close()
            with open('C:\err_view_temp\error_edit.txt', 'r') as f:  # 파일을 열어서
                # 개행으로 split후 각각의 리스트를 공백을 기준으로 나눔.
                line = f.readline()
                phone_list = map(lambda x: x.split(), f.read().split('\n'))
            sorted_list = sorted(phone_list, reverse=True, key=lambda x: (x[0], x[1]))
            f.close()
            f = open("C:\err_view_temp\\" + machine + "_error.txt", 'w')
            for i in range(0, len(sorted_list) - 1):
                error_msg = str()
                for j in range(5, len(sorted_list[i])):
                    error_msg = error_msg + sorted_list[i][j] + " "
                try:
                    print_check = "{0} {1} {2:<8}{3:<28}{4:<10}{5:<83}".format(sorted_list[i][0], sorted_list[i][1],
                                                                               sorted_list[i][2], sorted_list[i][3],
                                                                               sorted_list[i][4], error_msg)
                    f.write(print_check)
                    f.write('\n')
                except IndexError as e:
                    pass
            f.close()
            break
    type_machine = "C:\Program Files (x86)\AcroSoft\AcroEdit\AcroEdit.exe C:\err_view_temp\\" + machine + "_error.txt"
    return type_machine

print("1. Error log view v2.0 입니다. 20.04.16")
print("2. C:\Program Files (x86)\AcroSoft\AcroEdit 에 acroedit가 있어야 합니다.")
print("3.호기명을 입력하여 주세요 ex) 601, 750, 803, 003")
print("4.종료하고 싶은경우 q를 입력하세요")

# 파일이 있는지 확인하고 없으면 만들어 준다
try:
    os.mkdir("c:\err_view_temp")
except FileExistsError as e:
    pass

# 임시 생성된 파일을 전부 삭제 진행해준다.
# 하위 폴더만 지우고 싶은데 다지우네 다시 확인 필요
# shutil.rmtree(r"c:\err_view_temp")

# 딕셔너리로 키값과 valure 값을 가져온다
machines = {}
machines['806'] = ['ftp.7407', '12.24.82.46', 'TWIN']
machines['811'] = ['ftp.6351', '12.24.82.51', 'TWIN']
machines['817'] = ['ftp.9175', '12.24.82.57', 'TWIN']
machines['818'] = ['ftp.4087', '12.24.82.58', 'TWIN']
machines['845'] = ['ftp.5594', '12.24.181.218', 'TWIN']
machines['717'] = ['ftp.7407', '12.24.72.33', 'TWIN']
machines['742'] = ['ftp.6351', '12.24.72.145', 'TWIN']
machines['747'] = ['ftp.9175', '12.24.72.217', 'TWIN']
machines['752'] = ['ftp.4087', '12.24.72.99', 'TWIN']
machines['754'] = ['ftp.5594', '12.24.174.77', 'TWIN']
machines['69'] = ['ewl', '12.24.66.205', 'EWL']
machines['70'] = ['ewl', '12.24.66.88', 'EWL']
machines['73'] = ['ewl', '12.24.63.53', 'EWL']
machines['74'] = ['ewl', '12.24.66.134', 'EWL']
machines['812'] = ['mcsv', '12.24.83.150', 'NIKON']
machines['813'] = ['mcsv', '12.24.83.149', 'NIKON']
machines['669'] = ['mcsv', '12.24.63.167', 'NIKON']
machines['605'] = ['mcsv', '12.24.63.171', 'NIKON']
machines['674'] = ['mcsv', '12.24.63.168', 'NIKON']
machines['675'] = ['mcsv', '12.24.63.195', 'NIKON']
machines['p01'] = ['mcsv', '12.24.172.250', 'LABEL']
machines['p02'] = ['mcsv', '12.24.64.116', 'LABEL']
machines['p03'] = ['mcsv', '12.24.162.93', 'LABEL']
machines['p04'] = ['mcsv', '12.24.65.170', 'LABEL']
machines['801'] = ['ftp.4772', '12.24.82.41', 'ASML']
machines['804'] = ['ftp.4349', '12.24.82.44', 'ASML']
machines['807'] = ['ftp.7829', '12.24.82.47', 'ASML']
machines['810'] = ['ftp.8059', '12.24.82.50', 'ASML']
machines['826'] = ['ftp.4011', '12.24.82.66', 'ASML']
machines['827'] = ['ftp.4598', '12.24.82.67', 'ASML']
machines['828'] = ['ftp.9815', '12.24.82.68', 'ASML']
machines['829'] = ['ftp.3570', '12.24.82.69', 'ASML']
machines['841'] = ['ftp.8861', '12.24.82.141', 'ASML']
machines['003'] = ['ftp.6545', '12.24.108.19', 'ASML']
machines['005'] = ['ftp.9831', '12.24.108.110', 'ASML']
machines['006'] = ['ftp.6303', '12.24.108.162', 'ASML']
machines['833'] = ['ftp.3700', '12.24.82.73', 'ASML']
machines['837'] = ['ftp.4506', '12.24.82.77', 'ASML']
machines['809'] = ['ftp.7703', '12.24.82.49', 'ASML']
machines['831'] = ['ftp.4255', '12.24.82.71', 'ASML']
machines['838'] = ['ftp.4371', '12.24.82.78', 'ASML']
machines['846'] = ['ftp.8097', '12.24.82.144', 'ASML']
machines['601'] = ['ftp.8900', '12.24.164.50', 'ASML']
machines['608'] = ['ftp.4227', '12.24.62.84', 'ASML']
machines['609'] = ['ftp.3427', '12.24.63.237', 'ASML']
machines['610'] = ['ftp.6588', '12.24.62.80', 'ASML']
machines['615'] = ['ftp.6371', '12.24.63.212', 'ASML']
machines['616'] = ['ftp.8411', '12.24.63.93', 'ASML']
machines['624'] = ['ftp.9444', '12.24.62.221', 'ASML']
machines['627'] = ['ftp.6241', '12.24.63.34', 'ASML']
machines['629'] = ['ftp.5030', '12.24.63.41', 'ASML']
machines['632'] = ['ftp.8975', '12.24.66.34', 'ASML']
machines['634'] = ['ftp.5756', '12.24.165.182', 'ASML']
machines['636'] = ['ftp.3223', '12.24.63.49', 'ASML']
machines['640'] = ['ftp.8189', '12.24.62.255', 'ASML']
machines['642'] = ['ftp.7172', '12.24.165.58', 'ASML']
machines['643'] = ['ftp.9616', '12.24.63.233', 'ASML']
machines['648'] = ['ftp.9627', '12.24.62.149', 'ASML']
machines['655'] = ['ftp.5031', '12.24.63.200', 'ASML']
machines['656'] = ['ftp.4858', '12.24.164.104', 'ASML']
machines['657'] = ['ftp.7457', '12.24.62.114', 'ASML']
machines['658'] = ['ftp.6152', '12.24.66.29', 'ASML']
machines['660'] = ['ftp.9731', '12.24.62.158', 'ASML']
machines['661'] = ['ftp.4438', '12.24.62.203', 'ASML']
machines['662'] = ['ftp.9211', '12.24.62.25', 'ASML']
machines['663'] = ['ftp.8677', '12.24.165.214', 'ASML']
machines['665'] = ['ftp.5280', '12.24.62.207', 'ASML']
machines['666'] = ['ftp.8389', '12.24.164.151', 'ASML']
machines['703'] = ['ftp.3202', '12.24.73.128', 'ASML']
machines['705'] = ['ftp.5102', '12.24.73.130', 'ASML']
machines['706'] = ['ftp.9867', '12.24.73.131', 'ASML']
machines['713'] = ['ftp.6674', '12.24.73.132', 'ASML']
machines['714'] = ['ftp.3808', '12.24.73.133', 'ASML']
machines['715'] = ['ftp.3470', '12.24.73.134', 'ASML']
machines['716'] = ['ftp.3589', '12.24.175.156', 'ASML']
machines['717'] = ['ftp.6918', '12.24.72.33', 'ASML']
machines['718'] = ['ftp.7752', '12.24.73.99', 'ASML']
machines['720'] = ['ftp.5027', '12.24.174.73', 'ASML']
machines['722'] = ['ftp.4290', '12.24.76.117', 'ASML']
machines['724'] = ['ftp.9811', '12.24.73.104', 'ASML']
machines['725'] = ['ftp.7354', '12.24.175.173', 'ASML']
machines['727'] = ['ftp.7259', '12.24.72.199', 'ASML']
machines['728'] = ['ftp.9449', '12.24.175.163', 'ASML']
machines['729'] = ['ftp.8123', '12.24.73.137', 'ASML']
machines['734'] = ['ftp.5516', '12.24.174.206', 'ASML']
machines['735'] = ['ftp.5783', '12.24.175.189', 'ASML']
machines['737'] = ['ftp.6955', '12.24.76.206', 'ASML']
machines['739'] = ['ftp.6785', '12.24.76.194', 'ASML']
machines['741'] = ['ftp.4725', '12.24.76.184', 'ASML']
machines['742'] = ['ftp.6891', '12.24.72.145', 'ASML']
machines['743'] = ['ftp.8254', '12.24.76.48', 'ASML']
machines['744'] = ['ftp.4722', '12.24.174.239', 'ASML']
machines['747'] = ['ftp.4330', '12.24.72.217', 'ASML']
machines['750'] = ['ftp.6477', '12.24.73.216', 'ASML']
machines['751'] = ['ftp.6194', '12.24.73.135', 'ASML']
machines['752'] = ['ftp.5508', '12.24.72.99', 'ASML']
machines['754'] = ['ftp.9738', '12.24.174.77', 'ASML']
machines['756'] = ['ftp.6938', '12.24.72.142', 'ASML']
machines['757'] = ['ftp.4244', '12.24.174.115', 'ASML']
machines['758'] = ['ftp.4384', '12.24.76.34', 'ASML']
machines['759'] = ['ftp.5062', '12.24.72.118', 'ASML']
machines['603'] = ['ifour', '12.24.66.204', 'CANON']
machines['604'] = ['ifour', '12.24.66.209', 'CANON']
machines['612'] = ['ifour', '12.24.63.98', 'CANON']
machines['613'] = ['ifour', '12.24.66.103', 'CANON_ES5']
machines['617'] = ['ifour', '12.24.63.154', 'CANON_ES6']
machines['619'] = ['ifour', '12.24.66.117', 'CANON_ES5']
machines['620'] = ['ifour', '12.24.66.36', 'CANON']
machines['638'] = ['ifour', '12.24.63.220', 'CANON']
machines['641'] = ['ifour', '12.24.63.221', 'CANON']
machines['645'] = ['ifour', '12.24.62.126', 'CANON']
machines['664'] = ['ifour', '12.24.62.206', 'CANON']
machines['701'] = ['ifour', '12.24.76.118', 'CANON']
machines['704'] = ['ifour', '12.24.76.79', 'CANON']
machines['730'] = ['ifour', '12.24.175.166', 'CANON']
machines['732'] = ['ifour', '12.24.76.105', 'CANON']
machines['733'] = ['ifour', '12.24.76.115', 'CANON']
machines['745'] = ['ifour', '12.24.175.160', 'CANON']
machines['755'] = ['ifour', '12.24.73.155', 'CANON']
machines['802'] = ['ifour', '12.24.82.42', 'CANON']
machines['803'] = ['ifour', '12.24.82.43', 'CANON']

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
        elif split_info[2] == 'CANON':
            type_machine = canon(split_info)
        elif split_info[2] == 'TWIN':
            type_machine = twin(split_info)
        else:
            print("아직 작업중입니다.")
        # 파일 실행시키기
        pyautogui.hotkey('win', 'r')
        # 너무 빨리치면 error 날까봐 delay
        time.sleep(0.5)
        pyautogui.typewrite(type_machine)
        time.sleep(0.1)
        pyautogui.press('enter')