# What happen if we try to write from  within a file open in read mode
#  we have to have the file open in write mode
# with open('test.txt','r') as f:
#     f.write('Test')

#  this will create the file test2.txt inside Files directory
# with open('Files/test2.txt','w') as f:
#     pass



# with open('Files/test2.txt','w') as f:
#     f.write('Test')
#     f.seek(0)
#     # 2nd test overwrite first test
#     # f.write('TestOnefile')
#     f.write('e')


# with open('Files/test.txt','r') as rf:
#     with open('Files/test_copy.txt','w') as wf:
#         for line in rf:
#             wf.write(line)


#  if we waft to copy jpg/png then
#  we get an UnicodeDecodeError:- utf-8 codec con't decode byte 0xff in position 0, invalid start byte

#  this to work we have to open this file in binary mode
# with open('Files/Mohit.jpg','rb') as rf:
#     with open('Files/CopyMohit.jpg','wb') as wf:
#         for line in rf:
#             wf.write(line)

# other way to copy image
with open('Files/Mohit.jpg','rb') as rf:
    with open('Files/CopyMohit.jpg','wb') as wf:
        chunked_size = 4096
        rf_chunk = rf.read(chunked_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunked_size)