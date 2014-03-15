#!/bin/bash

gcc -o sdl sdl.c -Wall `sdl-config --cflags --libs`
