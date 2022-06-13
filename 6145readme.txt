Reproduction Steps
1Open AnkiDroid with two decks and several sub deck. Enable Scheduler V2
2Try to export a single deck with time data
3Try to export whole collection without time data
4Try to export whole collection while including time data
Expected Result
Trying to export a single deck shows a warning, that exporting single decks with time data is only supported with SchedV1.
When exporting the complete collection with time data, no such warning is shown, so I expect it to be able to export the collection

Actual Result
Using SchedV2 the collection can be exported without the time data.

When the time data is selected for export, AnkiDroid crashes without further notice when trying to export the collection.

AnkiDroid Version = 2.10beta3
完成了重现bug视频的录制，但是由于文件大小限制无法上传.