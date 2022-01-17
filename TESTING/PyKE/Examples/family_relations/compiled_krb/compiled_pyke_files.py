# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc2_example.krb'):
           [1642252465.8182905, 'bc2_example_bc.py'],
         ('', '', 'bc_example.krb'):
           [1642252465.8663018, 'bc_example_bc.py'],
         ('', '', 'example.krb'):
           [1642252465.9223135, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'family.kfb'):
           [1642252465.938317, 'family.fbc'],
         ('', '', 'fc_example.krb'):
           [1642252465.9783258, 'fc_example_fc.py'],
        },
        compiler_version)

