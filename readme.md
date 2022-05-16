通过github action在每天的北京时间10:00(2:00 UTC) 自动运行

使用说明：

  1. fork此仓库

  2. 在仓库的Settings -> Secrets -> Actions中新建两项secret：
  
      name:USERNAME  value:学号
    
      name:PASSWORD  value:密码

  注：在仓库的Actions中直接run workflow可以测试是否能正确运行
