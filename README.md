# active-fsl
This repo contains the scripts to generate the SONYC-FSD-SED dataset presented in the paper "Active Few-Shot Learning for Sound Event Detection." (INTERSPEECH 2022)

## SONYC-FSD-SED
SONYC-FSD-SED is an open dataset of programmatically mixed audio clips that simulates audio data in an environmental sound monitoring system, where sound class occurrences and co-occurrences exhibit seasonal periodic patterns. We use recordings collected from the Sound of New York City ([SONYC](cacm.acm.org/magazines/2019/2/234354-sonyc/fulltext)) acoustic sensor network as backgrounds, and single-labeled clips in the [FSD50K](https://zenodo.org/record/4060432#.YWyLAEbMIWo) dataset as foreground events to generate 576,591 10-second strongly-labeled soundscapes with [Scaper](github.com/justinsalamon/scaper) (including 111,294 additional test data for the experiment of sampling window). Instead of sampling foreground sound events uniformly, we simulate the occurrence probability of each class at different times in a year, creating more realistic temporal characteristics.


Due to the large size of the dataset, instead of releasing the raw audio files, we release the source material and soundscape annotations in JAMS format, which can be used to reproduce SONYC-FSD-SED using Scaper.

To reproduce SONYC-FSD-SED:
1. Download all files from Zenodo.
2. Extract `.tar.gz` files. You will get
- `SONYC_FSD_SED.source`: 96 SONYC backgrounds and 10,158 foreground sounds in `.wav` format, 2GB.
- `SONYC_FSD_SED.annotations`: 465,467 annotation files, 57GB. 
- `SONYC_FSD_SED_add_test.annotations`: 111,294 annotation files for additional test data, 14GB. 
- `vocab.json`: 87 classes, each class is then labeled by its index in the list in following experiments. 0-42: train, 43-56: val, 57-86: test. 
- `occ_prob_per_cl.pkl`: Occurrence probability for each foreground sound class. 

3. Install [Scaper](https://github.com/justinsalamon/scaper)
4. Generate soundscapes from jams files by running the command. Set `annpaths` and `audiopath` to the extracted folders, and `savepath` to the desired path to save output audio files.
```
python generate_soundscapes.py \
--sourcepath PATH-TO-SONYC_FSD_SED.source \
--annpath PATH-TO-SONYC_FSD_SED.annotations \
--savepath PATH-TO-SAVE-OUTPUT
```
Note that this will generate 465,467 audio files with a size of ~765GB to the folder `SONYC_FSD_SED.audio` at the set `savepath`.

5. If you also want to generate additional test data (used in the paper for the experiment of sampling window), change the `annpath`
```
python generate_soundscapes.py \
--sourcepath PATH-TO-SONYC_FSD_SED.source \
--annpath PATH-TO-SONYC_FSD_SED_add_test.annotations \
--savepath PATH-TO-SAVE-OUTPUT
```
