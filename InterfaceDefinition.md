# Overview

This filde descirbes the structure of data exchanged between the Classifier and the WebUI.

# Structure

## Dictionary Data

The dictionary contains all the words the Classifier has classified and their classification. The objects have an ID, the word and a vector of the classification values in the interval [0-1].

| Name | Value | Example |
|------|-------|---------|
|id|string|"abc123"|
|word|string|"cancer"|
|classification|[number]|[1.0,0.0,0.0,0.0,0.0,0.0]|

## Classified Articles

This array contains all data on all the articles used for training. Every item has the following properties:

| Name | Value | Example |
|------|-------|---------|
| id | string | "abc123" |
| title | string | "Hallmarks of Cancer" |
| URL | string | [link](https://www.cell.com/cell/fulltext/S0092-8674(00)81683-9)|
|classification|[number]|[1.0,0.0,0.0,0.0,0.0,0.0]|
