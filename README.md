# Provenance case study
This repo contains notebook files and a poster presentation from the American Geophysical Union 2019 Fall meeting in San Francisco relating to an industry geological case study. The details of the dataset and major findings are confidential but aspects of the major project are presented here.

## The problem:
The offshore Gulf of Mexico (GoM) contains highly-important hydrocarbon resources from rocks 60-53 million years old (Middle Paleocene to Early Eocene). The commercial viability of the recoverable oil is a function of the sediment quality. In the geological past several rivers and deltas fed into the GoM from west Texas through to Mississippi and the sediment dumped offshore from these delta complexes forms the present-day reservoirs for oil and gas. The rock record offshore is drilled during oil exploration and the rock fragments from depth contain microfossils of pollen and spores that represent vegetation from onshore during the geological past. An explanation of this process is provided in my capstone presentation here https://github.com/b3py0/Capstone-projects/blob/master/Thinkful_volve_presentation.pdf.

## The question:
Which delta is associated with the best reservoir quality offshore? 

## Approach:
Analysing rocks containing fossils onshore from the Gulf Coastal Plain, the fossil record of each region and major delta complex is established so that they can 'fingerprint' different parts of the Gulf Coast. These data are compared to offshore sediments of the same age using data exploration and machine learning. The dataset represents counted fossil occurrences of different species (taxonomic groups) from onshore wells and outrop sites. **Machine learning has not been implemented on such datatypes before.** This repo contains:

* A .PDF of the poster presented at AGU
* A notebook of the PCA, RFC and VIF scores used to inform on the most important taxonomic groups
* A notebook on the ML algorithms attempted on the dataset with predictions to the offshore (i.e. confidential deep-water samples from oil exploration wells) of the same age.
* A python implementation of the Hellinger transformation

## Summary point:
In order to gain _quality_ data, samples have been culled and this results in a small dataset (c. 400 samples repreenting each class max) that even with synthethic oversampling results in __overfit__ models but PCA indicates that offshore samples probably represent cases that are not seen onshore in the training data leading to poor prediction from onshore --> offshore.  
