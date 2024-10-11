from pathlib import Path
import os
from itertools import zip_longest
'''
:param file1 第一个文件 even_index lines
:param file2 第二个文件 odd_index lines
:param output_path 输出文件路径
:return merged_file

'''
def text_merge(file1, file2):
    '''检查输出文件夹是否存在，如果不存在则创建新的输出路径'''
    
    my_path = Path(__file__).resolve() #该文件所在目录
    root = my_path.parent
    output_dir = Path.joinpath(root, "output")
    if not Path.exists(output_dir):
        #如果不存在则创建
        os.makedirs(output_dir)
        print(f"路径不存在，已创建: {output_dir}")
    else:
        print(f"路径已存在：{output_dir}")
        
  
    '''读取file1以及file2中的内容'''
    with Path(file1).open("r", encoding="utf-8") as tem_file1, Path(file2).open("r", encoding="utf-8") as tem_file2:
        
        line1 = tem_file1.readlines()
        line2 = tem_file2.readlines()
        
        # 创建输出文件
        output_file = os.path.join(output_dir, "output.txt")
        with open(output_file, 'w', encoding= "utf-8") as output_file:
            #先对得到的两个列表进行配对 
            zipped = zip_longest(line1, line2) 
            
            #按照规则对于配对后的迭代数据进行处理
           
            i = 0 #定义一个索引
            for (line1, line2) in zipped:
               
                
                if line1:
                     
                      #even index从第一个文件中取，即迭代器中的line1
                     output_file.write(f'{i}\t{file1.name}\t{line1.rstrip()}\n') 
                       #格式：           index  filename  content（去除换行符等)
                    
                     i += 1
                     
                    #odd index从第二个文件中取，即迭代器中的line2
                     output_file.write(f'{i}\t{file2.name}\t{line2.rstrip()}\n') 
                    
                    
                    
                     i += 1
                   
                else:
                    break
                    #遍历完所有语句后break跳出循环
                
    
    return "已处理完成"     
                        
if __name__  == "__main__":
    root_path = Path(__file__).resolve().parent
    resource_path = Path.joinpath(root_path, "resource")
    file1 =Path.joinpath(resource_path,"file1.txt")
    file2 =Path.joinpath(resource_path,"file2.txt")
    print(file1.name)
   
    
    print(text_merge(file1, file2))