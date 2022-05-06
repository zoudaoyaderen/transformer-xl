#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: cuiyi@zuoshouyisheng.com
# Created Time: 04 December 2020 15:55
import os
import json
import torch
from torch.utils.data import Dataset


class DiskBasedDataset(Dataset):
    def __init__(self, cache_dir, num_examples=0):
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        self.cache_dir = cache_dir
        self.num_examples = num_examples

    def __len__(self):
        return self.num_examples

    def __getitem__(self, index):
        return open(os.path.join(self.cache_dir, "{}.txt".format(index))).readline().strip()

    def add(self, text):
        index = self.num_examples
        pt_save_path = os.path.join(self.cache_dir,
                                    "{}.txt".format(index))
        f = open(pt_save_path, 'w')
        f.write(text)
        f.close()
        self.num_examples += 1

    @classmethod
    def load(cls, cache_dir):
        meta_path = os.path.join(cache_dir, "META.json")
        with open(meta_path, "r") as f_meta:
            cache_meta = json.load(f_meta)
            num_examples = cache_meta["num_examples"]
            dataset = cls(cache_dir, num_examples)
            return dataset
        return None

    def save(self):
        meta_path = os.path.join(self.cache_dir, "META.json")
        with open(meta_path, "w") as f_meta:
            json.dump({"num_examples": self.num_examples}, f_meta)
