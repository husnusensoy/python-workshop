create schema weather;

create table weather.istanbul(
    airTemperature float,
    visibility float,
    measure_time timestamp
);

truncate table weather.istanbul;

copy weather.istanbul(airTemperature
, visibility
, time filler timestamptz
, measure_time as time at time zone 'Europe/Istanbul')
 from local '/Users/husnusensoy/code/python-training-2910/week9/data/staging/weather/jsonl/*.jsonl' PARSER fjsonparser() REJECTMAX 1;

 