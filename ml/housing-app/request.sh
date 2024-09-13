#!/bin/bash

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"longitude":"-121.89","latitude":"37.29","housing_median_age":"38","total_rooms":"1568","total_bedrooms":"351","population":"710","households":"339","median_income":"2.7042","ocean_proximity":"<1H OCEAN"}' \
    https://elcursodeia-housing.vercel.app/predict