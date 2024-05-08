"""
 append_string.py
 Created on Tue Jul 11 2023
 @author: S.OHSAWA 
 
 指定したディレクトリ内の特定のファイル名の後ろに文字列を追加する
 PyInstallerやNuitkaでexe化することを想定している

"""

import os
import glob

def main():
    dire = input('Enter the path of the target directory:')
    file_name = input('Enter the characters contained in the target file:')

    target_dire = glob.glob(f'{dire}/*{file_name}*')
    print(target_dire)
    
    string = input('Enter a string to be appended:')

    for fn in target_dire:
        new_fn = fn[:-4] + string + fn[-4:]
        os.rename(fn, new_fn)
        

if __name__ == '__main__':
    main()

