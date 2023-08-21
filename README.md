# **PathAnalysis** package for ANSYS Mechanical
Extension package for ANSYS Mechanical for computing and exporting stress and temperature analyses along linear paths.

### Sharing
[![Repo](https://img.shields.io/badge/GitHub-PathAnalysis-blue)](https://github.com/tplobo/path-analysis)
[![Developer Portal discussion](https://img.shields.io/badge/ANSYS-Developer_Portal-orange)](https://discuss.ansys.com/discussion/2398/pathanalysis-package-for-ansys-mechanical#latest)

***
### Introduction
This package was developed as a simple (_i.e._ quick and dirty) tool to compute and export stress and temperature analyses along linear paths between a point and surface pair selected in ANSYS Mechanical. Check [this link](https://feaforall.com/introduction-stress-linearization/) or [this link](https://www.graspengineering.com/what-is-stress-linearization/) or [this link](https://featips.com/2022/10/27/stress-linearization-explained/) for more information on linearization along FEM/FEA paths. [This article](https://asmedigitalcollection.asme.org/pressurevesseltech/article/113/4/481/436544/The-ASME-Code-and-3D-Stress-Evaluation) also provides a good example.

This has the aim of producing analyses necessary for licensing pressure vessels under some regulations (_e.g._ [ASME's BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-bpvc-section-viii-rules-construction-pressure-vessels-division-1/2023/print-book), [afcen's RCC-MRx Code](https://www.afcen.com/en/rcc-mrx/198-rcc-mrx-rcc-mr.html)).

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
by enabling the check-box for **PathAnalysis**. A menu of the same name should appear in the toolbar of your results visualization window (_i.e._ not in the workbench):
![Toolbar menu of the PathAnalysis extension.](https://github.com/tplobo/path-analysis/blob/94394dd69eb74889acf7b6b4110a3967169aca94/example/screenshot_toolbar.png)

To use the extension:
1. first create **named selections** for both a node and a surface in your results visualization window;
2. then click the **Path** button (route icon) in the toolbar to create the shortest path between them;
3. then click the **Calculate** button (calculator icon) to compute the stress and temperature analysis summaries and export them as a CVS file on your Desktop.

The **Calculate** button can perform its action for multiple paths,  so steps 1 and 2 can be repeated as many times as necessary.
The **Delete** button (paper shreder icon) can be used to delete analysis solutions for all paths.

The example file in the repo can be used to test the extension after it has been installed and enabled.

It contains a named Node and a named Surface that can define a path, in a simple geometry loaded with a simple temperature distribution. Altering the given node/surface and clicking Path a few times can provide us with linear paths to perform an example analysis:
![Multiple paths created by changing the Node and Surface named selections.](https://github.com/tplobo/path-analysis/blob/94394dd69eb74889acf7b6b4110a3967169aca94/example/screenshot_paths.png)

Solutions are produced and renamed accordingly:
![One of the path analysis solutions: the Linearized Equivalent Stress along the first path.](https://github.com/tplobo/path-analysis/blob/94394dd69eb74889acf7b6b4110a3967169aca94/example/screenshot_solution.png)

And the summaries are exported as a CSV file onto the Desktop, that can be opened with Excel for example:
![Solution summaries exported and opened as a spreadsheet.](https://github.com/tplobo/path-analysis/blob/94394dd69eb74889acf7b6b4110a3967169aca94/example/screenshot_export.png)

***
### Development
The extension is a simple set of files: one .XML for configuring the toolbar and a few .PY to define the functions necessary to run its features.

If you intend to modify the package, it might be a good idea to enable the debugging mode in the ANSYS Mechanical GUI. To do so, in the Workbench toolbar:
`Tools > Options > Extensions`,
enable the check-box for **Debug Mode**.

For additional information on XML tags and custom extensions, one can always check the *Online API and XML Reference Guides* in [ANSYS ACT Developers Guides](https://catalog.ansys.com/Developers.cshtml).
