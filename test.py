import json
from PackageDescr.Package import Package
from PackageDescr.Dependency import Dependency
from PackageDescr.ChoiceDependency import ChoiceDependency

from PackageDescr.Choices import Choices



dp = Dependency("base-system/glibc", "gte", "4.6.*")
fftw = Dependency("general-margs/fftw", "lte", "4.*")

qt = ChoiceDependency("apps-gui/qt", "gte", "5.4.*", True)
gtk = ChoiceDependency("apps-gui/qtk", "gte", "3.6.*", False)

gui = Choices("gui",[qt, gtk], False)


pkg = Package("apps-media/rosegarden","I am","2020021822T34Z","5..6.7",[],[dp,fftw],[],gui)


json_data = json.dumps( pkg, default=lambda o: o.__dict__, indent=4,sort_keys=False)
print(json_data)
