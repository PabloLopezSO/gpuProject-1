#!/bin/bash


cd /home/ubuntu/gpuProject/src/main && python3 -m luigi --module main ExecuteStreamLit --local-scheduler
