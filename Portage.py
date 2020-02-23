import os,fnmatch,json


class Portage:



    def __init__(self):
        self.REPO_PATH = 'repository'
        self.PKG_ENDING = '.json'
        pass


    def search(self, search_term):
        print 'Searching for ' + search_term
        #print self.REPO_PATH
        result = []
        for root, dirs, packages in os.walk(self.REPO_PATH):
            for each_package in packages:
                #print each_package
                #if fnmatch.fnmatch(each_package, search_term):
                if search_term in each_package:
                    #result.append(os.path.join(root, search_term))
                    pgk_build_file = os.path.join(root, each_package)
                    print pgk_build_file

                    pkg_contents = {}
                    with open(pgk_build_file, 'r') as file:
                        json_str = file.read().replace('\n', '')
                        pkg_contents = json.loads(json_str)
        print pkg_contents
