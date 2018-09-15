# Scripts

[Koruri](http://koruri.lindwurm.biz) をビルドするためのスクリプトです。

## 使い方

```
git clone https://github.com/Koruri/Scripts make_koruri
```

```
cd make_koruri
```

### `setup.sh` でできる

```
mkdir opensans mplus roboto koruri
```

```
wget -O opensans.zip https://fonts.google.com/download?family=Open+Sans && unzip opensans.zip -d opensans
```

### 手動

* [ここ](https://osdn.jp/projects/mplus-fonts/releases/62344) から最新の M+ OUTLINE FONTS TESTFLIGHT をダウンロード
* M+ 1p を `mplus` に展開
* Roboto の `U+EE01` だけを取り出した版を用意する(WIP)

```
fontforge -lang=py -script koruri.py
```
