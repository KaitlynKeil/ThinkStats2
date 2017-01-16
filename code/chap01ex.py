"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)

def CleanFemResp(df):
    """Recodes variables from the pregnancy frame.

    df: DataFrame
    """
    # replace 'not ascertained', 'refused', 'don't know' with NaN
    na_vals = [97, 98, 99]
# replace 'not ascertained', 'refused', 'don't know' with NaN
    na_vals = [97, 98, 99]
    df.pregnum.replace(na_vals, np.nan, inplace=True)
    
def ReadFemResp(dct_file='2002FemResp.dct',dat_file='2002FemResp.dat.gz'):
	dct = thinkstats2.ReadStataDct(dct_file)
	df = dct.ReadFixedWidth(dat_file, compression='gzip')
	CleanFemResp(df)
	return df

def ValidatePregnum():
	resp = ReadFemResp()
	print(resp.pregnum.value_counts().sort_index())
	preg = nsfg.ReadFemPreg()
	preg_map = nsfg.MakePregMap(preg)
	
	for index, pregnum in resp.pregnum.iteritems():
		caseid = resp.caseid[index]
		caseid_indices = preg_map[caseid]

		if pregnum != len(caseid_indices):
			return False
	
	return True	

if __name__ == '__main__':
    print(ValidatePregnum())
