import sys
from Portage import Portage
options = ['s']


p =  Portage()


if len(sys.argv) ==1:
    print 'No arguments.Valid arguments are'
    print options
else:
    #args_list = sys.argv.split(' ')
    #print args_list
    args_list = sys.argv[1:]
    print args_list
    p.search(args_list[0])
