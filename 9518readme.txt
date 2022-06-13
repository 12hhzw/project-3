Reproduction Steps
1Visit genanki-js/demo page and select Run example from menu
2Select any example from Select test example menu
3Change deck name to Test::New for creating subdeck
var d = new Deck(1276438724672, "Test::New")
4Click Run, it generate Anki deck .apkg.
5Import in AnkiDroid The issue created in genanki-js/issues

Expected Result
It should import deck with deck name Test and subdeck New. The .apkg file imported successfully on Anki desktop.

Actual Result
The app crashed and deck is not imported successfully.

Debug info
Refer to the support page if you are unsure where to get the "debug info".

AnkiDroid = v2.16alpha14
这个bug的重现的主要工作不在Ankiroid app进行，在Ankiroid中只需要简单的导入事先已经在外部生成的卡包，
因此我没有编写脚本去实现它。也正因如此，这个bug才有可讲的地方.

原先的bug report需要使用的网页，在千辛万苦打开之后（网不太好，梯子也不太稳定）,发现提示网页已转移。
不过找到了genanki-js这一项目的网址——https://github.com/krmanik/genanki-js
（genanki-js可以根据输入的数据生成Anki deck，也就是Ankiroid需要的“卡包“）

在把项目下载之后按照reproduce step里面说的，将sample文件夹下js中的jindex.js文件的deck name(“1347617346765，“New deck")
改为("1347617346765,"Test::New")
之后运行index.html,输入数据生成apkg卡包
之后将卡包拖入共享文件夹下，在模拟器中导入。
最终结果并未导致闪退，但也没有成功导入卡包，(可见上传的视频）,在adb logcat中也发现了报错。
尝试多次，发现如果使用genanki输入数据时量足够，那么是可以导入成功而不会发生任何bug。而如果数据量较少，则会报错.
我认为如果能在Android studio上进行上述工作应该可以复现bug，我的操作应该没有问题.

