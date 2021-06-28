import basic
import os
import platform

print('+------------------------------------------------------+')
print('|              Pengerjaan Kelompok 1                   |')
print('+------------------------------------------------------+')
print("| Operating System : " + platform.system() +
              "                         []|")
print("| Release          : " + platform.release() +
              "                              []|")
print('+------------------------------------------------------+\n')


while True:

    text = input('Input_Nilai ~ ')
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        print(repr(result))
