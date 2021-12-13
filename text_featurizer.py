# coding=utf-8
# Copyright (C) 2019 ATHENA AUTHORS; Xiangang Li; Shuaijiang Zhao
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
# pylint: disable=invalid-name
""" Text featurizer """

import os
import re
import csv
import json
import warnings


class TextFeaturizer:
    """The main text featurizer interface
    """
    def __init__(self, config=None):
        self.punct_tokens = r"＇｛｝［］＼｜｀～＠＃＄％＾＆＊（）"
        self.punct_tokens += r"＿＋，。、‘’“”《》？：；【】——~！@"
        self.punct_tokens += r"￥%……&（）,.?<>:;\[\]|`\!@#$%^&()+?\"/_-"

    def delete_punct(self, tokens):
        """delete punctuation tokens
        """
        return re.sub("[{}]".format(self.punct_tokens), "", tokens)

    def strQ2B(self, ustring):
        """全角转半角"""
        rstring = ""
        for uchar in ustring:
            inside_code=ord(uchar)
            if inside_code == 12288:                              #全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374): # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            rstring += chr(inside_code)
        return rstring

    def strB2Q(self, ustring):
        """半角转全角"""
        rstring = ""
        for uchar in ustring:
            inside_code=ord(uchar)
            if inside_code == 32:                                 #半角空格直接转化
                inside_code = 12288
            elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
                inside_code += 65248

            rstring += chr(inside_code)
        return rstring
