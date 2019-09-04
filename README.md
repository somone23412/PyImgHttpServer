# PythonHttpServer API

~~`use crontab to ensure service always online`~~

+ To run this project:

```shell
source run.sh
```

## ImgAdd

+ url: `/imgadd`
+ method: `POST multipart`
+ parameter

| KEY |VALUE |
| --- | --- |
| blackListPersonId | 入库ID |
| blackListPersonName | 入库名 |
| blackListPersonImg |  入库图片，**jpg**格式|

+ black list : Id end as "_1"
white list : Id end as "_0" 
red list : Id end as "_2"
+ response：

```json
{"status": "0", "message": "add_accept"}
{"status": "1", "message": "add_reject_beacuse_of_id_exsists"}
{"status": "1", "message": "add_reject_beacuse_of_not_a_jpg_img'"}
```

## ImgDel
+ url: `/imgdel`
+ method: `DELETE`
+ parameter

| KEY |VALUE |
| --- | --- |
| deletePersonId | 出库ID |

+ response：

```json
{"status": "0", "message": "del_accept"}
{"status": "1", "message": "del_reject_beacuse_of_id_not_exsists"}
```
