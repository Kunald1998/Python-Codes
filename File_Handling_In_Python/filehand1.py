def main():
    fd = open(file="marvellous.txt",mode="a")
    string = "DESHMANE"
    fd.write(string)
    fd.close()
    fd1 = open(file="marvellous.txt",mode="r")
    print(fd.read())

if __name__ == "__main__":
    main()
