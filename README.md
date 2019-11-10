# Sunlight Foundation ETL Task for Datamade

This repo shows two ways of transforming data from the Sunlight Foundation’s list of legislators in the United States.
The first method uses Python, the second uses Make and Postgresql.

To clone this repo using HTTPS, type into the command line

```
git clone https://github.com/egfrank/sunlight.git
```

All the commands below will assume you are in the root directory of the repo, so from here enter
```
cd sunlight
```
if you have git cloned the repo successfully, you should see the source file `raw/legislators.csv`. Both methods use this file to create the new spreadsheets.

## Python Approach
My initial approach was to use Pandas in Python to filter this data. 

#### Requirements You need Python3 installed to run this script. The only Python package we need to install is Pandas, so run
```
pip install pandas
```
in the command line. 

#### Run the script
From the root directory of the repo run
```
python python/transform.py raw/legislators.csv
```

The script should output `python/democrats.csv` and `python/republicans.csv`.


## Makefile Approach and Postgresql

After coding the Python approach, I read [Datamade's Guide to ETL processes with Make](https://github.com/datamade/data-making-guidelines) and wanted to learn how to write a Makefile. I used Postgresql specifically because one query asked for "All Democrats who are younger than 45 years old" and Postgresql has a function to calculate age.

#### Requirements 
If you are running these commands on a Mac, you should have Make already installed. You will need to install Postgresql if it's not already installed. I am a big fan of going to https://postgresapp.com/ and using their app to install Postgres, but you can also use Brew:
```
brew install postgres
```

Then you need to launch your Postgres server. If you downloaded Postgres via `postgresapp.com`, then you can search for the Postgres GUI and launch it from there. If you downloaded Postgres via Brew, then using the command line run
```
brew services start postgresql
```

Then, edit the file `config.mk`, changing the first three lines so the Makefile can connect to your Postgres server. If you downloaded Postgres via  `postgresapp.com` you probably will only need to change the second line, the PG_USER, and it should be your system username.

Finally, to run this Makefile you'll also need to download the Python packages `csvkit` and `psycopg2` 
```
pip install csvkit
pip install psycopg2
```
#### Running the Makefile

To create the spreadsheets using the Makefile, run
```
make all
```
This will create `output/democrats.csv` and `output/republicans.csv`. These two files should be similar, with slight formatting differences, to the outputs of the Python script.

When you git cloned the repo, `output/democrats.csv` and `output/republicans.csv` probably already existed. To delete these files, run
```
make clean
```
Then if you run `make all` you can be sure you're creating new spreadsheets.



## Troubleshooting

If you see an error that looks like 
```
"psql: FATAL:  role "*PLEASE_FILL_IN*" does not exist"
```
go into `config.mk` and change the PG_USER variable to your chosen Postgresql username

If you see an error that looks like
```
psql: could not connect to server: No such file or directory
     Is the server running locally and accepting
     connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
```
your Postgresql server is probably not on. The instructions for turning on your Postgresql server were included in the Makefile section under *Requirements*.



## Context

This was my code sample for the [Datamade developer position that opened up Winter 2019](https://datamade.us/blog/join-the-datamade-team/). The [prompt](https://docs.google.com/document/d/11_WSplUs2rX2Tw8a-Oko0uHW3fGtWAD3c7gIhmQeB64/edit) was:
```
1. Spreadsheet manipulation
Download the Sunlight Foundation’s list of legislators in the United States. Write a script that reads the spreadsheet as input, filters the rows based on specific criteria, and writes two spreadsheets as output. The criteria for the two spreadsheets should be:

First spreadsheet: All Democrats who are younger than 45 years old
Second spreadsheet: All Republicans who have Twitter accounts and YouTube channels

For each row in the output, make sure to keep all of the columns from the original data source.
```