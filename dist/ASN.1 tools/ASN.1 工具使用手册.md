# ASN.1 工具使用手册

## 1. 界面

   ![image-20221013131355488](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013131355488.png)

   1. 点击Reset按钮可以重置四个文本框
   2. 点击Compile按钮可以编译ASN1结构体，结果在Results框中展示
   3. 点击Encode/Decode按钮可以对加密/解密框中的内容进行加密/解密，结果在Output框中展示
   4. ![image-20221013131849401](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013131849401.png)选择Encode进行加密，选择Decode进行解密
   5. ![image-20221013131941844](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013131941844.png)选择Compile，Encode 和 Decode 格式，默认为UPER



## 2. 解密流程
   （加密流程为1 -> 2 -> 3 -> 4 -> 5）（解密流程为1 -> 2 -> 3 -> 6 -> 7）

   1. 在图中所示的文本框中输入ASN1结构体，红框中内容自行替换

      ![image-20221013132640579](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013132640579.png)

   2. 选择默认的编码格式"UPER"
      
      ![image-20221013133052652](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013133052652.png)
      
   3. 点击Compile，Results框会显示编译成功
   
      ![image-20221013132839642](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013132839642.png)
   
   4. 在文本框中输入需要加密的内容
   
      ![image-20221013132922448](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013132922448.png)
   
   5. 点击Encode，Output文本框中会显示加密后的内容
   
      ![image-20221013133017628](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013133017628.png)
      
   6. 将加密的内容（Hex）复制到Decode文本框
   
      ![image-20221013133205119](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013133205119.png)
   
   7. 点击Decode，Output文本框会显示解密后的内容
   
      ![image-20221013133311515](C:\Users\Haisong.Xu1\AppData\Roaming\Typora\typora-user-images\image-20221013133311515.png)

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

