# Scripts

[Koruri](https://koruri.github.io/) をビルドするためのスクリプトです。

## 使い方

```
git clone https://github.com/Koruri/Scripts.git make_koruri
```

```
cd make_koruri
```

Open Sans と Roboto は `setup.sh` の中でダウンロード、展開されます。

```
./setup.sh
```

あとは

* [ここ](https://osdn.jp/projects/mplus-fonts/releases/62344) から最新の `M+ OUTLINE FONTS TESTFLIGHT` をダウンロード
* M+ 1p を `mplus` に展開
* [FontForge](https://fontforge.org/) をインストールしておく

```
fontforge -lang=py -script koruri.py
```
