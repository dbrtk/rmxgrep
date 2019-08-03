#!/bin/sh -

CORPUS_PATH=$1
PIPED_LEMMA=$2

grep -Ri -P -o "[^.?!]*\b($PIPED_LEMMA)\b[^.?!]*[.?!]?" $CORPUS_PATH
