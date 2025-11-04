import sys
import os

# fix python path if working locally

# 1. 현재 파일의 디렉터리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__)) # .py 파일일 경우
# 만약 Jupyter/Colab 환경이라면: current_dir = os.getcwd() 

# 2. 'utils.py'가 있는 상위 디렉터리를 sys.path에 추가합니다.
# 상위 디렉터리가 어딘지에 따라 경로를 조정해야 합니다.
# 예: utils.py가 현재 폴더의 부모 폴더에 있을 경우
parent_dir = os.path.join(current_dir, '..')

# 경로가 이미 추가되어 있지 않다면 추가합니다.
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# 3. 이제 커스텀 'utils' 모듈을 올바르게 불러올 수 있습니다.
try:
    from utils import fix_pythonpath_if_working_locally
    fix_pythonpath_if_working_locally()
except ImportError as e:
    print(f"경로를 수정했음에도 모듈 임포트 실패: {e}")
    print("utils.py 파일의 실제 위치를 확인하고 상위 경로 설정(parent_dir)을 조정하세요.")

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)