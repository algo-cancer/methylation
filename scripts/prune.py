'''
    prune.py <t{i}.nwk> <heuristically_called_statuses.npz> <t{i}_site_mask.npz>
'''

import numpy as np, sys
from datetime import datetime
import skbio


if __name__ == "__main__":

    # work-around for snakemake env bug
    f_in, f_out, root, f_log = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    f = open(f_log, 'w')
    sys.stderr = sys.stdout = f

    obj = np.load(f_in, allow_pickle=True)
    pwd, cells = obj['pwd'], obj['rows']
    assert (kappa > 0) and (kappa < 1), 'Kappa must be a fraction.'

    f = open(f_log, 'w')
    sys.stderr = sys.stdout = f

    f.write('[{}] gmelin-larch is building neighbor-joining tree\n'.format(datetime.now()))

    dm = skbio.DistanceMatrix(pwd, cells)
    tree = build_and_reroot(dm, root)

    with open(f_out, 'w') as fi:
        fi.write(str(tree))

    f.write('[{}] DONE\n'.format(datetime.now()))
    f.close()
