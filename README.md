# Data science project structure

Based on https://drivendata.github.io/cookiecutter-data-science/

```
.
├── Makefile
├── config.yml
├── config-private.yml
├── data
│   └── raw             <- raw data from Kaggle
│   ├── intermediate
│   ├── processed       <- processed data from Kaggle (so fit models from stuff here)
│   ├── temp
├── results
│   ├── outputs
│   ├── models
├── documents
│   ├── docs
│   ├── images
│   └── references
├── notebooks               <- notebooks for explorations / prototyping
└── src                     <- all source code, internal org as needed
```
