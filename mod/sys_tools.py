from os.path    import isfile
from sys        import argv, exit
from os         import remove
from mod.consts import usage

# ==========.==========

# Usage  for command line :
# python3 crpt.py  alb.jpg "my key"
def check_argv(argv, in_key):
    # arg = argv
    if len(argv) < 3:  # 3 arguments in command line
        print("Not enougth arguments.")
        print(usage)
        exit(0)

    out_key = argv[2]  # check command line key
    # argv[2] is the out_key
    if len(out_key) < 2 or len(out_key) > 15:
        # out key is the client kev given in command line : argv[2]
        print("Error in out_key.")
        print(usage)
        exit(0)

    return out_key + in_key  # crypt out key + inner key

# ==========.==========

def file_to_crypt(argv, suf):
    
    if argv[0] == argv[1]:
        # it' not safe  to crypt machine so exit
        print("You cannot crypt the crypt machine.")
        print(usage)
        exit(0)
   
    in_f = argv[1] # file to be crypted
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    if not isfile( in_f ): # in_f does not exist ?
        print(f"{in_f} does not exists : check usage") # in_f dont exists
        print(usage)
        exit(0)
    
    # here in_f exist
    if in_f.endswith(suf):  # suf is ".crypted"
        # f exist and finish with '.crypted'
        out_f = in_f.replace(suf, "") 
    else: 
        # in_f exist and does not ends with suf
        out_f = in_f + suf
    
    if isfile(out_f):  # danger, out_f will be overwritten
        print(f"Process is stoped : {out_f} yet exists.")
        print(usage)
        exit(0)
        
    return [in_f, out_f] # return file to crypt and file crypted

# ==========.==========

def start(argv):
    a = argv[1]
    if a == '-v' or a == " --version" or a == " -V" or a == "VERSION":
        print( "crpt.py is a crypt machine, version 1.5")
        exit(0)
    
    elif a == '-h' or a == "--help" or a == "-H" or a == "HELP":
        print(usage,  '''  
                crypt Help
    
    python3 crpt.py is the crypt machine
    "path is the file path of the file to crypt" 
    "out crypt key" is the client key for crypting and uncrypting.
    len of "out crypt key" must be  2 <= len <= 15
    The name of the crypted file will be path.crypted\n
    To uncrypt apply the crypt machine on the cypted file
    Like that : python3 crpt.py path.crypted "out crypt key"
    It's important to keep on the initial key to uncrypt file
    Initial cripted file have cannot be in the folder for uncrypting
    
    Mail me at : franck.corniquet@gmail.com
    Bye
    ''')   
        exit(0)
        
# ==========.==========
        
def bye_crypt(in_out_f):
    # say bye : end of crypt
    print("----------.----------.---------.----------"   )
    print(f"CRYPT DONE: crypt({in_out_f[0]}) -> {in_out_f[1]}" )
    print( "Mail me at : franck.corniquet@gmail.com\nBye")    
    print("----------.----------.----------.----------"  )