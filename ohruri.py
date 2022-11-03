#!/usr/bin/env fontforge -lang=py -script
# -*- coding: utf-8 -*-

import fontforge
from datetime import date

# Open Sans のあるディレクトリのパス
opensans_path = "./opensans"

# Roboto のあるディレクトリのパス
roboto_path = "./roboto"

# M+ のあるディレクトリのパス
mplus_path = "./mplus"

# Mgen+ のあるディレクトリのパス
mgen_path = "./mgen"

# Ohruri を生成するディレクトリのパス
# 同じディレクトリに一時ファイルも生成される
ohruri_path = "./ohruri"

# フォントリスト
# Open Sans ファイル名, Roboto ファイル名, M+ ファイル名, Mgen+ ファイル名, Ohruri ウェイト
font_list = [
    ("OpenSans-Light.ttf", "Roboto-Light.ttf", "mplus-1p-light.ttf", "mgenplus-1p-light.ttf", "Light"),
    ("OpenSans-Regular.ttf", "Roboto-Regular.ttf", "mplus-1p-regular.ttf", "mgenplus-1p-regular.ttf", "Regular"),
    ("OpenSans-SemiBold.ttf", "Roboto-Medium.ttf", "mplus-1p-medium.ttf", "mgenplus-1p-medium.ttf", "Semibold"),
    ("OpenSans-Bold.ttf", "Roboto-Bold.ttf", "mplus-1p-bold.ttf", "mgenplus-1p-bold.ttf", "Bold"),
    ("OpenSans-ExtraBold.ttf", "Roboto-Black.ttf", "mplus-1p-heavy.ttf", "mgenplus-1p-heavy.ttf", "Extrabold"),
]

def main():
    # 縦書き対応
    fontforge.setPrefs('CoverageFormatsAllowed', 1)

    # バージョンを今日の日付から生成する
    today = date.today()
    version = "Ohruri-{0}".format(today.strftime("%Y%m%d"))

    for (op, rb, mp, mg, weight) in font_list:
        op_path = "{0}/{1}".format(opensans_path, op)
        rb_path = "{0}/{1}".format(roboto_path, rb)
        mp_path = "{0}/{1}".format(mplus_path, mp)
        mg_path = "{0}/{1}".format(mgen_path, mg)
        oh_path = "{0}/Ohruri-{1}.ttf".format(ohruri_path, weight)
        generate_ohruri(op_path, rb_path, mp_path, mg_path, oh_path, weight, version)

def ohruri_sfnt_names(weight, version):
    return (
        ('English (US)', 'Copyright',
         '''\
         Ohruri: Copyright (c) 2015- lindwurm.

         Open Sans: Copyright 2020 The Open Sans Project Authors. https://github.com/googlefonts/opensans
         Roboto: Copyright (c) 2012- Google.
         Mgen+: (c) 2015 自家製フォント工房, (C) 2002- M+ FONTS PROJECT.'''),
        ('English (US)', 'Family', 'Ohruri {0}'.format(weight)),
        ('English (US)', 'SubFamily', weight),
        ('English (US)', 'Fullname', 'Ohruri-{0}'.format(weight)),
        ('English (US)', 'Version', version),
        ('English (US)', 'PostScriptName', 'Ohruri-{0}'.format(weight)),
        ('English (US)', 'Vendor URL', 'https://koruri.github.io'),
        ('English (US)', 'Preferred Family', 'Ohruri'),
        ('English (US)', 'Preferred Styles', weight),
        ('Japanese', 'Preferred Family', 'Ohruri'),
        ('Japanese', 'Preferred Styles', weight),
    )

def ohruri_gasp():
    return (
        (8, ('antialias',)),
        (13, ('antialias', 'symmetric-smoothing')),
        (65535, ('antialias', 'symmetric-smoothing')),
    )

def generate_ohruri(op_path, rb_path, mp_path, mg_path, oh_path, weight, version):
    # Mgen+ を開く
    font = fontforge.open(mg_path)

    # M+ を開く
    mpfont = fontforge.open(mp_path)

    # M+ に含まれるグリフを削除する
    font.selection.none()
    mpfont.selection.all()
    for glyph in mpfont.selection.byGlyphs:
        if glyph.glyphname in font:
            font.selection.select(("more",), glyph.glyphname)
    font.clear()

    # M+ をマージする
    font.mergeFonts(mp_path)

    # EMの大きさを2048に設定する
    font.em = 2048

    # Open Sans を開く
    opfont = fontforge.open(op_path)

    # Open Sans に含まれるグリフを削除する
    font.selection.none()
    opfont.selection.all()
    for glyph in opfont.selection.byGlyphs:
        if glyph.glyphname in font:
            font.selection.select(("more",), glyph.glyphname)
    font.clear()

    # Open Sans をマージする
    font.mergeFonts(op_path)

    # Fancy Colon を Roboto からコピーする
    rbfont = fontforge.open(rb_path)
    
    # Fancy Colon をコピー
    rbfont.selection.select(0xee01)
    rbfont.copy()
    font.selection.select(0xee01)
    font.paste()

    # Fancy Colon を U+A789 にコピー
    font.selection.select(0xee01)
    font.copy()
    font.selection.select(0xa789)
    font.paste()

    # フォント情報の設定
    font.sfnt_names = ohruri_sfnt_names(weight, version)
    font.os2_vendor = "maud"

    # Grid Fittingの設定
    font.gasp = ohruri_gasp()

    # TTF の生成
    font.generate(oh_path, '', ('short-post', 'opentype', 'PfEd-lookups'))

if __name__ == '__main__':
    main()
