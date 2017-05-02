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
	""" Reads the given female respondent file (default 2002)
    	and cleans it for use.
    
    	Returns a data file as a dictionary.
    	"""
	dct = thinkstats2.ReadStataDct(dct_file)
	df = dct.ReadFixedWidth(dat_file, compression='gzip')
	CleanFemResp(df)
	return df

def ValidatePregnum():
    """ Validates that the pregnancy number is the same
    between female respondent and pregnancy
    
    Returns either True or False
    """
    resp = ReadFemResp()
    print(resp.pregnum.value_counts().sort_index())
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg) # lets us search pregnancy file by case id

    for index, pregnum in resp.pregnum.iteritems():
        case_id = resp.caseid[index] # gets the case id for every respondent on the list
        case_id_indices = preg_map[case_id] # counts the number of pregnancies for a given case id number (one woman)

        if pregnum != len(case_id_indices): # checks the number of pregnancies compared to how many times they appeared in the pregnancy record. If 0, would not appear in pregnancy file
            return False # returns false if the numbers do not match

    return True # if does not return false before this time, is true	

if __name__ == '__main__':
    print("Female respondent number of pregnancy is equal to pregnancy responses:", ValidatePregnum())
