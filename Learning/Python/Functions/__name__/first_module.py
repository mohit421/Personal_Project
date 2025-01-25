#  If __name__ =='__main__'

'''

The reason it is used because there is a code we only want to run 
and we running that as a main file 
and some file we wanna run when it been imported

'''
# print("First moudle's Name: {}".format(__name__))

# def main():
#     print("First moudle's Name: {}".format(__name__))

# if __name__ =='__main__':
#     print("Run Direcly")
# else:
#     print("Run from Import ")




print("this will always be run")
def main():
    print("First Module's main method ")

if __name__ =='__main__':
    main()
