douban="http://pypi.douban.com/simple/"
ali="http://mirrors.aliyun.com/pypi/simple/"
tsinghua="https://pypi.tuna.tsinghua.edu.cn/simple"

echo "开始创建venv"
python -m venv venv
if [ $? -ne 0 ]; then
  echo "faild" 1>&2
  exit 1
else
  echo "成功创建venv"
fi


echo "切换虚拟环境"
source ./venv/bin/activate
if [ $? -ne 0 ]; then
  echo "faild" 1>&2
  exit 1
else
  echo "成功切换虚拟环境"
fi

echo "pip安装依赖包"
pip install -r requirements.txt -i $tsinghua
if [ $? -ne 0 ]; then
  echo "faild" 1>&2
  exit 1
else
  echo "成功安装依赖包"
fi


echo "退出环境"
deactivate
