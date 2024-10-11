from pathlib import Path
import re

def target_replace():
    #获取.txt文件的路径
    root_path = Path.cwd()
    file_path = Path(root_path).joinpath("exercise4", "Dataset_Xiang-Kuperberg_2015.txt")
    output_path = Path(root_path).joinpath("exercise4", "target_replace_output.txt")
    #检查文件路径是否存在
    if Path(file_path).exists:
        print("Valid file path")
    else:
        print("Please check the file path, as the file path is invalid")

    #读写模式打开文件
    with Path(file_path).open("r", encoding= "utf8") as file:
        texts = file.readlines()
        
        #创建替换后的文本储存器
        new_texts = []
        new_texts.append(texts[0]) #加入标题
        #print(new_texts)
    
        #通过切片去除第一行的标题行
        for text in texts[1:]:
            tokenized_text = text.split("\t")
            #利用制表符分词，index = 4为target，index = 2为sentence
            target_word = tokenized_text[4].rstrip() #去掉文本中的换行符号\n
            sentence = tokenized_text[2]
            
            #替换targetword为[MASK]
            new_sentence = re.sub(target_word, "[MASK]", sentence) 
            tokenized_text[2] = new_sentence
            text = "\t".join(tokenized_text)
            new_texts.append(text)
        
        
    
        #写入txt文档中
        with Path(output_path).open("w+", encoding="utf8") as file:
        
            for new_text in new_texts:
                file.write(new_text)
    return print(f"success, and the output path: {output_path}")
 
if __name__ == "__main__":
    target_replace()
       
      
            
        
        

        
   