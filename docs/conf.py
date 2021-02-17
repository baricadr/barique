import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'baricadr'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'recommonmark']
master_doc = 'index'


def run_apidoc(_):
    from sphinx.ext.apidoc import main
    parentFolder = os.path.join(os.path.dirname(__file__), '..')
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(parentFolder)

    module = os.path.join(parentFolder, 'baricadr')
    output_path = os.path.join(cur_dir, 'api')
    main(['-e', '-f', '-o', output_path, module])


def setup(app):
    app.connect('builder-inited', run_apidoc)
