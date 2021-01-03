# buildingSci-SideKick
(WIP) A central side kick application, for ALL of the bldgphys/sci data for PH, and stuff. 

Currently a work in progress. 

the intent is to provide a way to integrate all of the data used for materials, 
systems, components and constructions, ect used for programs like:
energyPlus, PHPP, and other building phys/sci sim and analysis programs.

I don't know about anyone else but: some centralized I/O, storage, 
and frequently used calcs and other tools would make things a bit easier.

The main intent is to allow a centralized database:
tables for insulation, masonry, wood materials, membranes, air layers, ERV/HRV's 
heat pumps, glazing, frames, doors and literally whatever you want to make a table of.

Then, from thoes:
    create table of assemblies ect.
    table of projects to organize all the aforementioned being used for each specific project.


To-Do list:
    Get the intitial tk gui up and running.
    Add additional init tables for additional elements.
    Add additional init tables for constructions, systems, heatpumps, boilers ect. 
    Add additional init tables for projects.
    Revamp the gui because at this point it will likely be messy.
    Add feature: import and append *.csv data to tables
    Prolly add 'create your own table'

    I/O:
    EnergyPlus*
    Rhino** for use with LBT's, PHT's
    to be continued..

    * likely in the form of classes to format the output objs as needed
    ** plugin to interface with Grasshopper and handle the data being passed: with classes to format output objs

Way down the road to-do: 
    py package to: like @santoshphilip eppy:   handle and control PHPP from .py.