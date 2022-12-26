create schema if not exists weather;

/*
 {"time": "2020-01-31T21:00:00+00:00", "humidity": 68.49333333333334, "airTemperature": 8.08, "visibility": 24.14}
 */

create table if not exists weather.istanbul(
    measure_time TIMESTAMP not null,
    humidity float not null,
    airTemperature float not null,
    visibility float not null
);

COPY weather.istanbul (
    humidity,
    airTemperature,
    visibility,
    time filler timestamptz,
    measure_time as time at time zone 'Europe/Istanbul'
)
FROM LOCAL 'data/weather/jsonl/feb.jsonl' PARSER FJSONPARSER()  REJECTMAX 1;


