# tools/src.html の __DATA__ にデータファイルを埋め込んで index.html を作る
parts=['data.js','quick.js','nutrition.js','more.js']
s=open('tools/src.html').read()
open('index.html','w').write(s.replace('__DATA__','\n'.join(open('tools/'+f).read() for f in parts)))
