douban = "http://pypi.douban.com/simple/"
ali = "http://mirrors.aliyun.com/pypi/simple/"
tsinghua = "https://pypi.tuna.tsinghua.edu.cn/simple"

echo "开始创建venv"
python -m venv venv
echo "创建venv成功"

echo "切换虚拟环境"
source ./venv/Scripts/activate

echo "pip安装依赖包"
pip install -r requirements.txt -i $tsinghua

echo "退出环境"
deactivate
