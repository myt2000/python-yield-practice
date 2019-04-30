from tempfile import TemporaryFile


def temp_file_test():
    temp = TemporaryFile()
    print(temp)
    print(temp.name)
    # 写入缓冲区
    temp.write(b'hello\nworld')
    temp.seek(0)
    print(temp.read())
    temp.close()


if __name__ == "__main__":
    temp_file_test()