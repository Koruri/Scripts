# Scripts

[Koruri](http://koruri.lindwurm.biz) をビルドするためのスクリプトです。

## 使い方

```
git clone https://github.com/Koruri/Scripts make_koruri
```

```
cd make_koruri
```

```
./setup.sh
```

[ここ](https://osdn.jp/projects/mplus-fonts/releases/62344) から最新の M+ OUTLINE FONTS TESTFLIGHT をダウンロードして M+ 1p を `make_koruri/mplus` に展開

```
fontforge -lang=py -script koruri.py
```
