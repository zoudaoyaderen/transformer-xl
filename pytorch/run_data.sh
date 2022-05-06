#!/bin/bash

echo 'cache_data...'
nohup python get_data.py \
    --cuda \
    --data ../data/chunyu/ \
    --dataset chunyu \
    --n_layer 12 \
    --d_model 512 \
    --n_head 8 \
    --d_head 64 \
    --d_inner 2048 \
    --dropout 0.1 \
    --dropatt 0.0 \
    --optim adam \
    --lr 0.00025 \
    --warmup_step 0 \
    --max_step 8000000 \
    --tgt_len 512 \
    --mem_len 512 \
    --eval_tgt_len 128 \
    --batch_size 24 \
    ${@:2} &
