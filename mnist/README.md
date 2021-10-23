# Data File Description


### file source
<http://yann.lecun.com/exdb/mnist/>

These files are not in any standard image format. You have to write your own (very simple) program to read them.





### file format

#### train-labels
| offset | type | value | description |  
|:--- | :--- | :--- | :--- |  
| 0000     | 32 bit integer  | 0x00000801(2049) | magic number (MSB first) |
| 0004     | 32 bit integer  | 60000            | number of items |
| 0008     | unsigned byte   | ??               | first label(0~9) |
| 0009     | unsigned byte   | ??               | second label(0~9) |
| ........ | | | |
| xxxx     | unsigned byte   | ??               | label(0~9) |


#### train-image
| offset | type | value | description |  
|:--- | :--- | :--- | :--- |
| 0000     | 32 bit integer  | 0x00000803(2051) | magic number |
| 0004     | 32 bit integer  | 60000            | number of images |
| 0008     | 32 bit integer  | 28               | number of rows (pixel) |
| 0012     | 32 bit integer  | 28               | number of columns (pixel) |
| 0016     | unsigned byte   | ??               | pixel 1 |
| 0017     | unsigned byte   | ??               | pixel 2 |
| ....... | | | |
| xxxx     | unsigned byte   | ??               | pixel |


#### test-labels
| offset | type | value | description |  
|:--- | :--- | :--- | :--- |  
| 0000     | 32 bit integer  | 0x00000801(2049) | magic number (MSB first) |
| 0004     | 32 bit integer  | 60000            | number of items |
| 0008     | unsigned byte   | ??               | first label(0~9) |
| 0009     | unsigned byte   | ??               | second label(0~9) |
| ........ | | | |
| xxxx     | unsigned byte   | ??               | label(0~9) |


#### test-image
| offset | type | value | description |  
|:--- | :--- | :--- | :--- |
| 0000     | 32 bit integer  | 0x00000803(2051) | magic number |
| 0004     | 32 bit integer  | 60000            | number of images |
| 0008     | 32 bit integer  | 28               | number of rows (pixel) |
| 0012     | 32 bit integer  | 28               | number of columns (pixel) |
| 0016     | unsigned byte   | ??               | pixel 1 |
| 0017     | unsigned byte   | ??               | pixel 2 |
| ....... | | | |
| xxxx     | unsigned byte   | ??               | pixel |




