# Things to be done
  
* [x] [Get Istanbul Traffic Data](https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/00d72836-d035-462d-a66e-408883216195/download/traffic_density_202105.csv) from IBB Data Portal
* [x] Store locally in a parquet file
* [x] Store this in Google BQ

* [x]  [StormGlass API](https://docs.stormglass.io/) query istanbul weather data.
  * [x] Store response as it is (in Json Files)
  * [x] Convert response data in json lines format
  * [x] Store in weather data in Vertica (COPY LOCAL in json)

* [ ] Implement several queries & services over two datasets
  * [x] Available traffic data time range
  * [x] Total number of vehicles for a given hour range per geographical resolution (use jinja to generate SQL)
  * [x] Average number of vehicles for a given hour range per geographical resolution (use jinja to generate SQL)
  * [/] Correlation of traffic with temprature for a given hour range per geographical resolution (use jinja to generate SQL)

* [ ] Provide a CLI for power users to consume service over their Cli.

## Some helping notes

* Note that we have lots of components a better way to use a docker stack to handle all those requests
  * Finally use docker stack to combine all


## Useful notes

### Geohash Prefix Resolution

```
Geohash length Cell width Cell height
1 ≤ 5,000km × 5,000km
2 ≤ 1,250km × 625km
3 ≤ 156km × 156km
4 ≤ 39.1km × 19.5km
5 ≤ 4.89km × 4.89km
6 ≤ 1.22km × 0.61km
7 ≤ 153m × 153m
8 ≤ 38.2m × 19.1m
9 ≤ 4.77m × 4.77m
10 ≤ 1.19m × 0.596m
11 ≤ 149mm × 149mm
12 ≤ 37.2mm × 18.6mm
```