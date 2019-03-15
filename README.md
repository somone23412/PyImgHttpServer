# PythonHttpServer API

`use crontab to ensure service always online`

## ImgAdd

+ url: `/imgadd`
+ method: `POST multipart`
+ parameter

| KEY |VALUE |
| --- | --- |
| blackListPersonId | 入库ID |
| blackListPersonImg |  入库图片，**jpg**格式|

+ response：

```json
{"status":"0", "message":"add_accept"}
{"status":"1", "message":"add_reject_beacuse_of_id_exsists"}
```
If got other response may be the Img has not been send correctly. 

## ImgDel

+ url: `/imgdel`
+ method: `DELETE`
+ parameter

| KEY |VALUE |
| --- | --- |
| deletePersonId | 出库ID |

+ response：

```json
{"status":"0", "message":"del_accept"}
{"status":"1", "message":"del_reject_beacuse_of_id_not_exsists"}
```
