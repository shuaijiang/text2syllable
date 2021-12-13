# coding=utf-8
# Copyright (C) zhaoshuaijiang8@gmail.com
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from absl import logging

def create_vocab(input_pinyin, output_vocab):
    with open(input_pinyin, 'r', encoding='utf-8') as PINYIN, \
         open(output_vocab, 'w', encoding='utf-8') as VOCAB:
        texts = PINYIN.readlines()
        vocab_dict = {}
        for text in texts:
            text_list = text.split()
            key = text_list[0]
            pinyin_list = text_list[1:]
            for pinyin in pinyin_list:
                if pinyin in vocab_dict:
                    vocab_dict[pinyin] += 1
                else:
                    vocab_dict[pinyin] = 1
        for entry in vocab_dict:
            VOCAB.write('{}\t{}\n'.format(entry, vocab_dict[entry]))

if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    if len(sys.argv) < 3:
        logging.info('Usage: python {} input_pinyin output_vocab\n'
              '    input_pinyin   : the input pinyin file \n'
              '    output_vocab : the output vocab file \n'.format(sys.argv[0]))
        exit(1)
    input_pinyin = sys.argv[1]
    output_vocab = sys.argv[2]

    create_vocab(input_pinyin, output_vocab)
