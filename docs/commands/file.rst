file
====

This section is auto-generated from the help text for the barique command
``file``.


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


      --email TEXT  User email adress for notificatio
      -h, --help    Show this message and exit.
    
