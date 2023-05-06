import os
import subprocess


class cmpFile:

    def __init__(self, file_in, file1, file2):
        self.file_in = file_in
        self.file1 = file1
        self.file2 = file2

    def fileExists(self):
        if os.path.exists(self.file_in) and os.path.exists(self.file1) and os.path.exists(self.file2):
            return True
        else:
            return False

    # 对比文件不同之处, 并返回结果
    def compare(self):
        if not cmpFile(self.file_in, self.file1, self.file2).fileExists():
            return []
        fp0 = open(self.file_in)
        fp1 = open(self.file1)
        fp2 = open(self.file2)
        flist0 = [j for j in fp0]
        flist1 = [i for i in fp1]
        flist2 = [x for x in fp2]
        fp1.close()
        fp2.close()
        flines1 = len(flist1)
        flines2 = len(flist2)

        '''if flines1 < flines2:
            flist1[flines1:flines2 + 1] = ' ' * (flines2 - flines1)
        if flines2 < flines1:
            flist2[flines2:flines1 + 1] = ' ' * (flines1 - flines2)'''

        counter = 1
        cmpreses = []
        for x in zip(flist1, flist2):
            if x[0] == x[1]:
                counter += 1
                continue
            if x[0] != x[1]:
                cmpres = '%s和%s第%s行不同, 输入为 , 内容为: %s --> %s' % \
                         (self.file1, self.file2, counter, x[0].strip(), x[1].strip())
                cmpreses.append(cmpres)
                counter += 1
        return cmpreses


def execute_java(stdin, jar):
    cmd = ['java', '-jar', "-Xms128m", "-Xmx256m", jar]  # 更改为自己的.jar包名
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    success = True
    try:
        stdout, stderr = proc.communicate(stdin.encode(), timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        success = False
    if not success:
        raise
    return stdout.decode().strip()


def run():
    file_in = open('in.txt', 'r')
    inputStr = file_in.read()
    outputStr1 = execute_java(inputStr, 'code1.jar')
    outputStr2 = execute_java(inputStr, 'code2.jar')
    file_out1 = open('out1.txt', 'w')
    file_out1.write(outputStr1)
    file_out2 = open('out2.txt', 'w')
    file_out2.write(outputStr2)
    file_in.close()
    file_out1.close()
    file_out2.close()


def cmp():
    # os.system("in.txt | java -jar code1.jar | out1.txt")
    # os.system("in.txt | java -jar code2.jar | out2.txt")
    '''
    file = open('in.txt', 'r')
    inputStr = file.read()
    file.close()
    outputStr1 = execute_java(inputStr, 'code1.jar')
    outputStr2 = execute_java(inputStr, 'code2.jar')
    file = open('out1.txt', 'w')
    file.write(outputStr1)
    file.close()
    file = open('out2.txt', 'w')
    file.write(outputStr2)
    file.close()
    cmpfile = cmpFile('in.txt', 'out1.txt', 'out2.txt')
    difflines = cmpfile.compare()
    if len(difflines) == 0:
        return 1
    else:
        for i in difflines:
            print(i, end='\n')
        return 0
    '''
    run()
    file_in = open('in.txt', 'r')
    file_out1 = open('out1.txt', 'r')
    file_out2 = open('out2.txt', 'r')
    cnt = 0
    ans = True
    while True:
        a0 = file_in.readline()
        a1 = file_out1.readline()
        a2 = file_out2.readline()
        if not a1:
            break
        cnt = cnt + 1
        if a1 != a2:
            print("line:" + str(cnt) + " " + "input is " + str(a0).rstrip() + ", " + str(a1).rstrip() + " --> " + str(a2).rstrip())
            ans = False
        file_out1.readline()
        file_out2.readline()
    file_in.close()
    file_out1.close()
    file_out2.close()
    return ans

