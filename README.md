# 冷蔵庫ごはん

冷蔵庫の中身と保管期限の目安から、今日作るべき献立とレシピを提案するスマホ向けWebアプリ。

https://jtnwtamwjd-pixel.github.io/fridge-app/

- `index.html` … アプリ本体（単一ファイル、データは端末の localStorage に保存）
- `tools/src.html` + `tools/data.js` + `tools/quick.js` + `tools/nutrition.js` … 編集用ソース。`src.html` の `__DATA__` を `data.js`＋`quick.js`（時短レシピ）＋`nutrition.js`（栄養データ）の中身で置き換えると `index.html` になる
