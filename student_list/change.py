import os

#해당 폴더로 들어간다
os.chdir("/home/ubuntu/workspace/monday/student_list")

#폴더 안의 모든 파일을 돌면서 이름을 바꾼다.

for filename in os.listdir("."):
    os.rename(filename, filename.replace("student","mc"))