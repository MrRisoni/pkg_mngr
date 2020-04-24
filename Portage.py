import os,fnmatch,json


class Portage:



    def __init__(self):
        self.REPO_PATH = 'repository'
        self.PKG_ENDING = '.json'

        raw = [x.strip() for x in open('installed', 'r').readlines()]
        self.installed = {}
        for r in raw:
            details = r.split('::');
            #print (details)
            self.installed[details[0]] = [details[1]]
        print (self.installed)

    def versionCompare(self,installed,operator,needed):
        # unit test this
        #print ('version compare')
        #print (installed,operator,needed)
        version_rules = needed.split('.')
        major_needed = version_rules[0]
        minor_needed = version_rules[1]
        revision_needed = version_rules[2]

        installed_rules = installed[0].split('.')
        version_rules_installed = installed_rules
        major_installed = version_rules_installed[0]
        minor_installed = version_rules_installed[1]
        revision_installed = version_rules_installed[2]

        print (version_rules_installed)
        print (version_rules)
        needs_update = False

        if major_needed > major_installed:
            needs_update = true
        #if major_needed >=  major_installed &&    



    def installPackage(self,pkgItm):
        details = pkgItm.name.split('/')
        if details[1] not in self.installed:
            print ('Needs pkg ' + pkgItm.name + ' ' + pkgItm.operate + ' ' + pkgItm.pattern)
        else:
            # check version
            self.versionCompare(self.installed[details[1]],pkgItm.operate,pkgItm.pattern)

    def installOrder(self,packages):
        for pkg in packages:
            for dep in pkg.depends:
                self.installPackage(dep)



    def search(self, search_term):
        print ('Searching for ' + search_term)
        #print self.REPO_PATH
        result = []
        for root, dirs, packages in os.walk(self.REPO_PATH):
            for each_package in packages:
                #print each_package
                #if fnmatch.fnmatch(each_package, search_term):
                if search_term in each_package:
                    #result.append(os.path.join(root, search_term))
                    pgk_build_file = os.path.join(root, each_package)
                    #print pgk_build_file

                    pkg_contents = {}
                    with open(pgk_build_file, 'r') as file:
                        json_str = file.read().replace('\n', '')
                        pkg_contents = json.loads(json_str)
        print (pkg_contents)
