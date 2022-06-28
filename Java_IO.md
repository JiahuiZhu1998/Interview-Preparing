JAVA I/O
===
    
  常用场景: 文件上传，文件下载，文件复制<br>
  Java I/O 分为 字节流(ByteStream) 和 字符流(CharacterStream)<br>
  
  **字节流(ByteStream) 又包含:**<br>
  
    字节输入流(FileInputStream   BufferedInputStream)
            fis = new FileInputStream(path);
            int size = fis.available();
            byte[] array = new byte[size];
            fis.read(array);
        
    字节输出流(FileOutputStream  BufferedOutputStream)
    
        方法1:
            File file = new File("src");  
            FileOutputStream fos = new FileOutputStream(file);
            fos.write(1);
        
        方法2:
            FileOutputStream fos = new FileOutputStream(new File("src"));
            fos.write(1);
  
    文件复制:
        
        复制字节流文件:
            FileInputStream fis = new FileInputStream("/Users/b/Desktop/java1.txt");
            FileOutputStream fos = new FileOutputStream("/Users/b/Desktop/java2.txt");

            int by;
            while ((by = fis.read()) != -1) {
                    fos.write((char)by);
            }

            fis.close();
            fos.close();
        
        复制byte流文件:
             FileInputStream fis = new FileInputStream("/Users/b/Desktop/Images/image-2.png");
            FileOutputStream fos = new FileOutputStream("/Users/b/Desktop/image1.png");

            byte[] b = new byte[1024];
            int len;
            while ((len = fis.read(b)) != -1){
                fos.write(b);
            }

            fis.close();
            fos.close();
        
        
  **字符流(CharacterStream)又包含:**<br>
    读 (FileReader  BufferedReader)<br>
    写 (FileWriter  BufferedWriter)<br>
