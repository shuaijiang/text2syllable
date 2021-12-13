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
from text_featurizer import TextFeaturizer
from pypinyin import pinyin, Style

default_config = {
    "type": "vocab",
    "model": "examples/asr/aishell/data/vocab",
}

def text2token(input_text, output_token):
    textfeaturizer = TextFeaturizer()
    with open(input_text, 'r', encoding='utf-8') as TEXT, \
         open(output_token, 'w', encoding='utf-8') as TOKEN:
        texts = TEXT.readlines()
        for text in texts:
            text_list = text.split()
            key = text_list[0]
            trans = ''.join(text_list[1:])
            trans = textfeaturizer.delete_punct(trans)
            trans = textfeaturizer.strQ2B(trans)
            pinyin_list = pinyin(trans, style=Style.TONE3, errors=lambda x: ['_' + ele + '_' for ele in x])
            pinyin_str = ' '.join([pinyin[0] for pinyin in pinyin_list])
            TOKEN.write('{}\t{}\n'.format(key, pinyin_str))

if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    if len(sys.argv) < 3:
        logging.info('Usage: python {} input_text output_pinyin\n'
              '    input_text   : the input text file \n'
              '    output_token : the output token file \n'.format(sys.argv[0]))
        exit(1)
    input_text = sys.argv[1]
    output_pinyin = sys.argv[2]

    text2token(input_text, output_pinyin)
