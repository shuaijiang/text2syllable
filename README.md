# Convert Chinese text to syllable
Convert the Chinese character to syllable(pinyin) with tones.
Supported:
- text normalization
- convert full-width to half-width 
- convert English text to character with '_' before and after character 
- create vocabulary

# Demo
The Chinese characters:

`utt_1   步步高 ａ四 内置 什么 游戏 ？`

The Chinese syllable:

`utt_1  bu4 bu4 gao1 _a_ si4 nei4 zhi4 shen2 me you2 xi4`

Note: full-width 'ａ' convert to '\_a\_'

# Requirements
- pypinyin

# TODO
- support English subword(sentencepiece) 

# Author
- github: https://github.com/shuaijiang
- Email: zhaoshuaijiang8@gmail.com
