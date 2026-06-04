# Chelator fragment identification

The Chelator Rules, defined by Agrawal et al. (2010) and implemented as part of the ChemFH package, check a molecule against 55 SMARTS patterns representing chelating functional groups that target metalloproteinases. Chelating groups covered include picolinic acids, hydroxyquinolines, hydroxypyrimidines, hydroxypyranones, 3,4-HOPO and 3,4-HOPTO derivatives, salicylic acids, catechols, sulfonamides, beta-diketones, and others. The model returns a binary flag for each of the 55 substructures and the total number of matched substructures.

This model was incorporated on 2026-06-02.


## Information
### Identifiers
- **Ersilia Identifier:** `eos2egp`
- **Slug:** `chelating-groups`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Frequent hitter`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `56`
- **Output Consistency:** `Fixed`
- **Interpretation:** Binary indicators (1 = substructure present, 0 = absent) and total number of hits (n_hits).

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| picolinic_acid | integer | high | Presence of picolinic acid (pyridine-2-carboxylic acid) chelating substructure |
| picolinic_acid_n_oxide | integer | high | Presence of picolinic acid N-oxide chelating substructure |
| 8_hydroxyquinoline | integer | high | Presence of 8-hydroxyquinoline chelating substructure |
| 8_hydroxy_5_azaquinoline | integer | high | Presence of 8-hydroxy-5-azaquinoline chelating substructure |
| hydroxyquinoline | integer | high | Presence of hydroxyquinoline (non-8-position) chelating substructure |
| 2_mercaptoquinoline | integer | high | Presence of 2-mercaptoquinoline (thiol quinoline) chelating substructure |
| quinoline_2_carboxylic_acid | integer | high | Presence of quinoline-2-carboxylic acid chelating substructure |
| diaminohydroxypyrimidine | integer | high | Presence of 2-4-diaminopyrimidine-6-ol chelating substructure |
| mercapto_hydroxypyrimidine | integer | high | Presence of 2-mercapto-4-hydroxypyrimidine chelating substructure |
| hydroxy_mercaptopyrimidine | integer | high | Presence of 2-hydroxy-4-mercaptopyrimidine chelating substructure |

_10 of 56 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2egp.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2egp.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `514`


### References
- **Source Code**: [https://github.com/antwiser/ChemFH](https://github.com/antwiser/ChemFH)
- **Publication**: [https://doi.org/10.1002/cmdc.200900516](https://doi.org/10.1002/cmdc.200900516)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2010`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2egp
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2egp
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
