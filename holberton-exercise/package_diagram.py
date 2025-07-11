
# package name
"""
1, the tab in the upper left corner is used for displaying the name of the package diagram. 
2, the contents (members) of package are shown in the main rectangle. 
3, members of package can also be shown outside the rectangle (with a plus sign within the circle)
4, members of package can be public(+) or private(-). 
"""

# Packageable element(has a name, can be directly placed inside a package)
"""
Type, Classifier, Class, Use Case, Component, Package, Constraint, Dependency, Event  

"""

# Dashed Arrow
"""
in a package diagram, arrow starts from user (the dependent)
                      points to provider (the package being depended on)
For example, if package A needs something from package B, draw arrow from A to B
A -------------> B
"""

# Arrow with empty triangle heads represent generalization (inheritance-like) relationships.
"""
Generalization arrow points from child to parent. 
parent: abstract package: it defines general rules, interfaces or common behavior for different types
        of ..., but does not implememt details itself.
child: concrete package: it provides specific implementations of ..., each in their own way. 

For example:
Direction:
Random Storage ─────▷ External Storage ("Random Storage" is a kind of "External Storage")


"""

# Syntax of a fully qualified name
"""
NameOwingThePackage::NameOfThePackage

for example: java::util::Date
jave owns util, util owns Date (Date is inside util, util is inside java)
"""

# import and access
"""
Diagram: (Package is user, Package2 is provider)
Package --<<import>>--> Package2 (Package imports all the features of Packege2)

Diagram: (Package is user, Package2 is provider)
Package --<<access>>--> Package2 (Packsge can use some features of Package2)

"""
