# 目标
开发一个向量数据库，封装为mcp服务，供一个agent远程调用

建议方案：
知识库采用langchain开发;  
MCP服务采用fastmcp开发;  
general agent采用autogen开发  

<img width="600" height="400" alt="图片" src="https://github.com/user-attachments/assets/6bcb4154-3a00-4de7-af86-fdc4179b36ce" />

# 部署指南
1.本地需安装ollama，并执行```ollama pull bge-m3```安装bge-m3作为嵌入模型划分向量  

2.相关依赖已保存至requirements.txt，执行```pip install -r requirements.txt```即可

3.需要在项目目录下(和run.py同级)创建```.env```文件，并接入deepseek的api  
```API_KEY="sk-123"```  

 关键词：Autogen,MCP,fastmcp,langchain,向量数据库,知识库
