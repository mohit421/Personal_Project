import os 


# This error occurs because backslashes (\) in Windows file paths
#  can be interpreted as escape characters in Python strings 
# (e.g., \n for newline, \t for tab). In your path, \U starts 
# an invalid Unicode escape sequence.
# Python accepts forward slashes (/) in file paths, even on Windows.

# Add an r before the string to treat backslashes as literal characters
# os.chdir(r'C:\Users\Mohit Jaiswal\Videos\Pythons\OOPSByCoreySchafers')
# os.chdir('C:\\Users\\Mohit Jaiswal\\Videos\\Pythons\\OOPSByCoreySchafers')
os.chdir('C:/Users/Mohit Jaiswal/Videos/Pythons/OOPSByCoreySchafers')
# print(os.getcwd())


# for f in os.listdir():
#     print(f)


for f in os.listdir():
    # below will slip text and gives us every individual video in tuple
    # print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    # print(file_name.split(' '))
    f_title, f_course, f_num = f_name.split('-')
    # print(f_ext)
    # print('{}-{}-{}{}'.format(f_num,f_course,f_title,f_ext))
    new_name = '{}-{}-{}{}'.format(f_num,f_course,f_title,f_ext)
    os.rename(f,new_name)
    




