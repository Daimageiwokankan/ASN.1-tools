# ASN.1 工具使用手册

## 1. 界面

![image](https://user-images.githubusercontent.com/69131973/199273338-be96a520-2a45-4bfb-8ebf-2c0972d5e2da.png)

   1. 点击Reset按钮可以重置四个文本框
   2. 点击Compile按钮可以编译ASN1结构体，结果在Results框中展示
   3. 点击Encode/Decode按钮可以对加密/解密框中的内容进行加密/解密，结果在Output框中展示
   4. ![image](https://user-images.githubusercontent.com/69131973/199273491-43974561-56b4-4c68-b30d-c0a4a0a2399a.png)选择Encode进行加密，选择Decode进行解密
   5. ![image](https://user-images.githubusercontent.com/69131973/199273513-4e047201-4fd1-4b4b-be34-0f634a6e1c7c.png)选择Compile，Encode 和 Decode 格式，默认为UPER



## 2. 解密流程
   （加密流程为1 -> 2 -> 3 -> 4 -> 5）（解密流程为1 -> 2 -> 3 -> 6 -> 7）

   1. 在图中所示的文本框中输入ASN1结构体，红框中内容自行替换

      ![image](https://user-images.githubusercontent.com/69131973/199273553-6bef2f3f-142b-46f5-a1f4-095c4d7340a5.png)

   2. 选择默认的编码格式"UPER"
      
      ![image](https://user-images.githubusercontent.com/69131973/199273604-0026eba3-7e35-41a0-9d5f-316bb1ca706a.png)
      
   3. 点击Compile，Results框会显示编译成功
   
      ![image](https://user-images.githubusercontent.com/69131973/199273646-55fd4387-8c15-4df4-9235-3b5753b93bdc.png)
   
   4. 在文本框中输入需要加密的内容
   
      ![image](https://user-images.githubusercontent.com/69131973/199273664-acff16f6-e73c-4a5a-9f7d-f7ae6e9a214d.png)
   
   5. 点击Encode，Output文本框中会显示加密后的内容
   
      ![image](https://user-images.githubusercontent.com/69131973/199273681-b603c646-c82b-4a47-96af-9e16245e8d97.png)
      
   6. 将加密的内容（Hex）复制到Decode文本框
   
      ![image](https://user-images.githubusercontent.com/69131973/199273714-c7b16e6c-9956-4089-96ba-96450dcd179c.png)
   
   7. 点击Decode，Output文本框会显示解密后的内容
   
      ![image](https://user-images.githubusercontent.com/69131973/199273751-07e15b68-e4f7-47b8-917a-85a528126794.png)

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

