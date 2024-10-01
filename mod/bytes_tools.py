"""
function list of that module
============================

int_to_hex_arr(arr):    
                convert int to byte array
                The argument is an array : arr
                return an array: ar

file_to_byte_arr(path, limit) : 
                convert a file into array of bytes
                the argument : the path of the file
                limit usefull in develop phase only
                return an array of bytes
                    
file_to_int_arr(path, limit)                     
                convert a file to an array of int
                the argument : path : path of the file
                limit no usefull will be removed for exploitation
                after red file return an array of int                                   
 
file_to_int_xor(path, key, limit):
                convert a file to an 'xor'ed array of int 
                so the array is crypted yet
                limit : during development only
                2 arguments : path of file and the crypt key
                This function return the array crypted

arr_xor_arr(ar, key):  
                This function convert an array to an other 
                after being xor'ed
                2 arguments : path of file and the crypt key
                ar is an array  and key is a string
                This function return an array crypted
         
arr_to_file (path ,ar)
                save hex arr on file
                The array ar must be writen in hex format (!!)                

def crypt_file(path, key, suf, limit): 
                crypt from file "path" to file "path+suf" (suffixe)
                path is the path of the file
                key is the crypt key and suf is ".cypted"

inc_iter(j, len_key):
                that's the incrementor of the position key.
                j has to be defined and set to 0 previously.
                
"""


# convert int to byte array
# arr is the array of int to convert
# ar is the array returned of hex elements
def int_to_hex_arr(arr):  # arr is the array to transform
    ar = []  # init
    for i in arr:
        # ar is the array   transformed in Hex values
        ar.append(int.to_bytes(i, 1, "big"))
    return ar  # return the hex element array


# convert a file to an array of bytes
# for development only : limit the array len of bytes
def file_to_byte_arr(path, limit):
    i, ar = 0, []  # ar is the returned array
    f = open(path, "rb")
    data = f.read(1)
    while data and i < limit:
        ar.append(data)  # data in bytes
        data = f.read(1)  # read again
        i += 1  # limitation of array length
    f.close()
    return ar


# convert a file to an array of int
# for development only : limit the array len of bytes
def file_to_int_arr(path, limit):
    i, ar = 0, []  # ar is the returned array
    f = open(path, "rb")
    data = f.read(1)
    while data and i < limit:  # limit is not usefull remove it later
        x = int.from_bytes(data, "big")  # hex to int
        ar.append(x)  # data in int
        data = f.read(1)  # read again
        i += 1  # limitation of array length
    f.close()
    return ar


# return array of 'xor'ed from file path
# remove limit ; limit is  onnly to limit lenght of the array
# and during development
def file_to_int_xor(path, key, limit):  # cript
    f = open(path, "rb")
    data = f.read(1)  # initialise data
    i, j, ar, len_key = 0, 0, [], len(key)  # temporary var and iterator initialisation

    while data and i < limit:  # i is temporary var to remove in exploitation
        x = int.from_bytes(data, "big")  # bytes to int xor
        ar.append(x ^ ord(key[j]))
        j = inc_iter(j, len_key)  # go on the key next pos
        data = f.read(1)  # read file till limit
        i += 1
    f.close()
    return ar  # end of crypt function


# This function below convert an array to an other after being xor'ed
# so xor function is used
# ar is an array  and key is a string
def arr_xor_arr(ar, key):
    # rsl i the result of ar^key operation
    j, rsl, len_key = 0, [], len(key)  # initialise  the function
    for i in ar:  # ar define as the variable input
        rsl.append(i ^ ord(key[j]))  # full the result
        # print(i ^ ord(key[j]))
        j = inc_iter(j, len_key)
    return rsl


# save hex_arr on file
# ar must be writen in hex format
def arr_to_file(path, ar):  # save file
    g = open(path, "wb")  # open to write
    for i in ar:  # all elements of ar
        g.write(i)
    g.close()


# crypt from file "path"
# path is the path of the file : in_out_f[0] : in
# key is the crypt key and suf is ".cypted"
def crypt_file(path, out_f, key, suf, limit):
    # file -> crypt array with xor operator result
    int_crypted_arr = file_to_int_xor(path, key, limit)   
    # int -> hex array
    hex_crypted_arr = int_to_hex_arr(int_crypted_arr)
    # now reverse the int_crypted_arr
    # It's necessary to shuffes the cards a little bit more
    int_crypted_arr.reverse()    
    # save the cryped aff -> file    
    arr_to_file(out_f, hex_crypted_arr)


# that's the incrementor of the key position
# j index of key string
def inc_iter(j, len_key):
    j += 1
    if j >= len_key:
        j = 0  # back to 0 if j > len_key
    return j
