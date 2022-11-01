# ASN.1 工具使用手册

## Environment
   1. Python 3.9
   2. asntools - Python
      and install with cmd `pip install asn1tools`

## 更新记录

| 版本  | 时间       | P     | 说明                                                         |
| ----- | ---------- | ----- | ------------------------------------------------------------ |
| v1.01 | 10/12/2022 | Hasan | 1. 可以加密和解密                                            |
| v1.02 | 10/23/2022 | Hasan | 1. 修复由于结构体编译失败，加密和解密失败闪退<br />2. 可以拉伸窗口至全屏<br />3. 增加解密后结果前缩进，提高可读性 |
| v1.03 | 10/29/2022 | Hasan | 1. 添加打开ASN库文件按钮 单击选中后可直接编译；双击可以查看文件内容<br />2. 添加错误提示窗口，错误信息打印至Result窗口<br />3. 添加图标和作者信息 |



## 1. 界面

![image](https://user-images.githubusercontent.com/69131973/199275028-b5d8781e-068d-45e8-84c3-a163edfd8775.png)

   1. 点击`Reset`按钮可以重置四个文本框
   2. 点击`Compile`按钮可以编译ASN.1结构体，编译过程信息、错误信息在`Results`框中展示
   3. 选择`Encode`进行加密，选择`Decode`进行解密![image](https://user-images.githubusercontent.com/69131973/199275093-966a8d50-5cb1-4661-b975-76619e74ece4.png)
   4. 点击`Encode/Decode`按钮可以对加密/解密框中的内容进行加密/解密，结果在`Output`框中展示
   5. 选择编译格式，默认为 `uper`
   6. 点击`Encode/Decode`按钮可以进行加密或解密
   7. 结果在`Console Output`框中展示
   8. 点击 `Open ASN1 Library`按钮可以打开ASN库文件，位置是当前exe所在目录下的`asn_dir`文件夹。将您所需的ASN库复制到该文件夹下，重新打开工具后即可查看到库文件![image](https://user-images.githubusercontent.com/69131973/199275128-9f1363b9-f717-4a3b-b071-a8c5e32687c6.png)
   9. 单击选中某个库文件后，再点击`Compile`按钮即可编译该库文件
   10. 双击选中某个库文件即可查看该库文件内容，点击`Compile`即可编译该库文件
   11. 点击`Close ASN1 Library`即可返回文本输入界面



## 2. 流程
   （加密流程为1 -> 2 -> 3 -> 4 -> 5）（解密流程为1 -> 2 -> 3 -> 6 -> 7）

   1. 在图中所示的文本框中输入ASN1结构体，红框中内容自行替换

      ![image](https://user-images.githubusercontent.com/69131973/199275166-78b12444-6a28-400b-879c-adf7733aa9aa.png)

   2. 选择默认的编码格式`"UPER"`
      
      ![image](https://user-images.githubusercontent.com/69131973/199275202-8ae3cd53-ecb7-413b-bd3e-ddebc9ec7387.png)
      
   3. 点击Compile，Results框会显示编译成功
   
      ![image](https://user-images.githubusercontent.com/69131973/199275234-63ec380f-9c52-432f-8ff5-107c2e2370b3.png)
   
   4. 在文本框中输入需要加密的内容
   
      ![image](https://user-images.githubusercontent.com/69131973/199275268-089b6b96-e790-4f6a-9795-e22a36b34fd4.png)
   
   5. 点击Encode，Output文本框中会显示加密后的内容
   
      ![image](https://user-images.githubusercontent.com/69131973/199275292-a76f017e-55ef-49dc-926f-74bb97d808ee.png)
      
   6. 将加密的内容（Hex）复制到Decode文本框
   
      ![image](https://user-images.githubusercontent.com/69131973/199275328-a68a8397-8654-4dcc-a86b-0e979299304d.png)
   
   7. 点击Decode，Output文本框会显示解密后的内容
   
      ![image](https://user-images.githubusercontent.com/69131973/199275339-f8571715-7a2f-408c-aa84-134f0f37f49e.png)

## 3. 测试

   1. ASN1结构体

   ```
   Foo DEFINITIONS ::= BEGIN
   
       Question ::= SEQUENCE {
           id        INTEGER,
           question  IA5String
       }
   
       Answer ::= SEQUENCE {
           id        INTEGER,
           answer    BOOLEAN
       }
   
   END
   ```

   2. 加密内容

   ```
   {'id': 1, 'question': 'Is 1+1=3?'}
   ```

   3. 解密内容

   ```
   01010993cd03156c5eb37e
   ```

