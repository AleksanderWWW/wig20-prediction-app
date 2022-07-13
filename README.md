# wig20-prediction-app
Machine learning app performing on-demand modeling of wig20 performance

## Introduction

The aim of this project is to build a simple, yet efficient web application allowing the users
to interactively experiment and build on-demand models of wig20 performance.
It is therefore important to provide the users with extensive and fine-grained control
over the input provided to the modeling engine, while preserving interface elegance 
and usability even for less-demanding individuals, interested only in simple models 
with sensible defaults.

---

## Data

The time series data used for performance modeling come from Warsaw Stock Exchange and
are extarcted by the means of API request simulation.
By viewing the network traffic upon creating price chart it has been observed that
a request to *https://gpwbenchmark.pl/chart-json.php* returns a JSON response with
all the neccesarry data points in an easy-to-process format.

By modyfing the full URL string it is possible to obtain time series data for a user-defined
time period for all relevant price components of the index i.e. *close*, *open*, *min* and *max* price
data points, together with the corresponding timestamps.
For example, to obtain the data between 1st June - 1st July 2022 a request can be sent with the url:

*https://gpwbenchmark.pl/chart-json.php?req=[{%22isin%22:%22PL9999999987%22,%22mode%22:%22RANGE%22,%22from%22:%222022-06-01%22,%22to%22:%222022-07-01%22}]*

Despite this being a rather lengthy string, the insertion of relevant parameters is pretty straight-forward (see *app.scraper.gpw* module).

---
Author: Aleksander Wojnarowicz