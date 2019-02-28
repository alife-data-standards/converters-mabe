
# mabeData2stdPhylogeny.py 

Converts mabe data files to standard phylogeny format.
mabeData2stdPhylogeny.py creates lineage.json and lineage.csv

User must provide: 
<ul>
  <li>mabe file format for files to convert: either snapshot or SSwD (snapshot with delay)</li>
  <li>updateRange of files to convert, in format FIRST LAST STEP. i.e. from update 0 to 100 every 10</li>
  <li>other parameters are optional... see usage.</li>
</ul>
    
## Usage

```
usage: mabeData2stdPhylogeny.py [-h] [-path PATH] [-fileType TYPE]
                                [-oldColumnNames COLUMN_NAME [COLUMN_NAME ...]]
                                [-newColumnNames COLUMN_NAME [COLUMN_NAME ...]]
                                -updateRange FIRST LAST STEP [-verbose]

Converts .csv files generated by MABE to ALDS...

optional arguments:
  -h, --help            show this help message and exit
  -path PATH            path to files - default : none (will read files in
                        current directory)
  -fileType TYPE        type of file, either snapshot or SSwD, default :
                        snapshot
  -oldColumnNames COLUMN_NAME [COLUMN_NAME ...]
                        column names of data to read from source files -
                        default : "score_AVE" ("ID", "timeOfBirth", and the
                        correct ancestors list are added to the list
                        automatically)
  -newColumnNames COLUMN_NAME [COLUMN_NAME ...]
                        column names of data to be copied into new data file -
                        default : NONE, if blank, copy oldColumnNames ("id",
                        "origin_time", and "parents" are added to the list
                        automatically)
  -updateRange FIRST LAST STEP
                        update range of files to convert (from first to last
                        on step)
  -verbose              adding -verbose will provide more text output while
                        running (useful if you are working with a lot of data
                        to make sure that you are not hanging) - default (if
                        not set) : OFF
```
## Author(s)/Maintainer(s)

- Cliff Bohm
