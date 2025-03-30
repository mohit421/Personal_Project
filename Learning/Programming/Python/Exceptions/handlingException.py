try:
    x = 7/0

except Exception as e:
    print(e)

finally:
    print('Finally')