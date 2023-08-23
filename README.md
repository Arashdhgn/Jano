# Jano
A small data related Project to scrap and analyze rental place info

## 2023/06/18
Right now It's a web Scraper. but I'm working on the SQL Connection and an Incremental Load solution.

## 2023/08/24
The SQL functionality has been added.
now it can insert every single row of data it collects into SQL tables, right now, it is on the normalization branch.
the query to create the needed tables is added.
in the next commit, it would be able to avoid repeated Data.
created a class that contains pre-defined texts needed for scrapping as attributes, It's not complete yet but it works.
right now the master branch is still just a web scrapper and the normalization branch contains these 2 new features.
the branches will be merged after the completion and test of the new features.
