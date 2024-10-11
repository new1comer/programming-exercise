import random
from pathlib import Path

def random_replace():
    #获取文件路径
    root_path = Path.cwd()
    file_path = Path(root_path).joinpath("exercise4", "Dataset_Xiang-Kuperberg_2015.txt")
    
    #检查文件路径
    if Path(file_path).exists():
        print("valid file path")
    else:
        print("Please check the path, as the path is invalid")
    
    #读取文件内容
    with Path(file_path).open("r", encoding="utf8") as file:
        texts = file.readlines()
        #创建新的文件内容的储存器
        new_texts = []
        new_texts.append(texts[0]) #加入不变的标题
        for text in texts[1:]: #利用切片去掉标题行
            tokenized_text = text.split("\t")
            sentence = tokenized_text[2]
            tokenized_sentence = sentence.split()
            
            #生成随机数并对取随机数与当前句子长度取余数以确保能够随机取到的index不超句子范围
            n = random.randint(0,100)
            word_index = n % len(tokenized_sentence)
            
            #替换为[UNK]
            tokenized_sentence[word_index] = "[UNK]"
            tokenized_text[2] = " ".join(tokenized_sentence)
            new_text = "\t".join(tokenized_text)
            new_texts.append(new_text)
        
        #创建并且写入输出文件
        output_path = Path(root_path).joinpath("exercise4", "random_replace_output.txt")
        with Path(output_path).open("w+", encoding="utf8") as file:
            for text in new_texts:
                file.write(text)
        
    return print(f"success, and the output path: {output_path}")        
           
     
    
    
    
if __name__  == "__main__":
    random_replace()