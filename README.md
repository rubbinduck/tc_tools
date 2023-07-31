# tc_tools
Support for automatic generation of trading cards

This repository will be filled slowly with python code aiming to provide easy generation of trading cards using the commonly known tools Inkscape and Excel. I aim to work 1 to 2 hours each monday in my free time on this project, but some mondays have to be skipped when I want to do other stuff. If you are interested in this project growing faster, consider to create a PR by yourself ;).
I already had a repository tc_tools, but deleted that since it was more of a collection of prototypes and I want to do it more "properly" this time. If you have ideas or you see bugs/problems with the project, feel free to create an issue on Github.

## The Vision
The big idea is, that the generation of custom cardgames will be made easier.
- If you are not affine to IT you should be able to describe your custom card game using an svg template (generated by hand with Inkscape) an Excel sheet and maybe a configuration textfile and then just run tc_tools from command line or using a leightweight GUI to generate your custom cardgame (or customizable example cardgames if necessary).
- If you want to add some logic which is not supported by the command line/GUI you should be able to import tc_tools into your own Python project and use some dedicated objects in order to implement your custom logic fast and easy

## Technical Details
I plan to use the following dependencies:
- `pandas` (for excel reading)
- `xml.etree.ElementTree` (for an easy in-program representation of svg's)
- `kiwi` (for GUI)

For different components of an SVG, there should be different custom SVG objects yielding the same structure.

I plan to structure the process in a kind-of layered fashion involving the following layers (moduls):
- `persistence`: read data from disk and save data to disk
  - create ElementTree from svg
  - create svg from ElementTree
  - render svg to png or pdf (using Inkscape as "man in the middle")
  - read an excel file and create a respective data source object
- `mapper`: extract and transform data types into others
  - extract custom SVG object structure from ElementTree
  - copy custom SVG object structure
  - merge custom SVG object and ElementTree to ElementTree
- `manipulator`: change custom SVG objects
  - move, rotate, align elements etc.

In a later stage of the project, I possibly will add another layer between mapper and manipulator for png manipulation.

Another module, the `processor` module should then control the data flow between the layers and itself be called by the `gui` and the `command_line`.

Here is a diagram, because diagrams are cool:

![module_diagram](https://github.com/RobertSchueler/tc_tools/assets/70914876/67716ef5-c975-4497-8be9-843749c0d05b)

## Git/Merging strategie

- the main branch is a version branch and therefore only updated when a new version is released
- hot fixes will be commited to the main branch directly
- the future branch contains the current WIP state of the next bigger version
- If you want to contribute you can create a PR to the future branch that realizes one of the points of the next section
- I want a linear git history, so everything should be rebased before a fast forward merge is performed
- The versioning will be according to standard practices
  - changes to README.md and other supplementary files do not result in a version change
  - hot fixes lead to a increase of the last version number, e.g. 0.0.0 -> 0.0.1
  - the merge of the future branch into main will result in an increase of the second version number, e.g. 0.0.99 -> 0.1.0
  - If all milestones are reached, the first version number is increased, e.g. 0.99.99 -> 1.0.0. Note that all deprecated features are removed in such a major change, so versions with a different first version number might not be compatible
- I want to refine the application feature by feature in a kind-of agile process (every in-between version should be running)

## Other design decision

- tests of behaviour for all methods (created while implementing)
- no tests of implementation
- no useless documentation
- make it typesafe

## Plan going forward (to version 0.1.0)

First we need to implement the basic structure and logic and get a first running application.
In particular we need to implement the following features:

- [x] create the base module structure
- [x] implement a method that reads an svg and creates an ElementTree object
- [x] implement a method that writes an svg from an ElementTree object
- [x] implement a method that calls Inkscape to create a png from ElementTree
- [x] implement a basic data source object
- [x] implement a method that creates data source object from excel sheet
- [x] implement root SVG object (allowing children to be mapped)
- [x] implement placeholder SVG object (for unknown svg elements)
- [x] implement a mapper from ElementTree to root SVG
- [x] implement a simple mapper mapping Element and placeholder SVG object to Element
- [x] implement a simple mapper mapping ElementTree object and root SVG object to ElementTree object
- [x] implement base processor method combining all the previous steps
- [x] create GUI window
- [x] add three file picker to GUI named
- [x] add labels for the three file picker (excel sheet, template, options)
- [x] add button labeled "render deck"
- [ ] add processor call to button
- [ ] implement command line integration

The resulting version will be relatively useless, since it only produces one rendering of a given template svg per line in the excel sheet. But everything will be in place, so it will hopefully be a good starting point for future features.

## Milestones for version 1.0.0

- Support for Text, Image, Rectangle, Groups
- Text content can be changed
- Image can be switched
- SVG root can be searched for elements by label, text content
- Elements can be repositioned, resized, rotated and reflected
- Font-family, font-size and font-weight can be changed
- Example Projects: Domino and Skat
