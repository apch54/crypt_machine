from mod.bytes_tools import file_to_int_arr, crypt_file, file_to_int_xor
from sys import argv
from mod.sys_tools import check_argv, file_to_crypt, bye_crypt, start
from mod.consts import *

start(argv)  # handle -v or -h
key = check_argv(argv, in_key)  # verifying the command line

# in_out_f is an array of file name
# strings  = [file to crypt, file to be crypted]
in_out_f = file_to_crypt(argv, suf)

# crypt in_out_f[0] -> in_out_f[1]
crypt_file(in_out_f[0], in_out_f[1], key, suf, limit)
# to check with uncrypting  open saveI

# say bye to crypt giving the name of the crypted file
bye_crypt(in_out_f)
