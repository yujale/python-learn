# 读取文件,监控文件读取过程
try:
    file = open('test.py', 'r')
    try:
        while True:
            content = file.read(3)
            if content == '':
                break
            print(content)

    except Exception:
        print('读取出现异常,强行终止')
    finally:
        print('关闭文件')
        file.close()

except Exception:
    print('没有该文件')