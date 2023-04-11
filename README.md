(if you have no idea what all of this is about, don't bother, it wouldn't be
of any use to you.)

# Principle
Editing /creating scenarios through the interface is very bothersome. Doing so
through the data file less so, but not quite ideal yet. This script aims to
allow you to explode your data files into their component (code, view, style)
and merge them in a data file.

You can also inject the content of your components directly into the DB to
bypass the module update step. Beware, this allows you to send code the parser
could flag as invalid and that'd have been caught in the module update step.
As such, make sure to always try to update your module with the final code before
pushing it to prod.

## Requirements
Python3, unidecode, psycopg2

## New scenario
run `dataer template`, creates structure necessary for work.
When your skeleton.json is complete, and you have a symlink to the location
your data file should go to, run `make` to "compile" your scenario and send it to its
destination.

## Inject code
run `dataer inject`. Parses the skeleton.json file to find which db entry to update, with which file's content.  
The entry has to exist first (run `make` and add the data file to your module to create the entries. Not needed if
your view/OC already exists).

## Existing scenario
run `dataer unravel FILENAME`. Should split an existing scenario into its component, kinda wonky as of right now
