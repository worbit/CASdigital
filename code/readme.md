## Python Installation
Most of the code should work with a basic [Anaconda](https://anaconda.org) installation. Except for some missing parenthesis in print statements, all scripts should work with both Python 2.7 and 3.6

## IfcOpenShell for BIM examples
On my Mac, it worked straight away with installing it following [these instructions](https://github.com/IfcOpenShell/IfcOpenShell#installing-ifcopenshell-with-conda). However, on Windows systems, IfcOpenShell had conflicts with libraries such as NLTK. A working approach is this:
* close both `Spyder` and `Navigator`
* reopen `Navigator`
* choose the `Environments`-tab on the left
* click `Create` in the bottom left corner
* give the new environment a `<name>` you remember and click `Create`
* open `Anaconda Prompt`
* type `activate <name>` and hit enter
* then follow [these instructions](https://github.com/IfcOpenShell/IfcOpenShell#installing-ifcopenshell-with-conda)
* in `Navigator` switch back to the `Home` tab, search for `Spyder` and click `Install`

## Additional Resources
* Main Page: http://ifcopenshell.org
* Forum: https://sourceforge.net/p/ifcopenshell/discussion/
* Academy (currently offline?): http://academy.ifcopenshell.org
* Blog: http://blog.ifcopenshell.org/
