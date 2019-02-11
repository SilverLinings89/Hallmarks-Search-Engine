# Hallmarks-Search-Engine

## Introduction

As described on my website, this repository contains my work on a search engine for scientific publications. It is built to be usable with any scientific field that can be split into multiple research directions. An example would be cancer research, where the Papers "Hallmarks of Cancer" and "Hallmarks of Cancer: The next Generation" offer such a classification.

The workflow is as follows: 
- Retrieve a dataset from any source that consists of either title-and-content pairs or title-and-abstract pairs.
- Train the classifier on it (you can specify some parameters for this or use default). The classifier is contained in this repo.
- Use the WebUI to visualize and use your tool. The WebUI is also contained in this repo.

If you have any further suggestions, feel free to leave them here or contact me.

## Classifier

The classifier computes the number of co-mentions of each collected keywords as well as a weighted co-mention value that is based on the total occurences of both words. For example: The first value only computes how many times the two words occur together. The second value gets higher if they occur most of the times together, i.e. if word a occurs word b also occurs. So if a occurs 100 times in total and b 5 times and 4 of them are together, this value is high. If for the same words both occur 100 times but only 5 times together, that value is low.

## Datasets

For scientific papers, the access rules can sometimes be difficult to handle which is sad. However, there are some efforts to overcome this burden. One place where you can start you search for content to train the classifier is the [archive](https://arxiv.org/) or the [SciGraph](https://scigraph.springernature.com/) and its [downloads](https://scigraph.springernature.com/explorer/downloads/).

## Instructions

Here I will descibe how to use this repository once everything is ready to use. Please be patient :)

## Data Preparation

In general, you need a file that consists of lines each holding a unique id, a title and an abstract - tab separated.

Since I use scigraph data myself, I have generated a set of scripts to read the downloadable data they provide into the format I require. Further, more complex data preparation scripts for other sources are welcome.
