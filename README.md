# snaketmpl
>>> Snakemake simplist workflow for wordcloud creation.

## What?
>>> This workflow contain 3 rules :
* First : Scrap url and direct the text to file.
* Second: Generate standard png wordcloud.
* Third: Generate based shape wordcloud.


## How?
#### Requirements
>>> Make sure that you have snakemake and conda installed.

#### Configuration
>>> You can scrap your personal url by editing configs/configurer.yaml file.

#### Usage
##### Get the repository
```bash
git clone
cd 
```
##### Run Snakemake
```bash
snakemake --use-conda -R --until get_shape get_plot --core 2
```

## License 
>>> MIT