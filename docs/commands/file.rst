file
====

This section is auto-generated from the help text for the barique command
``file``.


``freeze`` command
------------------

**Usage**::

    barique file freeze [OPTIONS] PATH

**Help**

Launch a freeze task


**Output**


    Id associated to the freeze task
    
**Options**::


      --force       Force freezing, even if the freezing delay was not reached
      --dry_run     Do not make any deletion, just list changes that would be made
      --email TEXT  User email adress for notification
      -h, --help    Show this message and exit.
    

``list`` command
----------------

**Usage**::

    barique file list [OPTIONS] PATH

**Help**

List files available from a remote repository for a local path


**Output**


    List of file relative paths
    
**Options**::


      --missing            Only list files missing from the local path
      --max_depth INTEGER  Restrict to a max depth. Set to 0 for all files.
                           [default: 1]
    
      --from_root          Return full paths from root of the repo (instead of
                           relative to given path)
    
      -h, --help           Show this message and exit.
    

``pull`` command
----------------

**Usage**::

    barique file pull [OPTIONS] PATH

**Help**

Launch a pull task


**Output**


    Id associated to the pull task
    
**Options**::


      --email TEXT  User email adress for notification
      -h, --help    Show this message and exit.
    
