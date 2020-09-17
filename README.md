# Provenance case study

This repo contains files and a poster presentations from AGU 2019 in San Francisco relating to a geological case study to investigate possible different delta sources for the Gulf of Mexico during the Paleocene (65-55 Ma) using the fossil record of pollen, spores and dinoflagellate cysts. These are abundant in rock chippings from oil exloration wells and one of the cheif ways of dating rocks in deep-water exploration wells.

The dataset represents counted fossil occurrences of different species (taxonomic groups) from onshore wells and outrop sites from Alabama through to west Texas. Machine learning has not been implemented on such datatypes before. This repo contains:

* A .PDF of the poster presented at AGU
* A notebook of the PCA, RFC and VIF scores used to inform on the most important taxonomic groups
* A notebook on the ML algorithms attempted on the dataset with predictions to the offshore (i.e. confidential deep-water samples from oil exploration wells) of the same age.
* A python implementation of the Hellinger transformation

## Summary point:
In order to gain _quality_ data, samples have been culled and this results in a small dataset (c. 400 samples repreenting each class max) that even with synthethic oversampling results in __overfit__ models but PCA indicates that offshore samples probably represent cases that are not seen onshore in the training data leading to poor prediction from onshore --> offshore.  
