import os
from os import makedirs, listdir
from os.path import join, isdir
from tqdm import tqdm
import scaper
import argparse

def generate(annpath, sourcepath, savepath, class_split, add_test):
    # set paths
    annfolder = join(annpath, class_split)
    savefolder = join(savepath, 'SONYC_FSD_SED.audio', class_split)
    
    if add_test:
        # additional test data in the past and future year are sampled from the test source
        fg_path = join(sourcepath, 'fsd50k_foreground', 'test')
    else:
        fg_path = join(sourcepath, 'fsd50k_foreground', class_split)
    bg_path = join(sourcepath, 'sonyc_background')

    if not isdir(savefolder):
        makedirs(savefolder)

    # generate audio files given jams files
    for fname in tqdm(listdir(annfolder)):
        jamsfile = join(annfolder, fname)
        savefile = join(savefolder, fname.replace('.jams', '.wav'))

        scaper.generate_from_jams(jams_infile = jamsfile,
                                  audio_outfile=savefile,
                                  fg_path=fg_path,
                                  bg_path=bg_path,
                                  jams_outfile=None,
                                  save_isolated_events=False,
                                  isolated_events_path=None,
                                  disable_sox_warnings=True,
                                  txt_path=None,
                                  txt_sep='\t')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--annpath', type=str, required=True, help='path to SONYC_FSD_SED.annotations folder')
    parser.add_argument('--sourcepath', type=str, required=True, help='path to SONYC_FSD_SED.source folder')
    parser.add_argument('--savepath', type=str, required=True, help='path to save generated soundscapes)')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
 
    if "add_test" in args.annpath: # generating additional test data for sampling window experiment
        add_test = True
        splits = ['test_past_year', 'test_future_year']
    else:
        add_test = False
        splits = ['train', 'val', 'test']
    
    for class_split in splits:
        generate(args.annpath, args.sourcepath, args.savepath, class_split=class_split, add_test=add_test)
