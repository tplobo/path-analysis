# **PathAnalysis** package for ANSYS Mechanical
Extension package for ANSYS Mechanical for computing and exporting stress and temperature analyses along linear paths.

***
### Introduction
This package was developed as a simple (_i.e._ quick and dirty) tool to compute and export stress and temperature analyses along linear paths between a point and surface pair selected in ANSYS Mechanical.

This has the aim of producing analyses necessary for licensing pressure vessels under some regulations (_e.g._ TBD).

***
### Installation
To install this package in your local ANSYS Mechanical, simply copy the contents of the `extensions` folder into the directory of same name that can be found in:
```
C:\Users\<username>\AppData\Roaming\Ansys\<version>\ACT\extensions\
```
Don't forget to substitute `<username>` and `<version>`!

***
### Usage
After installation, the extension must be loaded in the Workbench toolbar:
`Extensions > Extensions Manager`
by enabling the check-box for **PathAnalysis**. A menu of the same name should appear in the toolbar of your results visualization window (_i.e._ not in the workbench).

To use the extension:
1. first create **named selections** for both a node and a surface in your results visualization window;
2. then click the **Path** button (route icon) in the toolbar to create the shortest path between them;
3. then click the **Calculate** button (calculator icon) to compute the stress and temperature analysis summaries and export them as a CVS file on your Desktop.

The **Calculate** button can perform its action for multiple paths,  so steps 1 and 2 can be repeated as many times as necessary.
The **Delete** button (paper shreder icon) can be used to delete analysis solutions for all paths.

The example file `ANSYS_PathAnalysis_Example.wbpz` in the repo can be used to test the extension after it has been installed and enabled.
It contains a named Node and a named Surface that can define a path, in a simple geometry loaded with a simple temperature distribution.

***
### Development
The extension is a simple set of files: one .XML for configuring the toolbar and a few .PY to define the functions necessary to runits features.

If you intend to modify the package, it might be a good idea to enable the debugging mode in the ANSYS Mechanical GUI. To do so, in the Workbench toolbar:
`Tools > Options > Extensions`
enable the check-box for **Debug Mode**.

For more information on how to make your own extensions for ANSYS, please refer to [the ANSYS ACT Developers Guides](https://catalog.ansys.com/Developers.cshtml)
